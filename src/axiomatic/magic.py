import platformdirs # type: ignore
import os


from . import Axiomatic


class AXMagic:
    """Class implementing magic functions for IPython.
    Import with `%load_ext axiomatic.magic`."""

    def __init__(self):
        self.folder = platformdirs.user_config_dir("axiomatic")
        if not os.path.exists(f"{self.folder}/api_key"):
            os.makedirs(self.folder, exist_ok=True)
            self.api_key = None
        else:
            with open(f"{self.folder}/api_key", "r") as f:
                self.api_key = f.read()
            self.ax = Axiomatic(api_key=self.api_key)

    def ax_api(self, query):
        folder = platformdirs.user_config_dir("axiomatic")
        with open(f"{folder}/api_key", "w") as f:
            f.write(query)
            self.api = query
            self.ax = Axiomatic(api_key=self.api)
            print("API key set.")

    def ax_query(self, query, cell=None):
        # NOTE: we need to add additional dependencies to the requirements!
        # TODO: This would actually be a different dependency group
        # we don't want to force users to install IPython!
        from IPython import get_ipython # type: ignore
        from IPython.core.magic import register_line_cell_magic, register_line_magic # type: ignore
        from IPython.display import HTML, display # type: ignore

        if self.api_key:
            result = self.ax.experimental.magic_request(query=query, cell=cell)
            display(HTML(result.response))

            try:
                # When running in colab
                from google.colab import _frontend # type: ignore

                _frontend.create_scratch_cell(
                    f"""# {query}\n{result.code}""", bottom_pane=True
                )
            except Exception as e:
                # When running in jupyter
                get_ipython().set_next_input(f"{result.code}", replace=False)

        else:
            print(
                "Please set your Axiomatic API key first with the command %ax_api API_KEY. Request the api key at our Customer Service."
            )

    def ax_fix(self, query, cell=None):
        # Just dummy at the moment
        return self.ax_query(query, cell)


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
