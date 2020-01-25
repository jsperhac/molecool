"""
functions.py
example project for molssi best practices workshop

Handles the primary functions
"""

#import os
#import numpy as np
#import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination! (I didn't think HDT wrote code)"
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau, by JMS"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
