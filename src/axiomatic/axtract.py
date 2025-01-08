import ipywidgets as widgets # type: ignore
from IPython.display import display, Math, HTML # type: ignore
from dataclasses import dataclass, field
import hypernetx as hnx # type: ignore
import matplotlib.pyplot as plt # type: ignore
import re

OPTION_LIST = {
    "Select a template": [],
    "IMAGING TELESCOPE": [
        "Resolution (panchromatic)",
        "Ground sampling distance (panchromatic)",
        "Resolution (multispectral)",
        "Ground sampling distance (multispectral)",
        "Altitude",
        "Half field of view",
        "Mirror aperture",
        "F-number",
        "Focal length",
        "Pixel size (panchromatic)",
        "Pixel size (multispectral)",
        "Swath width",
    ],
    "PAYLOAD": [
        "Resolution (panchromatic)",
        "Ground sampling distance (panchromatic)",
        "Resolution (multispectral)",
        "Ground sampling distance (multispectral)",
        "Altitude",
        "Half field of view",
        "Mirror aperture",
        "F-number",
        "Focal length",
        "Pixel size (panchromatic)",
        "Swath width",
    ],
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
    "Ground sampling distance (multispectral)": 0.,
    "Altitude": 420000,
    "Half field of view": 0.005061455,
    "Mirror aperture": 0.85,
    "F-number": 1.,
    "Focal length": 0.3,
    "Pixel size (panchromatic)": 5.5e-6,
    "Swath width": 4251.66,
}


@dataclass
class Requirement:
    requirement_name: str
    latex_symbol: str
    value: int
    units: str
    tolerance: float
    sympy_symbol: str = field(init=False)

    def __post_init__(self):
        self.sympy_symbol = self.latex_symbol.replace("{", "").replace("}", "")

    @property
    def is_fixed(self):
        return self.tolerance == 0.0


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
            Requirement(
                requirement_name=name,
                latex_symbol=latex_symbol,
                value=numerical_value,
                units=unit,
                tolerance=0.0,
            )
        )

    return requirements


