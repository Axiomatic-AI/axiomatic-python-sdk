import re
from typing import Dict, List, Optional, Set, Tuple, Union

import iklayout  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import plotly.graph_objects as go  # type: ignore

from . import Computation, Parameter, StatementDictionary, StatementValidation, StatementValidationDictionary


def plot_circuit(component):
    """
    Show the interactive component layout with iKlayout.
    See: https://pypi.org/project/iklayout/

    In order to make this interactive, ensure that you have enabled
    interactive widgets. This can be done with %matplotlib widget in
    Jupyter notebooks.

    Args:
        component: GDS factory Component object.
            See https://gdsfactory.github.io/gdsfactory/_autosummary/gdsfactory.Component.html
    """
    path = component.write_gds().absolute()

    return iklayout.show(path)


def plot_losses(losses: List[float], iterations: Optional[List[int]] = None):
    """
    Plot a list of losses with labels.

    Args:
        losses: List of loss values.
    """
    iterations = iterations or list(range(len(losses)))
    plt.clf()
    plt.figure(figsize=(10, 5))
    plt.title("Losses vs. Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Losses")
    plt.plot(iterations, losses)
    return plt.gcf()


def plot_constraints(
    constraints: List[List[float]],
    constraints_labels: Optional[List[str]] = None,
    iterations: Optional[List[int]] = None,
):
    """
    Plot a list of constraints with labels.

    Args:
        constraints: List of constraint values.
        labels: List of labels for each constraint value.
    """

    constraints_labels = constraints_labels or [f"Constraint {i}" for i in range(len(constraints[0]))]
    iterations = iterations or list(range(len(constraints[0])))

    plt.clf()
    plt.figure(figsize=(10, 5))
    plt.title("Losses vs. Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Constraints")
    for i, constraint in enumerate(constraints):
        plt.plot(iterations, constraint, label=constraints_labels[i])
    plt.legend()
    plt.grid(True)
    return plt.gcf()


def plot_single_spectrum(
    spectrum: List[float],
    wavelengths: List[float],
    vlines: Optional[List[float]] = None,
    hlines: Optional[List[float]] = None,
):
    """
    Plot a single spectrum with vertical and horizontal lines.
    """
    hlines = hlines or []
    vlines = vlines or []

    plt.clf()
    plt.figure(figsize=(10, 5))
    plt.title("Losses vs. Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Losses")
    plt.plot(wavelengths, spectrum)
    for x_val in vlines:
        plt.axvline(x=x_val, color="red", linestyle="--", label=f"Wavelength (x={x_val})")  # Add vertical line
    for y_val in hlines:
        plt.axhline(y=y_val, color="red", linestyle="--", label=f"Transmission (y={y_val})")  # Add vertical line
    return plt.gcf()


