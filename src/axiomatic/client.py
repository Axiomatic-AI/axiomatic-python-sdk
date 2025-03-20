import base64
import dill  # type: ignore
import json
import requests # type: ignore
import os
import time
from typing import Dict, Optional, Sequence

from .base_client import BaseClient, AsyncBaseClient
from . import ParseResponse, EquationProcessingResponse
from .axtract.axtract_report import create_report
from .axtract.validation_results import display_full_results
from .types.variable_requirement import VariableRequirement
from .types.equation_validation_result import EquationValidationResult


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
        with open(os.path.join(path, "text.md"), "w") as f:
            f.write(response.markdown)

        if response.images:
            for img_name, img in response.images.items():
                with open(os.path.join(path, f"{img_name}.png"), "wb") as f:
                    f.write(base64.b64decode(img))

        with open(os.path.join(path, "interline_equations.json"), "w") as f:
            json.dump(response.interline_equations, f)

        with open(os.path.join(path, "inline_equations.json"), "w") as f:
            json.dump(response.inline_equations, f)

    def load_parsed_pdf(self, path: str) -> ParseResponse:
        """Load a parsed PDF response from a file."""
        with open(os.path.join(path, "text.md"), "r") as f:
            markdown = f.read()

        images = {}
        for img_name in os.listdir(path):
            if img_name.endswith((".png")):
                with open(os.path.join(path, img_name), "rb") as img_file:
                    images[img_name] = base64.b64encode(img_file.read()).decode("utf-8")

        with open(os.path.join(path, "interline_equations.json"), "r") as f:
            interline_equations = json.load(f)

        with open(os.path.join(path, "inline_equations.json"), "r") as f:
            inline_equations = json.load(f)

        return ParseResponse(
            markdown=markdown,
            images=images,
            interline_equations=interline_equations,
            inline_equations=inline_equations,
        )

class AxtractHelper:
    _ax_client: Axiomatic

    def __init__(self, ax_client: Axiomatic):
        """Initialize the AxtractHelper with an Axiomatic client.

        Args:
            ax_client (Axiomatic): The Axiomatic client instance to use for API calls
        """
        self._ax_client = ax_client

    def create_report(self, response: EquationProcessingResponse, path: str):
        """Create a report from equation extraction results.

        Args:
            response (EquationExtractionResponse): The extracted equations and their metadata
            path (str): Directory path where the report should be saved
        """
        create_report(response, path)

    def analyze_equations(
        self,
        file_path: Optional[str] = None,
        url_path: Optional[str] = None,
        parsed_paper: Optional[ParseResponse] = None,
    ) -> Optional[EquationProcessingResponse]:
        """Analyze and extract equations from a scientific document.

        This method supports three input methods:
        1. Local PDF file path
        2. URL to a PDF (with special handling for arXiv URLs)
        3. Pre-parsed paper data

        Args:
            file_path (Optional[str]): Path to a local PDF file
            url_path (Optional[str]): URL to a PDF file (supports arXiv links)
            parsed_paper (Optional[ParseResponse]): Pre-parsed paper data

        Returns:
            Optional[EquationExtractionResponse]: Extracted equations and their metadata.
            Returns None if no valid input is provided.

        Examples:
            # From local file
            client.analyze_equations(file_path="path/to/paper.pdf")
            
            # From URL
            client.analyze_equations(url_path="https://arxiv.org/pdf/2203.00001.pdf")
            
            # From parsed paper
            client.analyze_equations(parsed_paper=parsed_data)
        """
        if file_path:
            with open(file_path, "rb") as pdf_file:
                parsed_document = self._ax_client.document.parse(file=pdf_file)
                print("We are almost there")
                response = self._ax_client.document.equation.process(
                    markdown=parsed_document.markdown, 
                    interline_equations=parsed_document.interline_equations,
                    inline_equations=parsed_document.inline_equations
                    )
        
        elif url_path:
            if "arxiv" in url_path and "abs" in url_path:
                url_path = url_path.replace("abs", "pdf")
            url_file = requests.get(url_path)
            from io import BytesIO
            pdf_stream = BytesIO(url_file.content)
            parsed_document = self._ax_client.document.parse(file=url_file.content)
            print("We are almost there")
            response = self._ax_client.document.equation.process(
                markdown=parsed_document.markdown, 
                interline_equations=parsed_document.interline_equations,
                inline_equations=parsed_document.inline_equations
                )
        
        elif parsed_paper:
            response = EquationProcessingResponse.model_validate(
                self._ax_client.document.equation.process(**parsed_paper.model_dump()).model_dump()
            )
        
        else:
            print("Please provide either a file path or a URL to analyze.")
            return None
        
        return response

    def validate_equations(
        self,
        requirements: Sequence[VariableRequirement],
        loaded_equations: EquationProcessingResponse,
        include_internal_model: bool = False,
    ) -> EquationValidationResult:
        """Validate equations against a set of variable requirements.

        Args:
            requirements: List of variable requirements to validate
            loaded_equations: Previously processed equations to validate
            show_hypergraph: Whether to display the validation results graph (default: True)
            include_internal_model: Whether to include internal model equations in validation (default: False)

        Returns:
            EquationValidationResult containing the validation results
        """
        # equations_dict = loaded_equations.model_dump() if hasattr(loaded_equations, 'model_dump') else loaded_equations.dict()
        
        api_response = self._ax_client.document.equation.validate(
            variables=requirements, 
            paper_equations=loaded_equations,
            include_internal_model=include_internal_model
            )
        
        return api_response
    

    def display_full_results(self, api_response: EquationValidationResult, user_choice):
        display_full_results(api_response, user_choice)
    

    def set_numerical_requirements(self, extracted_equations: EquationProcessingResponse):
        """Launch an interactive interface for setting numerical requirements for equations.

        This method opens an interactive table interface where users can specify
        requirements for variables found in the extracted equations.

        Args:
            extracted_equations: The equations to set requirements for

        Returns:
            The requirements set through the interactive interface
        """
        from .axtract.interactive_table import interactive_table

        result = interactive_table(extracted_equations)
        return result


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

            tool_result = self._ax_client.tools.schedule(
                tool_name=tool_name,
                code=code_string,
            )
            if tool_result.is_success is True:
                job_id = str(tool_result.job_id)
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
                            output = json.loads(result.output or "{}")
                            if not output['objects']:
                                return result.output
                            else:
                                return {
                                    "job_id": job_id,
                                    "messages": output['messages'],
                                    "objects": self._load_objects_from_base64(output['objects'])
                                }
                        else:
                            return result.error_trace
            else:
                return tool_result.error_trace

    def load(self, job_id: str, obj_key: str):
        result = self._ax_client.tools.status(job_id=job_id)
        if result.status == "SUCCEEDED":
            output = json.loads(result.output or "{}")
            if not output['objects']:
                return result.output
            else:
                return self._load_objects_from_base64(output['objects'])[obj_key]
        else:
            return result.error_trace

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


class AsyncAxiomatic(AsyncBaseClient): ...
