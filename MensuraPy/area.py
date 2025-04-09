from param_parser import *  # Module to analyze and break down input data into a structured, usable format
from calculate_area import * # Module to calculate area of different polygons
from unit_converter import * # Module to convert dimensions to base unit 'm'

def area(*args):
    # First check if arguments are having values else display error
    if not args:  # Check if args is empty
        return "Error: No arguments were passed"
    else:
        dimensions, shape = param_parser(args) # Call param_parser method to recieve parsed users inputs for calculation
        print(f"param_parser-  {dimensions}")
        
        if shape == "square":
            result = square(dimensions)
            print(f"calculate_area:square-  {result}")
            return result
        
        if shape == "rectangle":
            result = rectangle(dimensions)
            print (f"calculate_area:rectangle-  {result}")
            return result
        
        if shape == "circle":
            result = circle(dimensions)
            print(f"calculate_area:circle-  {result}")
            return result
        
        if shape == "triangle":
            result = triangle(dimensions)
            print(f"calculate_area:triangle-  {result}")
            return result
        
        
    

# Tests
# area()
# area("square", "3m")
# area("rectangle", "3m", "5cm")
# area("triangle", 2m)
# area("triangle", "2m", "3cm", "30degrees")
# area("triangle", "3m", "400cm")
area("triangle", "1.2m", "85cm", "0.00095km")

"""
# area("circle", "3m")
area("trapezium", "3m", "2m") 
"""  

    
