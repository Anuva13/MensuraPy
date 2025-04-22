from .param_parser_perimeter import *  # Module to analyze and break down input data into a structured, usable format
from .calculate_perimeter import * # Module to calculate area of different polygons

def perimeter(*args):
    # First check if arguments are having values else display error
    if not args:  # Check if args is empty
        return "Error: No arguments were passed"
    else:
        dimensions, shape = param_parser(args) # Call param_parser method to recieve parsed users inputs for calculation
        print(f"param_parser_perimeter-  {dimensions}")
        
        if shape == "square":
            result = square(dimensions)
            print(f"calculate_perimeter:square-  {result}")
            return result
        
        if shape == "rectangle":
            result = rectangle(dimensions)
            print(f"calculate_perimeter:rectangle-  {result}")
            return result
        
        if shape == "circle":
            result = circle(dimensions)
            print(f"calculate_perimeter:circle-  {result}")
            return result
        
        if shape == "triangle":
            result = triangle(dimensions)
            print(f"calculate_perimeter:triangle-  {result}")
            return result
        
        if shape == "parallelogram":
            result = parallelogram(dimensions)
            print(f"calculate_perimeter:parallelogram-  {result}")
            return result
        
        if shape == "rhombus":
            result = rhombus(dimensions)
            print(f"calculate_perimeter:rhombus-  {result}")
            return result
        
        if shape == "trapezium":
            result = trapezium(dimensions)
            print(f"calculate_perimeter:trapezium-  {result}")
            return result
        
        if shape == "ellipse":
            result = ellipse(dimensions)
            print(f"calculate_perimeter:ellipse-  {result}")
            return result
        
        if shape == "cube":
            result = cube(dimensions)
            print(f"calculate_perimeter:cube-  {result}")
            return result
        
        if shape == "cuboid":
            result = cuboid(dimensions)
            print(f"calculate_perimeter:cuboid-  {result}")
            return result
        
        if shape == "sphere":
            result = square(dimensions)
            return "Error: Perimeter not defined for sphere"
            
        if shape == "cylinder":
            result = cylinder(dimensions)
            print(f"calculate_perimeter:cylinder-  {result}")
            return result
        
        if shape == "cone":
            result = cone(dimensions)
            print(f"calculate_perimeter:cone-  {result}")
            return result
        
        if shape == "pyramid":
            result = pyramid(dimensions)
            print(f"calculate_perimeter:pyramid-  {result}")
            return result
        
        if shape == "hemisphere":
            result = hemisphere(dimensions)
            print(f"calculate_perimeter:hemisphere-  {result}")
            return result
        

# Tests
# perimeter()
# perimeter("square", "3m")
# perimeter("square", "3cm")
# perimeter("rectangle", "3m", "4m")
# perimeter("rectangle", "3cm", "4m")
# perimeter("circle", "3m")
# perimeter("circle", "3mm")
# perimeter("triangle", "4m")
# perimeter("triangle", "4m", "2cm", "4m")
# perimeter("triangle", "4m", "2m")
# perimeter("parallelogram", "4cm", "2m")
# perimeter("triangle", "4m", "2cm")
# perimeter("rhombus", "3m")
# perimeter("trapezium", "4m", "2m", "4m", "3m")
# perimeter("ellipse", "4m", "3m")
# perimeter("cube", "4m")
# perimeter("cube", "4cm")
# perimeter("cuboid", "5m", "3m", "2m")
# perimeter("cuboid", "5cm", "3cm", "2cm")
# perimeter("sphere", "5m")
# perimeter("cylinder", "3m")
# perimeter("cylinder", "3m", "10m")
# perimeter("cylinder", "3cm", "10cm")
# perimeter("cone", "4m")
# perimeter("cone", "4m", "6m")
# perimeter("pyramid", "6m", "5m")
# perimeter("hemisphere", "5m")







