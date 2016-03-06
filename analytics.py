import math
import random
from .utils import euclidean_distance
from .utils import generate_random


def find_largest_city(gj):
    """
    Iterate through a geojson feature collection and
    find the largest city.  Assume that the key
    to access the maximum population is 'pop_max'.
    Parameters
    ----------
    gj : dict
         A GeoJSON file read in as a Python dictionary
    Returns
    -------
    city : str
           The largest city
    population : int
                 The population of the largest city
    """

    temp = 0
    city = ""
    max_population = 0
    for i in gj['features']:
       if i['properties']['pop_max'] > temp:
            temp = i['properties']['pop_max']
            city = i['properties']['name']
            max_population = temp

    return city, max_population


def average_nearest_neighbor_distance(points):
    """
    Given a set of points, compute the average nearest neighbor.
    Parameters
    ----------
    points : list
             A list of points in the form (x,y)
    Returns
    -------
    mean_d : float
             Average nearest neighbor distance
    References
    ----------
    Clark and Evan (1954 Distance to Nearest Neighbor as a
     Measure of Spatial Relationships in Populations. Ecology. 35(4)
     p. 445-453.
    """
    sum_nn_dis = 0

    for point_1 in points:
        first = True
        for point_2 in points:
            if point_1 == point_2:
                continue
            else:
                distance = euclidean_distance(point_1, point_2)
                if first:
                    nn_dis = distance
                    first = False
                elif distance < nn_dis:
                    nn_dis = distance

        sum_nn_dis += nn_dis
        mean_distance = sum_nn_dis / len(points)
    return mean_distance

def permutations(p = 99, n = 100):
    permutations = []
    for i in range(p):
        points_list = generate_random(n)
        permutations.append(average_nearest_neighbor_distance(points_list))

    return permutations


def critical_points(permutations):
    """
    Lowest distance and greatest distance of points.
    """
   
    lower = min(permutations)
    upper = max(permutations)
    return lower, upper


def significant_distance(lower, upper, observed):
    if (lower > observed) or (upper < observed):
       result = True
    else:
       result = False
       
    return result
