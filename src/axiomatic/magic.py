from IPython import get_ipython  # type: ignore
from IPython.display import HTML, display  # type: ignore

import platformdirs  # type: ignore
import os
import sys
import time
import json
import base64
import dill  # type: ignore
from . import Axiomatic


class AXMagic:
    """Class implementing magic functions for IPython.
    Import with `%load_ext axiomatic.magic`."""

    client: Axiomatic
    query: str

    def __init__(self):
        self.folder = platformdirs.user_config_dir("axiomatic")

        self.client = Axiomatic()
        self.query = ""

    def ax_api(self, *args, **kwargs):
        pass

    def axquery(self, query, cell=None):
        if cell:
            # REFINE
            try:
                exec(cell)
                feedback = "Code executed successfully."
            except Exception as e:
                feedback = f"Errors:\n{e}"
            print(feedback)
            current_query = f"{self.query}\n{query}"
            result = self.client.pic.circuit.refine(query=current_query, code=cell, feedback=feedback)
        else:
            # GENERATE FROM SCRATCH
            self.query = query
            result = self.client.pic.circuit.generate(query=query)

        # Process output
        pre_thought = result.raw_content.split("<thought>")[0]
        thought = result.thought_text.replace("\n", "<br>")
        if not thought:
            output = result.raw_content.replace("\n", "<br>")
        else:
            output = pre_thought + "<br>" + thought
        html_content = f"""<div style='font-family: Arial, sans-serif; line-height: 1.5;'>"
<div style='color: #6EB700;'><strong>AX:</strong> {output}</div>"""
        display(HTML(html_content))

        # Process code
        # remove last three lines (saving file)
        if result.code:
            code = "\n".join(result.code.split("\n")[:-3] + ["c"])
            if "google.colab" in sys.modules:
                # When running in colab
                from google.colab import _frontend  # type: ignore

                _frontend.create_scratch_cell(f"""# {query}\n# %%ax_fix\n{code}""", bottom_pane=True)
            else:
                # When running in jupyter
                get_ipython().set_next_input(f"# %%ax_fix\n{code}", replace=False)

    def ax_query(self, query, cell=None):
        # Updates the target circuit query
        self.query = query
        return self.axquery(query, cell)

    def ax_fix(self, query, cell=None):
        # Runs again without updating the query
        return self.axquery(query, cell)

    def ax_tool(self, tool, cell):
        """
        A custom IPython cell magic that sends python code in a cell to the tools scheduling API
        using Axiomatic's `client.tools.schedule` and wait for the tool execution to finish and
        show the 'stdout' of the script

        Usage:

            %%tool_schedule [optional_tool_name]
            <some code here>

        Example:

            %%tool_schedule fdtd
            print("Hello from this cell!")
            x = 1 + 2

        This cell won't run as Python code; instead, the text will be sent to the tool_schedule method
        of the Axiomatic client.
        """
        if not tool.strip():
            print("Please provider a tool name when calling this magic like:  %%tool_schedule [optional_tool_name]")
            tools = self.client.tools.list()
            print("Available tools are:")
            for tool in tools.tools_list:
                print(f"- {tool}")
        else:
            tool_name = tool.strip()
            code_string = cell

            output = self.client.tools.schedule(
                tool_name=tool_name,
                code=code_string,
            )
            if output.is_success is True:
                job_id = output.job_id
                result = self.client.tools.status(job_id=output.job_id)
                print(f"job_id: {job_id}")
                while True:
                    result = self.client.tools.status(job_id=output.job_id)
                    if result.status == "PENDING" or result.status == "RUNNING":
                        time.sleep(3)
                    else:
                        if result.status == "SUCCEEDED":
                            os.environ["TOOL_RESULT"] = result.output
                            output = json.loads(result.output)
                            if not output['objects']:
                                get_ipython().user_ns["tool_result"] = output
                            else:
                                get_ipython().user_ns["tool_result"] = {
                                    "job_id": job_id,
                                    "messages": output['messages'],
                                    "objects": self._load_objects_from_base64(output['objects'])
                                }
                            print("SUCCEEDED: access the execution result with tool_result variable.")
                        else:
                            print(result.error_trace)
                        break
            else:
                print(output.error_trace)

    def _load_objects_from_base64(self, encoded_dict):
        loaded_objects = {}
        for key, encoded_str in encoded_dict.items():
            try:
                decoded_bytes = base64.b64decode(encoded_str)
                loaded_obj = dill.loads(decoded_bytes)
                loaded_objects[key] = loaded_obj
            except Exception as e:
                print(f"Error loading object for key '{key}': {e}")
                loaded_objects[key] = None
        return loaded_objects


def ax_help(value: str):
    print(
        """
Available commands:

- `%load_ext axiomatic_pic` loads the ipython extension.
- `%ax_query` returns the requested circuit using our experimental API
- `%%ax_fix` edit the given code
- `%%ax_tool tool_name` executes python code for a given tool. Available tools are:
  `fdtd, femwell, jaxfem, optiland, pyspice and sax-gdsfactory`
"""
    )


def load_ipython_extension(ipython):
    ax_magic = AXMagic()
    ipython.register_magic_function(ax_magic.ax_query, "line_cell")
    ipython.register_magic_function(ax_magic.ax_fix, "line_cell")
    ipython.register_magic_function(ax_magic.ax_api, "line")
    ipython.register_magic_function(ax_magic.ax_tool, "cell")
    ipython.register_magic_function(ax_help, "line")
