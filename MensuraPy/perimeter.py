from param_parser_perimeter import *  # Module to analyze and break down input data into a structured, usable format
from calculate_perimeter import * # Module to calculate area of different polygons

def perimeter(*args):
    # First check if arguments are having values else display error
    if not args:  # Check if args is empty
        return "Error: No arguments were passed"
    else:
        dimensions, shape = param_parser(args) # Call param_parser method to recieve parsed users inputs for calculation
        print(f"param_parser_perimeter-  {dimensions}")
        
        if shape == "square":
            result = square(dimensions)
            print(f"calculate_surface_area:square-  {result}")
            return result
        

# Tests
# perimeter()
# perimeter("square", "3m")
# perimeter("square", "3cm")