def plot_interactive_spectra(
    spectra: Union[List[List[List[float]]], Dict[Union[Tuple[str, str], str], List[List[float]]]],
    wavelengths: List[float],
    spectrum_labels: Optional[List[str]] = None,
    vlines: Optional[List[float]] = None,
    hlines: Optional[List[float]] = None,
):
    """ "
    Creates an interactive plot of spectra with a slider to select different indices.
    Parameters:
    -----------
    spectra : list of list of float or a dictionary with tuple or string keys
        A list of spectra, where each spectrum is a list of lists of float values, each
        corresponding to the transmission of a single wavelength.
    wavelengths : list of float
        A list of wavelength values corresponding to the x-axis of the plot, in um.
    vlines : list of float, optional
        A list of x-values where vertical lines should be drawn, in um. Defaults to an empty list.
    hlines : list of float, optional
        A list of y-values where horizontal lines should be drawn. Defaults to an empty list.
    """

    hlines = hlines or []
    
    # Convert wavelengths to nm
    wavelengths = [wl*1e3 for wl in wavelengths]
    vlines = [wl*1e3 for wl in vlines] if vlines else []

    if isinstance(spectra, dict):
        port_keys = []
        for key in spectra:
            if isinstance(key, str):
                ports = key.split(",")
                if len(ports) != 2:
                    raise ValueError("Port keys must be in the format 'port_in,port_out' with exactly one comma.")
                port_keys.append((key.split(",")[0], key.split(",")[1]))
            elif isinstance(key, tuple):
                port_keys.append(key)
            else:
                raise ValueError("Port keys must be either a string or a tuple.")

    # Defaults
    if spectrum_labels is None and isinstance(spectra, dict):
        spectrum_labels = [f"T {port_in} -> {port_out}" for port_in, port_out in port_keys]

    elif spectrum_labels is None:
        spectrum_labels = [f"Spectrum {i}" for i in range(len(spectra))]

    if isinstance(spectra, dict):
        spectra = list(spectra.values())

    # Adjust y-axis range
    all_vals = [val for spec in spectra for iteration in spec for val in iteration]
    y_min = min(all_vals)
    y_max = max(all_vals)

    # dB scale
    if y_max <= 0:
        y_max = 0
        db = True
    else:
        db = False
        if hlines:
            y_min = min(hlines + [y_min]) * 0.95
            y_max = max(hlines + [y_max]) * 1.05

    # Create hlines and vlines
    shapes = []
    for xv in vlines:
        shapes.append(
            dict(type="line", xref="x", x0=xv, x1=xv, yref="paper", y0=0, y1=1, line=dict(color="red", dash="dash"))
        )
    for yh in hlines:
        shapes.append(
            dict(type="line", xref="paper", x0=0, x1=1, yref="y", y0=yh, y1=yh, line=dict(color="red", dash="dash"))
        )

    # Create initial figure
    fig = go.Figure()

    # Build initial figure for immediate display
    init_idx = 0
    for i, spec in enumerate(spectra):
        fig.add_trace(go.Scatter(x=wavelengths, y=spec[init_idx], mode="lines", name=spectrum_labels[i]))

    # Create transition steps
    steps = []
    for idx in range(len(spectra[0])):
        step = dict(
            method="restyle",
            args=["y", [spec[idx] for spec in spectra]],
            label=str(idx),
        )
        steps.append(step)

    # Create the slider
    sliders = [dict(active=0, currentvalue={"prefix": "Index: "}, pad={"t": 50}, steps=steps)]

    # Create the layout
    fig.update_layout(
        xaxis_title="Wavelength (nm)",
        yaxis_title="Transmission " + ("(dB)" if db else "(linear)"),
        shapes=shapes,
        sliders=sliders,
        yaxis=dict(range=[y_min, y_max]),
    )

    return fig


def plot_parameter_history(parameters: List[Parameter], parameter_history: List[dict]):
    """
    Plots the history of specified parameters over iterations.
    Args:
        parameters (list): A list of parameter objects, each having a 'path' attribute.
        parameter_history (list): A list of dictionaries containing parameter values
                                  for each iteration. Each dictionary should be
                                  structured such that the keys correspond to the
                                  first part of the parameter path, and the values
                                  are dictionaries where keys correspond to the
                                  second part of the parameter path.
    Returns:
        fig: The figure object containing the plots.
    """
    plt.clf()
    
    # Create figure and axes
    fig, axs = plt.subplots(len(parameters), 1, figsize=(10, 5 * len(parameters)), sharex=True)
    fig.suptitle("Parameter History vs. Iterations")
    fig.supxlabel("Iterations")
    fig.supylabel("Parameter Values")
    
    # Handle the case where there's only one parameter (axs becomes a single Axes object instead of a list)
    if len(parameters) == 1:
        axs = [axs]
    
    for i, param in enumerate(parameters):
        if "," in param.path:
            split_param = param.path.split(",")
            axs[i].plot(
                [parameter_history[j][split_param[0]][split_param[1]] for j in range(len(parameter_history))],
                label=param.path
            )
        else:
            axs[i].plot(
                [parameter_history[j][param.path] for j in range(len(parameter_history))],
                label=param.path
            )
        axs[i].legend()
        axs[i].grid(True)
    
    plt.tight_layout(rect=(0, 0, 1, 0.96))
    plt.close(fig)
    return fig


