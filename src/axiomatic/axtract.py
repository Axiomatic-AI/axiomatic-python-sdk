import ipywidgets as widgets  # type: ignore
from IPython.display import display, Math, HTML  # type: ignore
import json  # type: ignore
import os
import hypernetx as hnx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import re
from dataclasses import dataclass, asdict

@dataclass
class RequirementUserInput:
    requirement_name: str
    latex_symbol: str
    value: int
    units: str
    tolerance: float


def _find_symbol(name, variable_dict):

    matching_keys = [
        key for key, value in variable_dict.items() if name in value["name"]
    ]

    if not matching_keys:
        matching_keys.append("unknown")

    return matching_keys[0]


def requirements_from_table(results, variable_dict):
    requirements = []

    for key, value in results["values"].items():

        latex_symbol = _find_symbol(key, variable_dict)

        name = key
        numerical_value = value["Value"]
        unit = value["Units"]

        requirements.append(
            RequirementUserInput(
                requirement_name=name,
                latex_symbol=latex_symbol,
                value=numerical_value,
                units=unit,
                tolerance=0.0,
            )
        )

    return requirements


def interactive_table(variable_dict, file_path="./custom_presets.json"):
    """
    Creates an interactive table for IMAGING_TELESCOPE,
    PAYLOAD, and user-defined custom templates.
    Adds or deletes rows, and can save custom templates persistently in JSON.

    Parameters
    ----------
    variable_dict : dict
        Dictionary used to populate the "Add Requirement" dropdown, e.g.:
          {
            "var_key1": {"name": "Human-readable variable name1"},
            "var_key2": {"name": "Human-readable variable name2"},
            ...
          }
    file_path : str, optional
        JSON file path where we load and save user-created custom templates.

    Returns
    -------
    dict
        Contains user inputs after pressing "Submit" button.
    """

    # ---------------------------------------------------------------
    # 1) Define built-in templates and units directly inside the function
    # ---------------------------------------------------------------
    IMAGING_TELESCOPE_template = {
        "Resolution (panchromatic)": 0,
        "Ground sampling distance (panchromatic)":0,
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
                    default_value = (
                        custom_presets[selected_option]
                        .get(row_name, {})
                        .get("Value", 0.0)
                    )
                    default_unit = (
                        custom_presets[selected_option]
                        .get(row_name, {})
                        .get("Units", "")
                    )
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
    def submit_values(_):
        updated_values = {}
        for k, widget in value_widgets.items():
            label_or_variable = widget.children[0].value
            val = widget.children[1].value
            unit = widget.children[2].value
            updated_values[label_or_variable] = {"Value": val, "Units": unit}

        result["values"] = updated_values

    # ---------------------------------------------------------------
    # 8) add_req(): Adds a new, blank row to the bottom
    # ---------------------------------------------------------------
    def add_req(_):
        unique_key = (f"req_{len([kk for kk in value_widgets if kk.startswith('req_')]) + 1}")

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
    custom_count = len(
        [k for k in preset_options_dict if k.startswith("Custom-")]
        )

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
    submit_button = widgets.Button(
        description="Submit", button_style="success")
    submit_button.on_click(submit_values)

    add_req_button = widgets.Button(
        description="Add Requirement", button_style="primary"
    )
    add_req_button.on_click(add_req)

    del_req_button = widgets.Button(
        description="Delete Requirement", button_style="danger"
    )
    del_req_button.on_click(delete_req)

    save_req_button = widgets.Button(description="Save", button_style="info")
    save_req_button.on_click(save_requirements)

    buttons_box = widgets.HBox(
        [submit_button, add_req_button, del_req_button, save_req_button]
    )
    display(buttons_box)

    return result



def _get_node_names_for_node_lables(node_labels, api_requirements):

    # Create the output list
    node_names = []

    # Iterate through each symbol in S
    for symbol in node_labels:
        # Search for the matching requirement
        symbol = symbol.replace("$", "")
        for req in api_requirements:
            if req["latex_symbol"] == symbol:
                # Add the matching tuple to SS
                node_names.append(
                    (req["latex_symbol"], req["requirement_name"])
                    )
                break  # Stop searching once a match is found

    return node_names


def _get_latex_string_format(input_string):
    """
    Properly formats LaTeX strings for matplotlib when text.usetex is False.
    No escaping needed since mathtext handles backslashes properly.
    """
    return f"${input_string}$"  # No backslash escaping required


def _get_requirements_set(requirements):
    variable_set = set()
    for req in requirements:
        variable_set.add(req["latex_symbol"])

    return variable_set


def _find_vars_in_eq(equation, variable_set):
    patterns = [re.escape(var) for var in variable_set]
    combined_pattern = r"|".join(patterns)
    matches = re.findall(combined_pattern, equation)
    return {rf"${match}$" for match in matches}


def _add_used_vars_to_results(api_results, api_requirements):
    requirements = _get_requirements_set(api_requirements)

    for key, value in api_results["results"].items():
        latex_equation = value.get("latex_equation")
        # print(latex_equation)
        if latex_equation:
            used_vars = _find_vars_in_eq(latex_equation, requirements)
            api_results["results"][key]["used_vars"] = used_vars

    return api_results


def display_full_results(equations_dict, requirements=None, show_hypergraph=True):
    """Display equation validation results optimized for dark theme notebooks."""
    results = equations_dict.get("results", {})
    
    def format_equation(latex_eq):
        inner = latex_eq[3:-1]
        lhs, rhs = inner.split(',', 1)
        return f"{lhs} = {rhs}"
    
    matching = []
    non_matching = []
    
    for key, value in results.items():
        equation_data = {
            'latex': format_equation(value.get('latex_equation')),
            'lhs': value.get('lhs'),
            'rhs': value.get('rhs'),
            'diff': abs(value.get('lhs', 0) - value.get('rhs', 0)),
            'percent_diff': abs(value.get('lhs', 0) - value.get('rhs', 0)) / max(abs(value.get('rhs', 0)), 1e-10) * 100
        }
        if value.get('match'):
            matching.append(equation_data)
        else:
            non_matching.append(equation_data)

    # Summary header with dark theme
    total = len(results)
    display(HTML(
        '<div style="background-color:#1e1e1e; padding:20px; border-radius:10px; margin:20px 0; '
        'border:1px solid #3e3e3e;">'
        f'<h2 style="font-family:Arial; color:#e0e0e0; margin-bottom:15px">Equation Validation Analysis</h2>'
        f'<p style="font-family:Arial; font-size:16px; color:#e0e0e0">'
        f'<b>Total equations analyzed:</b> {total}<br>'
        f'<span style="color:#4caf50">✅ Matching equations: {len(matching)}</span><br>'
        f'<span style="color:#ff5252">❌ Non-matching equations: {len(non_matching)}</span></p>'
        '</div>'
    ))

    # Non-matching equations
    if non_matching:
        display(HTML(
            '<div style="background-color:#2d1f1f; padding:20px; border-radius:10px; margin:20px 0; '
            'border:1px solid #4a2f2f;">'
            '<h3 style="color:#ff5252; font-family:Arial">⚠️ Equations Not Satisfied</h3>'
        ))
        
        for eq in non_matching:
            display(Math(eq['latex']))
            display(HTML(
                '<div style="font-family:monospace; margin-left:20px; margin-bottom:20px; '
                'background-color:#2a2a2a; color:#e0e0e0; padding:15px; border-radius:5px; '
                'border-left:4px solid #ff5252">'
                f'Left side  = {eq["lhs"]:.6g}<br>'
                f'Right side = {eq["rhs"]:.6g}<br>'
                f'Absolute difference = {eq["diff"]:.6g}<br>'
                f'Relative difference = {eq["percent_diff"]:.2f}%'
                '</div>'
            ))
        
        display(HTML('</div>'))

    # Matching equations
    if matching:
        display(HTML(
            '<div style="background-color:#1f2d1f; padding:20px; border-radius:10px; margin:20px 0; '
            'border:1px solid #2f4a2f;">'
            '<h3 style="color:#4caf50; font-family:Arial">✅ Satisfied Equations</h3>'
        ))
        
        for eq in matching:
            display(Math(eq['latex']))
            display(HTML(
                '<div style="font-family:monospace; margin-left:20px; margin-bottom:20px; '
                'background-color:#2a2a2a; color:#e0e0e0; padding:15px; border-radius:5px; '
                'border-left:4px solid #4caf50">'
                f'Value = {eq["lhs"]:.6g}'
                '</div>'
            ))
            
        display(HTML('</div>'))

    # Hypergraph visualization
    if show_hypergraph and requirements:
        display(HTML(
            '<div style="background-color:#1e1e1e; padding:20px; border-radius:10px; margin:20px 0; '
            'border:1px solid #3e3e3e;">'
            '<h3 style="color:#e0e0e0; font-family:Arial">🔍 Equation Relationship Analysis</h3>'
            '<p style="font-family:Arial; color:#e0e0e0">The following graph shows how variables are connected through equations:</p>'
            '</div>'
        ))
        
        list_api_requirements = [asdict(req) for req in requirements]
        
        # Match get_eq_hypergraph settings exactly
        plt.rcParams["text.usetex"] = False
        plt.rcParams["mathtext.fontset"] = "stix"
        plt.rcParams["font.family"] = "serif"

        equations_dict = _add_used_vars_to_results(equations_dict, list_api_requirements)

        # Prepare hypergraph data
        hyperedges = {}
        for eq, details in equations_dict["results"].items():
            hyperedges[
                _get_latex_string_format(details["latex_equation"])] = details["used_vars"]

        # Create and plot the hypergraph
        H = hnx.Hypergraph(hyperedges)
        plt.figure(figsize=(16, 12))

        # Draw hypergraph with exact same settings as get_eq_hypergraph
        hnx.draw(
            H,
            with_edge_labels=True,
            edge_labels_on_edge=False,
            node_labels_kwargs={"fontsize": 14},
            edge_labels_kwargs={"fontsize": 14},
            layout_kwargs={"seed": 42, "scale": 2.5},
        )

        node_labels = list(H.nodes)
        symbol_explanations = _get_node_names_for_node_lables(
            node_labels,
            list_api_requirements
        )
        
        explanation_text = "\n".join(
            [f"${symbol}$: {desc}" for symbol, desc in symbol_explanations]
        )
        plt.annotate(
            explanation_text,
            xy=(1.05, 0.5),
            xycoords="axes fraction",
            fontsize=14,
            verticalalignment="center",
        )
        
        plt.title(r"Enhanced Hypergraph of Equations and Variables", fontsize=20)
        plt.show()

    return None


def get_numerical_values(ax_client, path, constants_of_interest):  
    with open(path, "rb") as f:
        file = f.read()

    constants = ax_client.document.constants(file=file, constants=constants_of_interest).constants
    print(constants)
    # Create a dictionary to store processed values
    processed_values = {}
    
    # Process each constant name from the constants dictionary
    for constant_name in constants:
        value_str = constants[constant_name]  # Get the value directly from the dictionary
        
        if value_str is None:
            # Handle None values
            processed_values[constant_name] = {
                "Value": 0.0,
                "Units": "unknown"
            }
        elif 'F/' in value_str:
            # Handle F-number values
            f_number = float(value_str.split('/')[-1])
            processed_values[constant_name] = {
                "Value": f_number,
                "Units": "dimensionless"
            }
        elif 'f/' in value_str:
            # Handle F-number values
            f_number = float(value_str.split('/')[-1])
            processed_values[constant_name] = {
                "Value": f_number,
                "Units": "dimensionless"
            }
        else:
            # Handle normal values with units
            # Split on the last space to separate value and unit
            parts = value_str.rsplit(' ', 1)
            if len(parts) == 2:
                value, unit = parts
                # Convert value to float
                value = float(value)
                
                # Handle unit conversions to meters
                if unit == "\u00b5m":  # micrometer
                    value *= 1e-6
                    unit = "m"
                elif unit == "mm":  # millimeter
                    value *= 1e-3
                    unit = "m"
                elif unit == "km":  # kilometer
                    value *= 1e3
                    unit = "m"
                # Handle degree conversions to radians
                elif unit in ["deg", "°", "degree", "degrees"]:  # degrees
                    value = value * (3.14159265359 / 180.0)  # convert to radians
                    unit = "rad"
                
                processed_values[constant_name] = {
                    "Value": value,
                    "Units": unit
                }
            else:
                # If no unit is found
                processed_values[constant_name] = {
                    "Value": float(parts[0]),
                    "Units": "unknown"
                }
    
    # Save as custom preset
    filename = os.path.basename(path)
    with open("./custom_presets.json", "r+") as f:
        presets = json.load(f)
        presets[filename] = processed_values
        f.seek(0)
        json.dump(presets, f, indent=2)
        f.truncate()

    return processed_values