def interactive_table(preset_options_dict, variable_dict):
    """
    Creates an interactive table with a dropdown for selecting options.

    Parameters:
    options_dict (dict): A dictionary where keys are dropdown options and
      values are lists of row names.

    Returns:
    dict: A dictionary containing user inputs for the selected rows.
    """

    variable_names = [details["name"] for details in variable_dict.values()]

    # Placeholder for result dictionary
    result = {}

    # Create dropdown for options
    dropdown = widgets.Dropdown(
        options=list(preset_options_dict.keys()),
        description="Select Option:",
        style={"description_width": "initial"},
    )

    # Dictionary to hold widgets for user input
    value_widgets = {}

    # VBox to stack rows vertically
    rows_output = widgets.VBox()

    # Output widget for confirmation messages
    message_output = widgets.Output()

    # Mutable container to store the current name label width
    name_label_width = ["150px"]  # Default width

    # Function to display the table based on the dropdown selection
    def display_table(change):
        selected_option = change["new"]

        # Clear existing rows
        rows_output.children = []
        value_widgets.clear()

        if selected_option in preset_options_dict:
            rows = preset_options_dict[selected_option]

            if selected_option != "Select a template":
                max_name_length = max(len(name) for name in rows)
                # Update the name_label_width based on the longest row name
                name_label_width[0] = f"{max_name_length + 2}ch"
            else:
                max_name_length = 40
                # Update the name_label_width based on the longest row name
                name_label_width[0] = f"{max_name_length + 2}ch"

            # Add Headers
            header_labels = [
                widgets.Label(
                    value="Name",
                    layout=widgets.Layout(width=name_label_width[0]),
                    style={'font_weight': 'bold'}
                ),
                widgets.Label(
                    value="Value",
                    layout=widgets.Layout(width="150px"),
                    style={'font_weight': 'bold'}
                ),
                widgets.Label(
                    value="Units",
                    layout=widgets.Layout(width="150px"),
                    style={'font_weight': 'bold'}
                ),
            ]

            # Combine header labels into a horizontal box
            header = widgets.HBox(header_labels)
            header.layout = widgets.Layout(
                border='1px solid black',
                padding='5px',
            )

            # Add the header to the rows_output VBox
            rows_output.children += (header,)

            for row_name in rows:
                # Create name label with dynamic width
                name_label = widgets.Label(
                    value=row_name,
                    layout=widgets.Layout(width=name_label_width[0]),
                )

                # Depending on the selected option, set default values
                if selected_option == "IMAGING TELESCOPE":
                    default_value = IMAGING_TELESCOPE.get(row_name, 0.0)
                    default_unit = IMAGING_TELESCOPE_UNITS.get(row_name, "")
                # elif selected_option == "LIDAR":
                #     default_value = LIDAR.get(row_name, 0.0)
                elif selected_option == "PAYLOAD":
                    default_value = PAYLOAD_1.get(row_name, 0.0)
                    default_unit = IMAGING_TELESCOPE_UNITS.get(row_name, "")
                else:
                    default_value = 0.0
                    default_unit = ""

                # Create input widgets
                value_text = widgets.FloatText(
                    value=default_value,
                    layout=widgets.Layout(width="150px"),
                )
                units_text = widgets.Text(
                    layout=widgets.Layout(width="150px"),
                    value=default_unit
                )

                # Combine widgets into a horizontal box
                row = widgets.HBox(
                    [
                        name_label,
                        value_text,
                        units_text,
                    ]
                )

                # Store the row widgets
                value_widgets[row_name] = row

                # Add the row to the rows_output VBox
                rows_output.children += (row,)

    # Attach handler to dropdown
    dropdown.observe(display_table, names="value")
    display(dropdown)
    display(rows_output)
    display(message_output)

    # Function to collect and store user inputs
    def submit_values(_):
        updated_values = {}

        for key, widget in value_widgets.items():
            variable = widget.children[0].value
            if key.startswith("req_"):
                updated_values[variable] = {
                    "Value": widget.children[1].value,
                    "Units": widget.children[2].value,
                }
            else:
                updated_values[key] = {
                    "Value": widget.children[1].value,
                    "Units": widget.children[2].value,
                }

        result["values"] = updated_values

        # Display confirmation message
        with message_output:
            message_output.clear_output()

    # Function to add a new requirement row
    def add_req(_):

        unique_key = (
            f"req_{len([k for k in value_widgets if k.startswith('req_')]) + 1}"
        )

        # Create a dropdown for variable selection with dynamic width
        variable_dropdown = widgets.Dropdown(
            options=variable_names,
            description="Variable:",
            style={"description_width": "initial"},
            layout=widgets.Layout(width=2 * name_label_width[0]),
        )
        value_text = widgets.FloatText(
            placeholder="Value",
            layout=widgets.Layout(width="150px"),
        )

        units_text = widgets.Text(
            placeholder="Units", layout=widgets.Layout(width="150px")
        )

        new_row = widgets.HBox(
            [variable_dropdown, value_text, units_text]
        )

        rows_output.children += (new_row,)
        value_widgets[unique_key] = new_row

    submit_button = widgets.Button(description="Submit")
    submit_button.on_click(submit_values)

    add_req_button = widgets.Button(description="Add Requirement")
    add_req_button.on_click(add_req)

    buttons_box = widgets.HBox([submit_button, add_req_button])
    display(buttons_box)

    return result


def display_formatted_answers(equations_dict):
    """
    Display LaTeX formatted equations and numerical results from a nested 
    dictionary structure in Jupyter Notebook.

    Parameters:
    equations_dict (dict): The dictionary containing the equations.
    """
    results = equations_dict.get('results', {})
    print("We identified the following equations that are relevant to your requirements:")

    for key, value in results.items():
        latex_equation = value.get('latex_equation')
        lhs = value.get('lhs')
        rhs = value.get('rhs')
        match = value.get('match')
        if latex_equation:
            display(Math(latex_equation))
            print(f"For provided values:\nleft hand side = {lhs}\nright hand side = {rhs}")
            if match:
                print("Provided requirements fulfill this mathematical relation")
        else:
            print(f"No LaTeX equation found for {key}")


