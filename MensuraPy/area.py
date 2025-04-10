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
        
        if shape == "parallelogram":
            result = parallelogram(dimensions)
            print(f"calculate_area:parallelogram-  {result}")
            return result

        if shape == "rhombus":
            result = rhombus(dimensions)
            print(f"calculate_area:rhombus-  {result}")
            return result        
        
        
        
    

# Tests
# area()
# area("square", "3m")
# area("rectangle", "3m", "5cm")
# area("circle", "3m")
# area("triangle", 2m)
# area("triangle", "2m", "3cm", "30degrees")
# area("triangle", "3m", "400cm")
# area("triangle", "1.2m", "85cm", "0.00095km")
# area("parallelogram", "10m", "6m")
# area("parallelogram", "8m", "5m", "60degrees")
# area("parallelogram", "8m", "5000mm", "60degrees")
# area("rhombus", "8m", "6m")
# area("rhombus", "800cm", "6m")
 

    
