from param_parser import *  # Module to analyze and break down input data into a structured, usable format
from calculate_area import * # Module to calculate area of different polygons

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
        
        
    

# Tests
# area()
# area("square", "3m")
#area("rectangle", "3m", "5m")
area("circle", "3m")

""" 
area("triangle", "2m", "3m", "90degrees")
area("trapezium", "3m", "2m") 
"""  

    
