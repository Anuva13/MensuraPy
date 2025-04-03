import math

def square(side):
    # Returns the area of a square.
    return side ** 2

def rectangle(length,breadth):
    # Returns the area of a rectangle.
    return length * breadth

def circle(radius):
    # Returns the area of a circle.
    return math.pi * radius ** 2

def triangle_base_height(base, height):
    # Returns the area of a triangle when base and height are given
    return 0.5 * base * height

def triangle_heros_formula(side1, side2, side3):
    # semi-perimeter
    s = (side1 + side2 + side3)/2
    # Returns the area of a triangle when 3 sides are given
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

def equilateral_triangle(side):
    # Returns the area of a triangle when 3 sides are same
    return (math.sqrt(3) / 4) * s ** 2

def triangle_sides_angle(side1, side2, angle_degrees):
    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)
     # Returns the area of a triangle when 2 sides and one angle given
    return 0.5 * side1 * side2 * math.sin(angle_radians)
    
    