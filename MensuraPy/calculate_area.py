import math

def square(dictionary):
    side = list(dictionary.values()) # get the first (and only) value
    side1 = side[0] # extracted first value from the nested array formed when dict is extracted
    side1= side1[0]
    unit = list(dictionary.keys())
    unit1 = unit[0]
    area = side1 * side1
    result = str(area)+unit1+str(2)
    # Returns the area of a square.
    return result

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
    
    