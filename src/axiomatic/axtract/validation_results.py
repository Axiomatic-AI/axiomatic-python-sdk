from IPython.display import display, Math, HTML  # type: ignore
import hypernetx as hnx  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import re


def display_full_results(validation_results, requirements=None, show_hypergraph=True):
    """Display equation validation results optimized for dark theme notebooks."""
    validations = validation_results.get("validations", {})

    matching = []
    non_matching = []

    for eq_name, value in validations.items():
        equation_data = {
            "name": eq_name,
            "latex": value.get("original_format", ""),
            "lhs": value.get("lhs_value"),
            "rhs": value.get("rhs_value"),
            "diff": abs(value.get("lhs_value", 0) - value.get("rhs_value", 0)),
            "percent_diff": abs(value.get("lhs_value", 0) - value.get("rhs_value", 0))
            / max(abs(value.get("rhs_value", 0)), 1e-10)
            * 100,
            "used_values": value.get("used_values", {}),
        }
        if value.get("is_valid"):
            matching.append(equation_data)
        else:
            non_matching.append(equation_data)

    # Summary header with dark theme
    total = len(validations)
    display(
        HTML(
            '<div style="background-color:#1e1e1e; padding:20px; border-radius:10px; margin:20px 0; '
            'border:1px solid #3e3e3e;">'
            f'<h2 style="font-family:Arial; color:#e0e0e0; margin-bottom:15px">Equation Validation Analysis</h2>'
            f'<p style="font-family:Arial; font-size:16px; color:#e0e0e0">'
            f"<b>Total equations analyzed:</b> {total}<br>"
            f'<span style="color:#4caf50">✅ Matching equations: {len(matching)}</span><br>'
            f'<span style="color:#ff5252">❌ Non-matching equations: {len(non_matching)}</span></p>'
            "</div>"
        )
    )

    # Non-matching equations
    if non_matching:
        display(
            HTML(
                '<div style="background-color:#2d1f1f; padding:20px; border-radius:10px; margin:20px 0; '
                'border:1px solid #4a2f2f;">'
                '<h3 style="color:#ff5252; font-family:Arial">⚠️ Equations Not Satisfied</h3>'
            )
        )

        for eq in non_matching:
            display(HTML(f'<h4 style="color:#e0e0e0; font-family:Arial">{eq["name"]}</h4>'))
            display(Math(eq["latex"]))
            display(
                HTML(
                    '<div style="font-family:monospace; margin-left:20px; margin-bottom:20px; '
                    "background-color:#2a2a2a; color:#e0e0e0; padding:15px; border-radius:5px; "
                    'border-left:4px solid #ff5252">'
                    f"Left side  = {eq['lhs']:.6g}<br>"
                    f"Right side = {eq['rhs']:.6g}<br>"
                    f"Absolute difference = {eq['diff']:.6g}<br>"
                    f"Relative difference = {eq['percent_diff']:.2f}%<br>"
                    "<br>Used values:<br>"
                    + "<br>".join([f"{k} = {v:.6g}" for k, v in eq["used_values"].items()])
                    + "</div>"
                )
            )

        display(HTML("</div>"))

    # Matching equations
    if matching:
        display(
            HTML(
                '<div style="background-color:#1f2d1f; padding:20px; border-radius:10px; margin:20px 0; '
                'border:1px solid #2f4a2f;">'
                '<h3 style="color:#4caf50; font-family:Arial">✅ Satisfied Equations</h3>'
            )
        )

        for eq in matching:
            display(HTML(f'<h4 style="color:#e0e0e0; font-family:Arial">{eq["name"]}</h4>'))
            display(Math(eq["latex"]))
            display(
                HTML(
                    '<div style="font-family:monospace; margin-left:20px; margin-bottom:20px; '
                    "background-color:#2a2a2a; color:#e0e0e0; padding:15px; border-radius:5px; "
                    'border-left:4px solid #4caf50">'
                    f"Value = {eq['lhs']:.6g}<br>"
                    "<br>Used values:<br>"
                    + "<br>".join([f"{k} = {v:.6g}" for k, v in eq["used_values"].items()])
                    + "</div>"
                )
            )

        display(HTML("</div>"))

    # Hypergraph visualization
    if show_hypergraph and requirements:
        display(
            HTML(
                '<div style="background-color:#1e1e1e; padding:20px; border-radius:10px; margin:20px 0; '
                'border:1px solid #3e3e3e;">'
                '<h3 style="color:#e0e0e0; font-family:Arial">🔍 Equation Relationship Analysis</h3>'
                '<p style="font-family:Arial; color:#e0e0e0">The following graph shows how variables are connected through equations:</p>'
                "</div>"
            )
        )

        list_api_requirements = requirements

        # Match get_eq_hypergraph settings exactly
        plt.rcParams["text.usetex"] = False
        plt.rcParams["mathtext.fontset"] = "stix"
        plt.rcParams["font.family"] = "serif"

        # Prepare hypergraph data
        hyperedges = {}
        for eq_name, details in validations.items():
            # Create a set of variables used in this equation
            used_vars = {f"${var}$" for var in details["used_values"].keys()}
            hyperedges[_get_latex_string_format(details["original_format"])] = used_vars

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
        symbol_explanations = _get_node_names_for_node_lables(node_labels, list_api_requirements)

        explanation_text = "\n".join([f"${symbol}$: {desc}" for symbol, desc in symbol_explanations])
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


def _get_node_names_for_node_lables(node_labels, api_requirements):
    """
    Creates mapping between symbols and their descriptions.

    Args:
        node_labels: List of node labels (symbols) from the hypergraph
        api_requirements: Can be either:
            - List of dicts with {"latex_symbol": str, "requirement_name": str}
            - Dictionary mapping variable names to their descriptions
    """
    node_names = []

    # Handle case where api_requirements is a dictionary
    if isinstance(api_requirements, dict):
        for symbol in node_labels:
            clean_symbol = symbol.replace("$", "")
            if clean_symbol in api_requirements:
                node_names.append((clean_symbol, api_requirements[clean_symbol]))
        return node_names

    # Handle case where api_requirements is a list of dicts
    for symbol in node_labels:
        clean_symbol = symbol.replace("$", "")
        for req in api_requirements:
            if isinstance(req, dict) and req.get("latex_symbol") == clean_symbol:
                node_names.append((req["latex_symbol"], req["requirement_name"]))
                break

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
