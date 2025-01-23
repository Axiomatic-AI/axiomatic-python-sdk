import base64
import requests
from typing import Dict

from .base_client import BaseClient, AsyncBaseClient
from . import MdResponse


class Axiomatic(BaseClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.document_helper = DocumentHelper(self)


class DocumentHelper:

    def __init__(self, ax_client: Axiomatic):
        self.ax_client = ax_client

    def pdf_from_url(self, url: str) -> MdResponse:
        """Download a PDF document from a URL and parse it into a Markdown response."""
        file = requests.get(url)
        response = self.ax_client.document.parse(file=file.content)
        return response.content

    def pdf_from_file(self, path: str) -> MdResponse:
        """Open a PDF document from a file path and parse it into a Markdown response."""
        with open(path, "rb") as f:
            file = f.read()
        response = self.ax_client.document.parse(file=file)
        return response.content

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


class AsyncAxiomatic(AsyncBaseClient): ...
