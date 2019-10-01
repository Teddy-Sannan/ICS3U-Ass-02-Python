#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: September 16
# This program calculates the surface area of a cone

import math


def main():
    # main function
    print("We will be calculating the surface area of a cone")
    print("")
    # input
    radius = int(input("Enter the radius (cm): "))
    height = int(input("Enter the height (cm): "))
    # process
    surface_area = math.pi*radius*(radius+math.sqrt(height**2+radius**2))
    print("")
    # output
    print("Surface Area is {} cm^2".format(surface_area))


if __name__ == "__main__":
    main()