def display_results(equations_dict):

    results = equations_dict.get('results', {})
    not_match_counter = 0

    for key, value in results.items():
        match = value.get('match')
        latex_equation = value.get('latex_equation')
        lhs = value.get('lhs')
        rhs = value.get('rhs')
        if not match:
            not_match_counter += 1
            display(HTML(
                '<p style="color:red; '
                'font-weight:bold; '
                'font-family:\'Times New Roman\'; '
                'font-size:16px;">'
                'Provided requirements DO NOT fulfill the following mathematical relation:'
                '</p>'
                ))           
            display(Math(latex_equation))
            print(f"For provided values:\nleft hand side = {lhs}\nright hand side = {rhs}")
    if not_match_counter == 0:
        display(HTML(
            '<p style="color:green; '
            'font-weight:bold; '
            'font-family:\'Times New Roman\'; '
            'font-size:16px;">'
            'Requirements you provided do not cause any conflicts'
            '</p>'
        ))


def _get_latex_string_format(input_string):
    """
    Properly formats LaTeX strings for matplotlib when text.usetex is False.
    No escaping needed since mathtext handles backslashes properly.
    """
    return f"${input_string}$"  # No backslash escaping required


def _get_requirements_set(requirements):
    variable_set = set()
    for req in requirements:
        variable_set.add(req['latex_symbol'])

    return variable_set


def _find_vars_in_eq(equation, variable_set):
    patterns = [re.escape(var) for var in variable_set]
    combined_pattern = r'|'.join(patterns)
    matches = re.findall(combined_pattern, equation)
    return {fr"${match}$" for match in matches}


def _add_used_vars_to_results(api_results, api_requirements):
    requirements = _get_requirements_set(api_requirements)

    for key, value in api_results['results'].items():
        latex_equation = value.get('latex_equation')
        # print(latex_equation)
        if latex_equation:
            used_vars = _find_vars_in_eq(latex_equation, requirements)
            api_results['results'][key]['used_vars'] = used_vars

    return api_results


def get_eq_hypergraph(api_results, api_requirements):
    # Disable external LaTeX rendering, using matplotlib's mathtext instead
    plt.rcParams['text.usetex'] = False
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'serif'

    api_results = _add_used_vars_to_results(api_results, api_requirements)

    # Prepare the data for HyperNetX visualization
    hyperedges = {}
    for eq, details in api_results["results"].items():
        hyperedges[_get_latex_string_format(
            details["latex_equation"])] = details["used_vars"]

    # Create the hypergraph using HyperNetX
    H = hnx.Hypergraph(hyperedges)

    # Plot the hypergraph with enhanced clarity
    plt.figure(figsize=(16, 12))

    # Draw the hypergraph with node and edge labels
    hnx.draw(
        H, 
        with_edge_labels=True, 
        edge_labels_on_edge=False,
        node_labels_kwargs={'fontsize': 14}, 
        edge_labels_kwargs={'fontsize': 14},
        layout_kwargs={'seed': 42, 'scale': 2.5}  
    )

    node_labels = list(H.nodes)
    symbol_explanations = _get_node_names_for_node_lables(node_labels, api_requirements)

    # Adding the symbol explanations as a legend
    explanation_text = "\n".join([f"${symbol}$: {desc}" for symbol, desc in symbol_explanations])
    plt.annotate(
        explanation_text, 
        xy=(1.05, 0.5), 
        xycoords='axes fraction', 
        fontsize=14, 
        verticalalignment='center'
    )

    plt.title(r"Enhanced Hypergraph of Equations and Variables", fontsize=20)
    plt.show()


def _get_node_names_for_node_lables(node_labels, api_requirements):

    # Create the output list
    node_names = []

    # Iterate through each symbol in S
    for symbol in node_labels:
        # Search for the matching requirement
        symbol = symbol.replace("$", "")
        for req in api_requirements:
            if req['latex_symbol'] == symbol:
                # Add the matching tuple to SS
                node_names.append((req["latex_symbol"], req["requirement_name"]))
                break  # Stop searching once a match is found

    return node_names
