from param_parser_surface_area import *  # Module to analyze and break down input data into a structured, usable format
from calculate_surface_area import * # Module to calculate area of different polygons

def surface_area(*args):
    # First check if arguments are having values else display error
    if not args:  # Check if args is empty
        return "Error: No arguments were passed"
    else:
        dimensions, shape = param_parser(args) # Call param_parser method to recieve parsed users inputs for calculation
        print(f"param_parser_surface_area-  {dimensions}")
        
        if shape == "cube":
            result = cube(dimensions)
            print(f"calculate_surface_area:cube-  {result}")
            return result
        
        if shape == "cuboid":
            result = cuboid(dimensions)
            print(f"calculate_surface_area:cuboid-  {result}")
            return result
        

# Tests
# surface_area()
# surface_area("cube", "3m")
# surface_area("cuboid", "4m", "3m", "2m")
# surface_area("cuboid", "4cm", "3m", "2cm")