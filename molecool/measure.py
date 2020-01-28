"""
measure.py
calculation functions for molssi best practices workshop

"""

import numpy as np

def calculate_distance(rA, rB):
    # This function calculates the distance between two points given as numpy arrays.
    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

