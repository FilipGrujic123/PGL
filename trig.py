from math import *

def get_angle_tan(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    rads = atan2(-dy,dx)
    rads %= 2*pi
    return degrees(rads)