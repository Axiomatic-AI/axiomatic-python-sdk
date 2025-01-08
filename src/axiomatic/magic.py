from IPython import get_ipython  # type: ignore
from IPython.core.magic import register_line_cell_magic, register_line_magic  # type: ignore
from IPython.display import HTML, display  # type: ignore
from typing import Optional

import platformdirs  # type: ignore
import os
import sys
from . import Axiomatic


class AXMagic:
    """Class implementing magic functions for IPython.
    Import with `%load_ext axiomatic.magic`."""

    api_key: str
    client: Axiomatic
    query: str

    def __init__(self, api_key: Optional[str] = os.getenv("AXIOMATIC_API_KEY")):
        self.folder = platformdirs.user_config_dir("axiomatic")

        self.api_key = api_key
        self.client = Axiomatic(api_key=api_key)
        self.query = ""

    def ax_api(self, query):
        pass

    def axquery(self, query, cell=None):
        if self.api_key:
            if cell:
                # REFINE
                try:
                    exec(cell)
                    feedback = "Code executed successfully."
                except Exception as e:
                    feedback = f"Errors:\n{e}"
                print(feedback)
                current_query = f"{self.query}\n{query}"
                result = self.client.pic.refine(
                    query=current_query, code=cell, feedback=feedback
                )
            else:
                # GENERATE FROM SCRATCH
                self.query = query
                result = self.client.pic.generate(query=query)

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

                    _frontend.create_scratch_cell(
                        f"""# {query}\n# %%ax_fix\n{code}""", bottom_pane=True
                    )
                else:
                    # When running in jupyter
                    get_ipython().set_next_input(f"# %%ax_fix\n{code}", replace=False)

        else:
            print(
                "Please set your Axiomatic API key first with the command %ax_api API_KEY and restart the kernel. Request the api key at our Customer Service."
            )

    def ax_query(self, query, cell=None):
        # Updates the target circuit query
        self.query = query
        return self.axquery(query, cell)

    def ax_fix(self, query, cell=None):
        # Runs again without updating the query
        return self.axquery(query, cell)


def ax_help(value: str):
    print(
        """
Available commands:

- `%load_ext axiomatic_pic` loads the ipython extension.
- `%ax_api` sets up the API key
- `%ax_query` returns the requested circuit using our experimental API
- `%%ax_fix` edit the given code
"""
    )


def load_ipython_extension(ipython):
    ax_magic = AXMagic()
    ipython.register_magic_function(ax_magic.ax_query, "line_cell")
    ipython.register_magic_function(ax_magic.ax_fix, "line_cell")
    ipython.register_magic_function(ax_magic.ax_api, "line")
    ipython.register_magic_function(ax_help, "line")
