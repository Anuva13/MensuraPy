from param_parser import *
from calculate_area import *

def area(*args):
    # To check arguments are having values else put error
    if not args:  # Check if args is empty
        return "Error: No arguments were passed"
    else:
        dimensions, shape = param_parser(args)
    
        if shape == "square":
            result = square(dimensions)
            print (result)
            return result
        
        if shape == "rectangle":
            result = rectangle(dimensions)
            print (f"Result from param_parser {result}")
            return result
    

# Tests
# area()
# area("square", "3m")
area("rectangle", "3m", "5m")

"""
area("circle", "3m") 
area("triangle", "2m", "3m", "90degrees")
area("trapezium", "3m", "2m") 
"""  

    
