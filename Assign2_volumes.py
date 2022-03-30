# name: Shenghua He
# student number: 251016121
# project: Assignment 2 - volumes.py
# class: CS1026A 002 SU21
# professor: Duff Jones

# import math so that pi can be used
import math


# define functions, return volume
def volume_of_a_cylinder(r, h):
    volume = math.pi * (r ** 2) * h
    return volume


def volume_of_a_rectangular_prism(l, w, h):
    volume = l * w * h
    return volume


def volume_of_a_sphere(r):
    volume = (4/3) * math.pi * (r ** 3)
    return volume
