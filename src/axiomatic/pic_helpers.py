import iklayout  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from ipywidgets import interactive, IntSlider  # type: ignore
from typing import List, Optional

from . import Parameter


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

    constraints_labels = constraints_labels or [
        f"Constraint {i}" for i in range(len(constraints[0]))
    ]
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
        plt.axvline(
            x=x_val, color="red", linestyle="--", label=f"Wavelength (x={x_val})"
        )  # Add vertical line
    for y_val in hlines:
        plt.axhline(
            x=y_val, color="red", linestyle="--", label=f"Transmission (y={y_val})"
        )  # Add vertical line
    return plt.gcf()


def plot_interactive_spectra(
    spectra: List[List[List[float]]],
    wavelengths: List[float],
    spectrum_labels: Optional[List[str]] = None,
    slider_index: Optional[List[int]] = None,
    vlines: Optional[List[float]] = None,
    hlines: Optional[List[float]] = None,
):
    """
    Creates an interactive plot of spectra with a slider to select different indices.
    Parameters:
    -----------
    spectra : list of list of float
        A list of spectra, where each spectrum is a list of lists of float values, each
        corresponding to the transmission of a single wavelength.
    wavelengths : list of float
        A list of wavelength values corresponding to the x-axis of the plot.
    slider_index : list of int, optional
        A list of indices for the slider. Defaults to range(len(spectra[0])).
    vlines : list of float, optional
        A list of x-values where vertical lines should be drawn. Defaults to an empty list.
    hlines : list of float, optional
        A list of y-values where horizontal lines should be drawn. Defaults to an empty list.
    Returns:
    --------
    ipywidgets.widgets.interaction.interactive
        An interactive widget that allows the user to select different indices using a slider.
    Notes:
    ------
    - The function uses matplotlib for plotting and ipywidgets for creating the interactive
    slider.
    - The y-axis limits are fixed based on the global minimum and maximum values across all
    spectra.
    - Vertical and horizontal lines can be added to the plot using the `vlines` and `hlines`
    parameters.
    """
    # Calculate global y-limits across all arrays
    y_min = min(min(min(arr2) for arr2 in arr1) for arr1 in spectra)
    y_max = max(max(max(arr2) for arr2 in arr1) for arr1 in spectra)

    slider_index = slider_index or list(range(len(spectra[0])))
    spectrum_labels = spectrum_labels or [f"Spectrum {i}" for i in range(len(spectra))]
    vlines = vlines or []
    hlines = hlines or []

    # Function to update the plot
    def plot_array(index=0):
        plt.close("all")
        plt.figure(figsize=(8, 4))
        for i, array in enumerate(spectra):
            plt.plot(wavelengths, array[index], lw=2, label=spectrum_labels[i])
        for x_val in vlines:
            plt.axvline(
                x=x_val, color="red", linestyle="--", label=f"Wavelength (x={x_val})"
            )  # Add vertical line
        for y_val in hlines:
            plt.axhline(
                x=y_val, color="red", linestyle="--", label=f"Transmission (y={y_val})"
            )  # Add vertical line
        plt.title(f"Iteration: {index}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.ylim(y_min, y_max)  # Fix the y-limits
        plt.legend()
        plt.grid(True)
        plt.show()

    slider = IntSlider(
        value=0, min=0, max=len(spectra[0]) - 1, step=1, description="Index"
    )
    return interactive(plot_array, index=slider)


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
        plt.plot(
            [
                parameter_history[i][split_param[0]][split_param[1]]
                for i in range(len(parameter_history))
            ]
        )
        plt.show()
