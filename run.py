#!/usr/bin/env python3

"""
A script to screen capture and solve a cube from
https://ruwix.com/online-puzzle-simulators/ using opencv

Works in linux
"""

from mss import mss
import cv2
import numpy as np


def get_colour(image, p):
    """
    Returns a char with the colour of given point
    """
    #  print('\n\n', image[p[0]+3, p[1]+3])

    return ''


def draw_rectangles(image, points):
    """
    Function to draw rectangle based on points given
    """
    state = []

    for p in points:
        state.append(image[p[0], p[1]])
        cv2.rectangle(image, p, (p[0]+3, p[1]+3), (0, 255, 0), 2)

    print(state[0], state[1], state[2])


def read_cube(bounding_box, points):
    """
    Function to read cube's initial state
    """
    screen = np.array(mss().grab(bounding_box))


if __name__ == "__main__":

    break_key = 'q'
    bounding_box = {'top': 350, 'left': 1200, 'width': 450, 'height': 400}
    points = [(95, 170), (140, 190), (185, 210),
              (95, 230), (140, 250), (185, 270),
              (95, 290), (140, 310), (185, 330)]

    #  read_cube(bounding_box)

    while True:
        screen = np.array(mss().grab(bounding_box))

        draw_rectangles(screen, points)

        cv2.imshow('cube', screen)

        k = cv2.waitKey(1) & 0xFF
        if k == ord(break_key):
            break
