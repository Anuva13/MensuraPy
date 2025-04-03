from param_parser import *

def area(*args):
    # To check arguments are having values else put error
    if not args:  # Check if args is empty
        return "Error: No arguments were passed"
    else:
        param_parser(args)
    

# Tests
area()
area("square", "3m")
area("rectangle", "3m", "5m")
area("circle", "3m") 
area("triangle", "2m", "3m", "90degrees")
area("trapezium", "3m", "2m")   

    