def print_statements(
    statements: StatementDictionary,
    validation: Optional[StatementValidationDictionary] = None,
    only_formalized: bool = False,
    pprint=True,
):
    """
    Print a list of statements in nice readable format.
    pprint enabled HTML rendering in Jupyter notebooks.
    """

    validation = StatementValidationDictionary(
        cost_functions=(validation.cost_functions if validation is not None else None)
        or [StatementValidation()] * len(statements.cost_functions or []),
        parameter_constraints=(validation.parameter_constraints if validation is not None else None)
        or [StatementValidation()] * len(statements.parameter_constraints or []),
        unformalizable_statements=(validation.unformalizable_statements if validation is not None else None)
        or [StatementValidation()] * len(statements.unformalizable_statements or []),
    )

    if len(validation.cost_functions or []) != len(statements.cost_functions or []):
        raise ValueError("Number of cost functions and validations do not match.")
    if len(validation.parameter_constraints or []) != len(statements.parameter_constraints or []):
        raise ValueError("Number of parameter constraints and validations do not match.")
    if len(validation.unformalizable_statements or []) != len(statements.unformalizable_statements or []):
        raise ValueError("Number of unformalizable statements and validations do not match.")

    if pprint:
        # NOTE: the pprint code has been generated by Chattie by conversion from the HTML code below
        html_parts = []

        # Start of HTML document
        html_parts.append("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Validation Report</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; background-color: #f9f9f9; }
            .block { background-color: #fff; border: 1px solid #ddd; padding: 15px; margin-bottom: 20px; border-radius: 5px; }
            .block h2 { margin-top: 0; font-size: 1.2em; color: #333; }
            .block p { margin: 5px 0; color: #555; }
            .holds { background-color: #d4edda; border-color: #c3e6cb; }
            .not-hold { background-color: #f8d7da; border-color: #f5c6cb; }
            .label { font-weight: bold; }
            .block code {
                background-color: #f4f4f4;
                border: 1px solid #ddd;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: Consolas, "Courier New", monospace;
                font-size: 0.9em;
                color: #c7254e;
                background-color: #f9f2f4;
            }
        </style>
        </head>
        <body>
        """)

        # Cost Functions Rendering
        for cost_stmt, cost_val in zip(statements.cost_functions or [], validation.cost_functions or []):
            if (cost_stmt.formalization is None or cost_stmt.formalization.mapping is None) and only_formalized:
                continue

            html_parts.append('<div class="block">')
            html_parts.append(f"<h2>{cost_stmt.type}</h2>")
            html_parts.append(f'<p><span class="label">Statement:</span> {cost_stmt.text}</p>')
            if cost_stmt.formalization is None:
                html_parts.append("UNFORMALIZED")
            else:
                html_parts.append('<p><span class="label">Formalization:</span> ')
                code = cost_stmt.formalization.code
                if cost_stmt.formalization.mapping is not None:
                    for var_name, computation in cost_stmt.formalization.mapping.items():
                        if computation is not None:
                            args_str = ", ".join(
                                f"{argname}=" + (f"'{argvalue}'" if isinstance(argvalue, str) else str(argvalue))
                                for argname, argvalue in computation.arguments.items()
                            )
                            code = code.replace(var_name, f"{computation.name}({args_str})")
                html_parts.append(f"<code>{code}</code>")
                html_parts.append("</p>")
            val = cost_val or cost_stmt.validation
            if val and val.satisfiable is not None and val.message is not None:
                html_parts.append(f'<p><span class="label">Satisfiable:</span> {val.satisfiable}</p>')
                html_parts.append(f'<p><span class="label">Reason:</span> {val.message}</p>')
            html_parts.append("</div>")

        # Parameter Constraints Rendering
        for param_stmt, param_val in zip(
            statements.parameter_constraints or [], validation.parameter_constraints or []
        ):
            if (param_stmt.formalization is None or param_stmt.formalization.mapping is None) and only_formalized:
                continue
            val = param_val or param_stmt.validation
            if val and val.holds is not None:
                holds_tag = "holds" if val.holds else "not-hold"
            else:
                holds_tag = ''
            html_parts.append(f'<div class="block {holds_tag}">')
            html_parts.append(f"<h2>{param_stmt.type}</h2>")
            html_parts.append(f'<p><span class="label">Statement:</span> {param_stmt.text}</p>')
            if param_stmt.formalization is None:
                html_parts.append("UNFORMALIZED")
            else:
                html_parts.append('<p><span class="label">Formalization:</span> ')
                code = param_stmt.formalization.code
                if param_stmt.formalization.mapping is not None:
                    for var_name, computation in param_stmt.formalization.mapping.items():
                        if computation is not None:
                            args_str = ", ".join(
                                f"{argname}=" + (f"'{argvalue}'" if isinstance(argvalue, str) else str(argvalue))
                                for argname, argvalue in computation.arguments.items()
                            )
                            code = code.replace(var_name, f"{computation.name}({args_str})")
                html_parts.append(f"<code>{code}</code>")
                html_parts.append("</p>")
            if val and val.satisfiable is not None and val.message is not None and val.holds is not None:
                html_parts.append(f'<p><span class="label">Satisfiable:</span> {val.satisfiable}</p>')
                html_parts.append(f'<p><span class="label">Holds:</span> {val.holds}</p>')
                html_parts.append(f'<p><span class="label">Reason:</span> {val.message}</p>')
            html_parts.append("</div>")

        # Unformalizable Statements Rendering (if applicable)
        if not only_formalized:
            for unf_stmt in statements.unformalizable_statements or []:
                html_parts.append('<div class="block not-hold">')
                html_parts.append(f"<h2>{unf_stmt.type}</h2>")
                html_parts.append(f'<p><span class="label">Statement:</span> {unf_stmt.text}</p>')
                # html_parts.append('<p><span class="label">Formalization:</span> UNFORMALIZABLE</p>')
                html_parts.append("</div>")

        # End of HTML document
        html_parts.append("""</body></html>""")

        # Combine all parts into the final HTML string
        final_html = "\n".join(html_parts)

        # Display the HTML string
        from IPython.display import display, HTML  # type: ignore

        display(HTML(final_html))
    else:
        print("-----------------------------------\n")
        for cost_stmt, cost_val in zip(statements.cost_functions or [], validation.cost_functions or []):
            if (cost_stmt.formalization is None or cost_stmt.formalization.mapping is None) and only_formalized:
                continue
            print("Type:", cost_stmt.type)
            print("Statement:", cost_stmt.text)
            print("Formalization:", end=" ")
            if cost_stmt.formalization is None:
                print("UNFORMALIZED")
            else:
                code = cost_stmt.formalization.code
                if cost_stmt.formalization.mapping is not None:
                    for var_name, computation in cost_stmt.formalization.mapping.items():
                        if computation is not None:
                            args_str = ", ".join(
                                [
                                    f"{argname}=" + (f"'{argvalue}'" if isinstance(argvalue, str) else str(argvalue))
                                    for argname, argvalue in computation.arguments.items()
                                ]
                            )
                            code = code.replace(var_name, f"{computation.name}({args_str})")
                print(code)
            val = cost_val or cost_stmt.validation
            if val and val.satisfiable is not None and val.message is not None:
                print(f"Satisfiable: {val.satisfiable}")
                print(val.message)
            print("\n-----------------------------------\n")
        for param_stmt, param_val in zip(
            statements.parameter_constraints or [], validation.parameter_constraints or []
        ):
            if (param_stmt.formalization is None or param_stmt.formalization.mapping is None) and only_formalized:
                continue
            print("Type:", param_stmt.type)
            print("Statement:", param_stmt.text)
            print("Formalization:", end=" ")
            if param_stmt.formalization is None:
                print("UNFORMALIZED")
            else:
                code = param_stmt.formalization.code
                if param_stmt.formalization.mapping is not None:
                    for var_name, computation in param_stmt.formalization.mapping.items():
                        if computation is not None:
                            args_str = ", ".join(
                                [
                                    f"{argname}=" + (f"'{argvalue}'" if isinstance(argvalue, str) else str(argvalue))
                                    for argname, argvalue in computation.arguments.items()
                                ]
                            )
                            code = code.replace(var_name, f"{computation.name}({args_str})")
                print(code)
            val = param_val or param_stmt.validation
            if val and val.satisfiable is not None and val.message is not None and val.holds is not None:
                print(f"Satisfiable: {val.satisfiable}")
                print(f"Holds: {val.holds} ({val.message})")
            print("\n-----------------------------------\n")
        if not only_formalized:
            for unf_stmt in statements.unformalizable_statements or []:
                print("Type:", unf_stmt.type)
                print("Statement:", unf_stmt.text)
                print("Formalization: UNFORMALIZABLE")
                print("\n-----------------------------------\n")


def _str_units_to_float(str_units: str) -> Optional[float]:
    """Returns the numeric value of a string with units in micrometers, e.g. '1550 nm' -> 1.55"""
    """Return None if the string is not a valid unit."""
    unit_conversions = {
        "nm": 1e-3,
        "um": 1,
        "mm": 1e3,
        "m": 1e6,
    }
    match = re.match(r"([\d\.]+)\s*([a-zA-Z]+)", str_units)
    numeric_value = float(match.group(1)) if match else None
    unit = match.group(2) if match else None
    return float(numeric_value * unit_conversions[unit]) if unit in unit_conversions and numeric_value is not None else None


def get_wavelengths_to_plot(statements: StatementDictionary, num_samples: int = 1000) -> Tuple[List[float], List[float]]:
    """
    Get the wavelengths to plot based on the statements.

    Returns a list of wavelengths to plot the spectra and a list of vertical lines to plot on top the spectra, in um.
    """

    min_wl = float("inf")
    max_wl = float("-inf")
    vlines: set = set()

    def update_wavelengths(mapping: Dict[str, Optional[Computation]], min_wl: float, max_wl: float, vlines: Set):
        for comp in mapping.values():
            if comp is None:
                continue
            if "wavelengths" in comp.arguments:
                vlines = vlines | {
                    _str_units_to_float(wl)
                    for wl in (comp.arguments["wavelengths"] if isinstance(comp.arguments["wavelengths"], list) else [])
                    if isinstance(wl, str) and _str_units_to_float(wl) is not None
                }
            if "wavelength_range" in comp.arguments:
                if (
                    isinstance(comp.arguments["wavelength_range"], list)
                    and len(comp.arguments["wavelength_range"]) == 2
                    and all(isinstance(wl, str) for wl in comp.arguments["wavelength_range"])
                ):
                    mi = _str_units_to_float(comp.arguments["wavelength_range"][0])
                    ma = _str_units_to_float(comp.arguments["wavelength_range"][1])
                    if mi is not None and ma is not None:
                        min_wl = min(min_wl, mi)
                        max_wl = max(max_wl, ma)
        return min_wl, max_wl, vlines

    for cost_stmt in statements.cost_functions or []:
        if cost_stmt.formalization is not None and cost_stmt.formalization.mapping is not None:
            min_wl, max_wl, vlines = update_wavelengths(cost_stmt.formalization.mapping, min_wl, max_wl, vlines)

    for param_stmt in statements.parameter_constraints or []:
        if param_stmt.formalization is not None and param_stmt.formalization.mapping is not None:
            min_wl, max_wl, vlines = update_wavelengths(param_stmt.formalization.mapping, min_wl, max_wl, vlines)

    if vlines:
        min_wl = min(min_wl, min(vlines))
        max_wl = max(max_wl, max(vlines))
    if min_wl >= max_wl:
        avg_wl = sum(vlines) / len(vlines) if vlines else _str_units_to_float("1550 nm")
        min_wl, max_wl = avg_wl - _str_units_to_float("10 nm"), avg_wl + _str_units_to_float("10 nm")
    else:
        range_size = max_wl - min_wl
        min_wl -= 0.2 * range_size
        max_wl += 0.2 * range_size

    wls = np.linspace(min_wl, max_wl, num_samples)
    return [float(wl) for wl in wls], list(vlines)
