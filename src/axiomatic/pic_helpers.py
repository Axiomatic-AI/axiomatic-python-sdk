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
    spectra: Union[List[List[List[float]]], Dict[Tuple[str, str], List[List[float]]]],
    wavelengths: List[float],
    spectrum_labels: Optional[List[str]] = None,
    vlines: Optional[List[float]] = None,
    hlines: Optional[List[float]] = None,
):
    """ "
    Creates an interactive plot of spectra with a slider to select different indices.
    Parameters:
    -----------
    spectra : list of list of float
        A list of spectra, where each spectrum is a list of lists of float values, each
        corresponding to the transmission of a single wavelength.
    wavelengths : list of float
        A list of wavelength values corresponding to the x-axis of the plot.
    vlines : list of float, optional
        A list of x-values where vertical lines should be drawn. Defaults to an empty list.
    hlines : list of float, optional
        A list of y-values where horizontal lines should be drawn. Defaults to an empty list.
    """

    # Defaults
    if spectrum_labels is None and isinstance(spectra, dict):
        spectrum_labels = [f"T {port_in} -> {port_out}" for port_in, port_out in spectra.keys()]
    elif spectrum_labels is None:
        spectrum_labels = [f"Spectrum {i}" for i in range(len(spectra))]
    if vlines is None:
        vlines = []
    if hlines is None:
        hlines = []

    if isinstance(spectra, dict):
        spectra = list(spectra.values())

    # Adjust y-axis range
    all_vals = [val for spec in spectra for iteration in spec for val in iteration]
    y_min = min(all_vals)
    y_max = max(all_vals)
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

    # Create frames for each index
    slider_index = list(range(len(spectra[0])))
    fig = go.Figure()

    # Build initial figure for immediate display
    init_idx = slider_index[0]
    for i, spec in enumerate(spectra):
        fig.add_trace(go.Scatter(x=wavelengths, y=spec[init_idx], mode="lines", name=spectrum_labels[i]))
    # Build frames for animation
    frames = []
    for idx in slider_index:
        frame_data = []
        for i, spec in enumerate(spectra):
            frame_data.append(go.Scatter(x=wavelengths, y=spec[idx], mode="lines", name=spectrum_labels[i]))
        frames.append(
            go.Frame(
                data=frame_data,
                name=str(idx),
            )
        )

    fig.frames = frames

    #  Create transition steps
    steps = []
    for idx in slider_index:
        steps.append(
            dict(
                method="animate",
                args=[
                    [str(idx)],
                    {"mode": "immediate", "frame": {"duration": 0, "redraw": True}, "transition": {"duration": 0}},
                ],
                label=str(idx),
            )
        )

    # Create the slider
    sliders = [dict(active=0, currentvalue={"prefix": "Index: "}, pad={"t": 50}, steps=steps)]

    # Create the layout
    fig.update_layout(
        xaxis_title="Wavelength",
        yaxis_title="Transmission",
        shapes=shapes,
        sliders=sliders,
        yaxis=dict(range=[y_min, y_max]),
    )

    fig.show()


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
        None: This function displays the plots and does not return any value.
    """

    for param in parameters:
        plt.figure(figsize=(10, 5))
        plt.title(f"Parameter {param.path} vs. Iterations")
        plt.xlabel("Iterations")
        plt.ylabel(param.path)
        split_param = param.path.split(",")
        if "," in param.path:
            split_param = param.path.split(",")
            plt.plot([parameter_history[i][split_param[0]][split_param[1]] for i in range(len(parameter_history))])
        else:
            plt.plot([parameter_history[i][param.path] for i in range(len(parameter_history))])
        plt.show()


def print_statements(
    statements: StatementDictionary,
    validation: Optional[StatementValidationDictionary] = None,
    only_formalized: bool = False,
):
    """
    Print a list of statements in nice readable format.
    """

    validation = StatementValidationDictionary(
        cost_functions=(validation.cost_functions if validation is not None else None)
        or [StatementValidation()] * len(statements.cost_functions or []),
        parameter_constraints=(validation.parameter_constraints if validation is not None else None)
        or [StatementValidation()] * len(statements.parameter_constraints or []),
        structure_constraints=(validation.structure_constraints if validation is not None else None)
        or [StatementValidation()] * len(statements.structure_constraints or []),
        unformalizable_statements=(validation.unformalizable_statements if validation is not None else None)
        or [StatementValidation()] * len(statements.unformalizable_statements or []),
    )

    if len(validation.cost_functions or []) != len(statements.cost_functions or []):
        raise ValueError("Number of cost functions and validations do not match.")
    if len(validation.parameter_constraints or []) != len(statements.parameter_constraints or []):
        raise ValueError("Number of parameter constraints and validations do not match.")
    if len(validation.structure_constraints or []) != len(statements.structure_constraints or []):
        raise ValueError("Number of structure constraints and validations do not match.")
    if len(validation.unformalizable_statements or []) != len(statements.unformalizable_statements or []):
        raise ValueError("Number of unformalizable statements and validations do not match.")

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
        val = cost_stmt.validation or cost_val
        if val.satisfiable is not None and val.message is not None:
            print(f"Satisfiable: {val.satisfiable}")
            print(val.message)
        print("\n-----------------------------------\n")
    for param_stmt, param_val in zip(statements.parameter_constraints or [], validation.parameter_constraints or []):
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
        val = param_stmt.validation or param_val
        if val.satisfiable is not None and val.message is not None and val.holds is not None:
            print(f"Satisfiable: {val.satisfiable}")
            print(f"Holds: {val.holds} ({val.message})")
        print("\n-----------------------------------\n")
    for struct_stmt, struct_val in zip(statements.structure_constraints or [], validation.structure_constraints or []):
        if struct_stmt.formalization is None and only_formalized:
            continue
        print("Type:", struct_stmt.type)
        print("Statement:", struct_stmt.text)
        print("Formalization:", end=" ")
        if struct_stmt.formalization is None:
            print("UNFORMALIZED")
        else:
            func_constr = struct_stmt.formalization
            args_str = ", ".join(
                [
                    f"{argname}=" + (f"'{argvalue}'" if isinstance(argvalue, str) else str(argvalue))
                    for argname, argvalue in func_constr.arguments.items()
                ]
            )
            func_str = f"{func_constr.function_name}({args_str}) == {func_constr.expected_result}"
            print(func_str)
        val = struct_stmt.validation or struct_val
        if val.satisfiable is not None and val.holds is not None:
            print(f"Satisfiable: {val.satisfiable}")
            print(f"Holds: {val.holds}")
        print("\n-----------------------------------\n")
    if not only_formalized:
        for unf_stmt in statements.unformalizable_statements or []:
            print("Type:", unf_stmt.type)
            print("Statement:", unf_stmt.text)
            print("Formalization: UNFORMALIZABLE")
            print("\n-----------------------------------\n")


def _str_units_to_float(str_units: str) -> float:
    unit_conversions = {
        "nm": 1e-3,
        "um": 1,
        "mm": 1e3,
        "m": 1e6,
    }
    match = re.match(r"([\d\.]+)\s*([a-zA-Z]+)", str_units)
    numeric_value = float(match.group(1) if match else 1.55)
    unit = match.group(2) if match else "um"
    return float(numeric_value * unit_conversions[unit])


def get_wavelengths_to_plot(statements: StatementDictionary, num_samples: int = 100) -> Tuple[List[float], List[float]]:
    """
    Get the wavelengths to plot based on the statements.

    Returns a list of wavelengths to plot the spectra and a list of vertical lines to plot on top the spectra.
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
                    if isinstance(wl, str)
                }
            if "wavelength_range" in comp.arguments:
                if (
                    isinstance(comp.arguments["wavelength_range"], list)
                    and len(comp.arguments["wavelength_range"]) == 2
                    and all(isinstance(wl, str) for wl in comp.arguments["wavelength_range"])
                ):
                    min_wl = min(min_wl, _str_units_to_float(comp.arguments["wavelength_range"][0]))
                    max_wl = max(max_wl, _str_units_to_float(comp.arguments["wavelength_range"][1]))
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
        avg_wl = sum(vlines) / len(vlines) if vlines else 1550
        min_wl, max_wl = avg_wl - 0.1, avg_wl + 0.1
    else:
        range_size = max_wl - min_wl
        min_wl -= 0.2 * range_size
        max_wl += 0.2 * range_size

    wls = np.linspace(min_wl, max_wl, num_samples)
    return [float(wl) for wl in wls], list(vlines)
