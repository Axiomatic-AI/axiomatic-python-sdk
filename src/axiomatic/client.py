import base64
import requests
import os
import time
from typing import Dict

from .base_client import BaseClient, AsyncBaseClient
from . import ParseResponse


class Axiomatic(BaseClient):
    def __init__(self, *args, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = 1200
        super().__init__(*args, **kwargs)

        self.document_helper = DocumentHelper(self)
        self.tools_helper = ToolsHelper(self)


class DocumentHelper:
    _ax_client: Axiomatic

    def __init__(self, ax_client: Axiomatic):
        self._ax_client = ax_client

    def pdf_from_url(self, url: str) -> ParseResponse:
        """Download a PDF document from a URL and parse it into a Markdown response."""
        if "arxiv" in url and "abs" in url:
            url = url.replace("abs", "pdf")
            print("The URL is an arXiv abstract page. Replacing 'abs' with 'pdf' to download the PDF.")
        file = requests.get(url)
        response = self._ax_client.document.parse(file=file.content)
        return response

    def pdf_from_file(self, path: str) -> ParseResponse:
        """Open a PDF document from a file path and parse it into a Markdown response."""
        with open(path, "rb") as f:
            file = f.read()
        response = self._ax_client.document.parse(file=file)
        return response

    def plot_b64_images(self, images: Dict[str, str]):
        """Plot a dictionary of base64 images."""
        import ipywidgets as widgets  # type: ignore
        from IPython.display import display  # type: ignore

        base64_images = list(images.values())
        current_index = [0]

        def display_base64_image(index):
            image_widget.value = base64.b64decode(base64_images[index])

        def navigate_image(change):
            current_index[0] = (current_index[0] + change) % len(base64_images)
            display_base64_image(current_index[0])

        image_widget = widgets.Image(format="png", width=600)
        prev_button = widgets.Button(description="Previous", icon="arrow-left")
        next_button = widgets.Button(description="Next", icon="arrow-right")

        prev_button.on_click(lambda b: navigate_image(-1))
        next_button.on_click(lambda b: navigate_image(1))

        buttons = widgets.HBox([prev_button, next_button])
        layout = widgets.VBox([buttons, image_widget])

        display(layout)
        display_base64_image(current_index[0])

    def save_parsed_pdf(self, response: ParseResponse, path: str):
        """Save a parsed PDF response to a file."""
        os.makedirs(path, exist_ok=True)
        if response.images:
            for img_name, img in response.images.items():
                with open(os.path.join(path, f"{img_name}.png"), "wb") as f:
                    f.write(base64.b64decode(img))

        with open(os.path.join(path, "text.md"), "w") as f:
            f.write(response.markdown)

    def load_parsed_pdf(self, path: str) -> ParseResponse:
        """Load a parsed PDF response from a file."""
        with open(os.path.join(path, "text.md"), "r") as f:
            markdown = f.read()

        images = {}
        for img_name in os.listdir(path):
            if img_name.endswith((".png")):
                with open(os.path.join(path, img_name), "rb") as img_file:
                    images[img_name] = base64.b64encode(img_file.read()).decode("utf-8")

        return ParseResponse(markdown=markdown, images=images)


class ToolsHelper:
    _ax_client: Axiomatic

    def __init__(self, ax_client: Axiomatic):
        self._ax_client = ax_client

    def tool_exec(self, tool: str, code: str, poll_interval: int = 3, debug: bool = True):
        """
        Helper function to schedule code execution for a specific tool and wait
        the execution to finish and return the output or error trace
        """
        if not tool.strip():
            return "Please specify a tool"
        else:
            tool_name = tool.strip()
            code_string = code

            output = self._ax_client.tools.schedule(
                tool_name=tool_name,
                code=code_string,
            )
            if output.is_success is True:
                job_id = str(output.job_id)
                result = self._ax_client.tools.status(job_id=job_id)
                if debug:
                    print(f"job_id: {job_id}")
                while True:
                    result = self._ax_client.tools.status(job_id=job_id)
                    if result.status == "PENDING" or result.status == "RUNNING":
                        if debug:
                            print(f"status: {result.status}")
                        time.sleep(poll_interval)
                    else:
                        if debug:
                            print(f"status: {result.status}")
                        if result.status == "SUCCEEDED":
                            return result.output
                        else:
                            return result.error_trace
            else:
                return output.error_trace


class AsyncAxiomatic(AsyncBaseClient): ...
