import base64
import requests
import os
from typing import Dict

from .base_client import BaseClient, AsyncBaseClient
from . import ParseResponse


class Axiomatic(BaseClient):

    def __init__(self, *args, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = 600
        super().__init__(*args, **kwargs)

        self.document_helper = DocumentHelper(self)


class DocumentHelper:

    _ax_client: Axiomatic

    def __init__(self, ax_client: Axiomatic):
        self._ax_client = ax_client

    def pdf_from_url(self, url: str) -> ParseResponse:
        """Download a PDF document from a URL and parse it into a Markdown response."""
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


class AsyncAxiomatic(AsyncBaseClient): ...
