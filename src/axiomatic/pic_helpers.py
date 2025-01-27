import iklayout  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from ipywidgets import interactive, IntSlider  # type: ignore
from typing import List

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


def plot_losses(losses: List[float], iterations: List[int] | None = None, return_fig: bool = False):
    """
    Plot a list of losses with labels.

    Args:
        losses: List of loss values.
    """
    iterations = iterations or list(range(len(losses)))
    plt.figure(figsize=(10, 5))
    plt.title("Losses vs. Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Losses")
    plt.plot(iterations, losses)
    if return_fig:
        return plt.gcf()
    plt.show()


def plot_constraints(constraints: List[List[float]], constraints_labels: List[str] | None = None, iterations: List[int] | None = None, return_fig: bool = False):
    """
    Plot a list of constraints with labels.

    Args:
        constraints: List of constraint values.
        labels: List of labels for each constraint value.
    """

    constraints_labels = constraints_labels or [f"Constraint {i}" for i in range(len(constraints[0]))]
    iterations = iterations or list(range(len(constraints[0])))

    plt.figure(figsize=(10, 5))
    plt.title("Losses vs. Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Constraints")
    for i, constraint in enumerate(constraints):
        plt.plot(iterations, constraint, label=constraints_labels[i])
    plt.legend()
    plt.grid(True)
    if return_fig:
        return plt.gcf()
    plt.show()


def plot_single_spectrum(spectrum: List[float],
                         wavelengths: List[float],
                         vlines: List[float] | None = None,
                         hlines: List[float] | None = None):
    """
    Plot a single spectrum with vertical and horizontal lines.
    """
    hlines = hlines or []
    vlines = vlines or []

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
        plt.axvline(
            x=y_val, color="red", linestyle="--", label=f"Transmission (y={y_val})"
        )  # Add vertical line
    plt.show()


def plot_interactive_spectrums(
    spectrums: List[List[List[float]]],
    wavelengths: List[float],
    spectrum_labels: List[str] | None = None,
    slider_index: List[int] | None = None,
    vlines: List[float] | None = None,
    hlines: List[float] | None = None,
):
    """
    Creates an interactive plot of spectrums with a slider to select different indices.
    Parameters:
    -----------
    spectrums : list of list of float
        A list of spectrums, where each spectrum is a list of lists of float values, each
        corresponding to the transmission of a single wavelength.
    wavelengths : list of float
        A list of wavelength values corresponding to the x-axis of the plot.
    slider_index : list of int, optional
        A list of indices for the slider. Defaults to range(len(spectrums[0])).
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
    spectrums.
    - Vertical and horizontal lines can be added to the plot using the `vlines` and `hlines`
    parameters.
    """

    # Calculate global y-limits across all arrays
    y_min = min(min(min(arr2) for arr2 in arr1) for arr1 in spectrums)
    y_max = max(max(max(arr2) for arr2 in arr1) for arr1 in spectrums)

    slider_index = slider_index or list(range(len(spectrums[0])))
    spectrum_labels = spectrum_labels or [f"Spectrum{i}" for i in range(len(spectrums))]
    vlines = vlines or []
    hlines = hlines or []

    # Function to update the plot
    def plot_array(index=0):
        plt.figure(figsize=(8, 4))
        for i, array in enumerate(spectrums):
            plt.plot(wavelengths, array[index], lw=2, label=spectrum_labels[i])
        for x_val in vlines:
            plt.axvline(
                x=x_val, color="red", linestyle="--", label=f"Wavelength (x={x_val})"
            )  # Add vertical line
        for y_val in hlines:
            plt.axvline(
                x=y_val, color="red", linestyle="--", label=f"Transmission (y={y_val})"
            )  # Add vertical line
        plt.title(f"Iteration: {index}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.ylim(y_min, y_max)  # Fix the y-limits
        plt.legend()
        plt.grid(True)
        plt.show()

    slider = IntSlider(value=0, min=0, max=len(spectrums[0]) - 1, step=1, description="Index")
    return interactive(plot_array, index=slider)
