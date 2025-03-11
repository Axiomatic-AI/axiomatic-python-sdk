import ipywidgets as widgets  # type: ignore
from IPython.display import display  # type: ignore
import json  # type: ignore
import os  # type: ignore
from .. import EquationExtractionResponse, VariableRequirement


def _find_symbol(name, variable_dict):
    matching_keys = [key for key, value in variable_dict.items() if name in value["name"]]

    if not matching_keys:
        matching_keys.append("unknown")

    return matching_keys[0]


def _requirements_from_table(results, variable_dict):
    requirements = []

    for key, value in results["values"].items():
        latex_symbol = _find_symbol(key, variable_dict)

        requirements.append(
            VariableRequirement(
                symbol=latex_symbol,
                name=key,
                value=value["Value"],
                units=value["Units"],
                tolerance=0.0,
            )
        )

    return requirements


def interactive_table(loaded_equations, file_path="./custom_presets.json"):
    """
    Creates an interactive table for IMAGING_TELESCOPE,
    PAYLOAD, and user-defined custom templates.
    Adds or deletes rows, and can save custom templates persistently in JSON.

    Parameters
    ----------
    loaded_equations : EquationExtractionResponse
        The extracted equations containing variable information
    file_path : str, optional
        JSON file path where we load and save user-created custom templates.

    Returns
    -------
    list
        List of VariableRequirement objects after pressing "Submit" button.
    """

    # ---------------------------------------------------------------
    # 1) Define built-in templates and units directly inside the function
    # ---------------------------------------------------------------
    IMAGING_TELESCOPE_template = {
        "Resolution (panchromatic)": 0,
        "Ground sampling distance (panchromatic)": 0,
        "Resolution (multispectral)": 0,
        "Ground sampling distance (multispectral)": 0,
        "Altitude": 0,
        "Half field of view": 0,
        "Mirror aperture": 0,
        "F-number": 0,
        "Focal length": 0,
        "Pixel size (panchromatic)": 0,
        "Pixel size (multispectral)": 0,
        "Swath width": 0,
    }

    IMAGING_TELESCOPE = {
        "Resolution (panchromatic)": 1.23529,
        "Ground sampling distance (panchromatic)": 0.61765,
        "Resolution (multispectral)": 1.81176,
        "Ground sampling distance (multispectral)": 0.90588,
        "Altitude": 420000,
        "Half field of view": 0.017104227,
        "Mirror aperture": 0.85,
        "F-number": 6.0,
        "Focal length": 5.1,
        "Pixel size (panchromatic)": 7.5e-6,
        "Pixel size (multispectral)": 11e-6,
        "Swath width": 14368.95,
    }

    IMAGING_TELESCOPE_UNITS = {
        "Resolution (panchromatic)": "m",
        "Ground sampling distance (panchromatic)": "m",
        "Resolution (multispectral)": "m",
        "Ground sampling distance (multispectral)": "m",
        "Altitude": "m",
        "Half field of view": "rad",
        "Mirror aperture": "m",
        "F-number": "dimensionless",
        "Focal length": "m",
        "Pixel size (panchromatic)": "m",
        "Pixel size (multispectral)": "m",
        "Swath width": "m",
    }

    PAYLOAD_1 = {
        "Resolution (panchromatic)": 15.4,
        "Ground sampling distance (panchromatic)": 7.7,
        "Resolution (multispectral)": 0.0,
        "Ground sampling distance (multispectral)": 0.0,
        "Altitude": 420000,
        "Half field of view": 0.005061455,
        "Mirror aperture": 0.85,
        "F-number": 1.0,
        "Focal length": 0.3,
        "Pixel size (panchromatic)": 5.5e-6,
        "Swath width": 4251.66,
    }

    # ---------------------------------------------------------------
    # 2) Create a preset_options_dict with built-in templates
    # ---------------------------------------------------------------
    preset_options_dict = {
        "Select a template": [],
        "IMAGING TELESCOPE": list(IMAGING_TELESCOPE.keys()),
        "IMAGING TELESCOPE template": list(IMAGING_TELESCOPE_template.keys()),
        "PAYLOAD": list(PAYLOAD_1.keys()),
    }

    # ---------------------------------------------------------------
    # 3) Helper functions for loading/saving custom presets from JSON
    # ---------------------------------------------------------------
    def load_custom_presets(file_path):
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return json.load(f)
        return {}

    def save_custom_presets(custom_data, file_path):
        with open(file_path, "w") as f:
            json.dump(custom_data, f, indent=2)

    # ---------------------------------------------------------------
    # 4) Load custom presets from JSON (if any) and integrate them
    # ---------------------------------------------------------------
    variable_dict = _create_variable_dict(loaded_equations)
    custom_presets = load_custom_presets(file_path)

    for custom_name, values_dict in custom_presets.items():
        preset_options_dict[custom_name] = list(values_dict.keys())

    # ---------------------------------------------------------------
    # 5) For the "Add Requirement" dropdown
    # ---------------------------------------------------------------
    variable_names = [details["name"] for details in variable_dict.values()]

    # This dict will store the final user inputs after pressing "Submit"
    result = {}

    # Main dropdown to pick a template
    dropdown = widgets.Dropdown(
        options=list(preset_options_dict.keys()),
        description="Select Option:",
        style={"description_width": "initial"},
    )

    # Container for all rows (including the header)
    rows_output = widgets.VBox()
    # Container for user messages
    message_output = widgets.Output()

    # We'll dynamically resize this label width
    name_label_width = ["150px"]

    # Dictionary to keep track of row widget references
    value_widgets = {}

    # ---------------------------------------------------------------
    # 6) display_table(change): Re-populate rows when user selects a template
    # ---------------------------------------------------------------
    def display_table(change):
        selected_option = change["new"]

        # Clear existing rows in the GUI
        rows_output.children = ()
        value_widgets.clear()

        if selected_option in preset_options_dict:
            rows = preset_options_dict[selected_option]

            if selected_option != "Select a template" and len(rows) > 0:
                max_name_length = max(len(r) for r in rows)
                name_label_width[0] = f"{max_name_length + 2}ch"
            else:
                name_label_width[0] = "42ch"

            # Create a header row
            header_labels = [
                widgets.Label(
                    value="Name",
                    layout=widgets.Layout(width=name_label_width[0]),
                    style={"font_weight": "bold"},
                ),
                widgets.Label(
                    value="Value",
                    layout=widgets.Layout(width="150px"),
                    style={"font_weight": "bold"},
                ),
                widgets.Label(
                    value="Units",
                    layout=widgets.Layout(width="150px"),
                    style={"font_weight": "bold"},
                ),
            ]
            header = widgets.HBox(header_labels)
            header.layout = widgets.Layout(
                border="1px solid black",
                padding="5px",
            )
            rows_output.children += (header,)

            for row_name in rows:
                # Figure out default values if it's one of our built-ins
                if selected_option == "IMAGING TELESCOPE":
                    default_value = IMAGING_TELESCOPE.get(row_name, 0.0)
                    default_unit = IMAGING_TELESCOPE_UNITS.get(row_name, "")
                elif selected_option == "PAYLOAD":
                    default_value = PAYLOAD_1.get(row_name, 0.0)
                    default_unit = IMAGING_TELESCOPE_UNITS.get(row_name, "")
                elif selected_option in custom_presets:
                    default_value = custom_presets[selected_option].get(row_name, {}).get("Value", 0.0)
                    default_unit = custom_presets[selected_option].get(row_name, {}).get("Units", "")
                else:
                    default_value = 0.0
                    default_unit = ""

                name_label = widgets.Label(
                    value=row_name,
                    layout=widgets.Layout(width=name_label_width[0]),
                )
                value_text = widgets.FloatText(
                    value=default_value,
                    layout=widgets.Layout(width="150px"),
                )
                units_text = widgets.Text(
                    value=default_unit,
                    layout=widgets.Layout(width="150px"),
                )

                row = widgets.HBox([name_label, value_text, units_text])
                value_widgets[row_name] = row
                rows_output.children += (row,)

    dropdown.observe(display_table, names="value")

    # Display the UI
    display(dropdown)
    display(rows_output)
    display(message_output)

    # ---------------------------------------------------------------
    # 7) submit_values(): Gather the current table's values into `result`
    # ---------------------------------------------------------------
    # Store the requirements to return later
    requirements_result = [None]  # Using a list to store mutable reference

    def submit_values(_):
        updated_values = {}
        for k, widget in value_widgets.items():
            label_or_variable = widget.children[0].value
            val = widget.children[1].value
            unit = widget.children[2].value
            updated_values[label_or_variable] = {"Value": val, "Units": unit}

        result["values"] = updated_values
        requirements_result[0] = _requirements_from_table(result, variable_dict)

        # Display a confirmation message
        with message_output:
            message_output.clear_output()
            print("Requirements submitted successfully!")

        return requirements_result[0]

    # ---------------------------------------------------------------
    # 8) add_req(): Adds a new, blank row to the bottom
    # ---------------------------------------------------------------
    def add_req(_):
        unique_key = f"req_{len([kk for kk in value_widgets if kk.startswith('req_')]) + 1}"

        variable_dropdown = widgets.Dropdown(
            options=variable_names,
            description="Variable:",
            style={"description_width": "initial"},
            layout=widgets.Layout(width=str(50) + "ch"),
        )
        value_text = widgets.FloatText(
            placeholder="Value",
            layout=widgets.Layout(width="150px"),
        )
        units_text = widgets.Text(
            placeholder="Units",
            layout=widgets.Layout(width="150px"),
        )

        new_row = widgets.HBox([variable_dropdown, value_text, units_text])
        rows_output.children += (new_row,)
        value_widgets[unique_key] = new_row

    # ---------------------------------------------------------------
    # 9) delete_req(): Delete the last row (if there's more than the header)
    # ---------------------------------------------------------------
    def delete_req(_):
        with message_output:
            message_output.clear_output()
            if len(rows_output.children) > 1:
                children_list = list(rows_output.children)
                last_row = children_list.pop()  # remove from display
                rows_output.children = tuple(children_list)

                # remove from the dictionary
                for k in reversed(list(value_widgets.keys())):
                    if value_widgets[k] is last_row:
                        del value_widgets[k]
                        break
            else:
                print("No row available to delete.")

    # ---------------------------------------------------------------
    # 10) save_requirements():
    #   - Gathers rows,
    #   - Creates a new "custom_n" entry in preset_options_dict,
    #   - Also updates custom_presets + JSON file,
    #   - So it persists across restarts.
    # ---------------------------------------------------------------
    custom_count = len([k for k in preset_options_dict if k.startswith("Custom-")])

    def save_requirements(_):
        nonlocal custom_count
        custom_count += 1
        new_option_name = f"custom_{custom_count}"

        # Gather current row data
        updated_values = {}
        for key, widget in value_widgets.items():
            row_label = widget.children[0].value
            val = widget.children[1].value
            unit = widget.children[2].value
            updated_values[row_label] = {"Value": val, "Units": unit}

        # Get row names for the new template
        new_template_rows = list(updated_values.keys())

        # Insert new key into preset_options_dict so it appears in dropdown
        preset_options_dict[new_option_name] = new_template_rows

        # Store the data in custom_presets
        custom_presets[new_option_name] = updated_values

        # Persist to JSON
        save_custom_presets(custom_presets, file_path)

        # Update the dropdown
        dropdown.options = list(preset_options_dict.keys())

    # ---------------------------------------------------------------
    # 11) Create & display the buttons
    # ---------------------------------------------------------------
    submit_button = widgets.Button(description="Submit", button_style="success")
    submit_button.on_click(submit_values)

    add_req_button = widgets.Button(description="Add Requirement", button_style="primary")
    add_req_button.on_click(add_req)

    del_req_button = widgets.Button(description="Delete Requirement", button_style="danger")
    del_req_button.on_click(delete_req)

    save_req_button = widgets.Button(description="Save", button_style="info")
    save_req_button.on_click(save_requirements)

    buttons_box = widgets.HBox([submit_button, add_req_button, del_req_button, save_req_button])
    display(buttons_box)

    # Return the requirements object directly - it will be updated when submit is clicked
    return requirements_result


def _create_variable_dict(equation_response: EquationExtractionResponse) -> dict:
    """
    Creates a variable dictionary from an EquationExtractionResponse object
    for use with the interactive_table function.

    Parameters
    ----------
    equation_response : EquationExtractionResponse
        The equation extraction response containing equations and their symbols

    Returns
    -------
    dict
        A dictionary in the format:
        {
            "symbol1": {"name": "Human-readable description1"},
            "symbol2": {"name": "Human-readable description2"},
            ...
        }
    """
    variable_dict = {}

    # Iterate through all equations and their symbols
    for equation in equation_response.equations:
        for symbol in equation.latex_symbols:
            # Only add if not already present (avoid duplicates)
            if symbol.key not in variable_dict:
                variable_dict[symbol.key] = {"name": symbol.value}

    return variable_dict
