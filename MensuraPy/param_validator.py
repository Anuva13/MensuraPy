# Validate 
def square_param_validator(args):
    if len(args) == 2:
        return True
    else:
        return False
    
def rectangle_param_validator(args):
    if len(args) == 3:
        return True 
    else:
        return False
    
def circle_param_validator(args):
    if len(args) == 2:
        return True 
    else:
        return False
    
def triangle_param_validator(args):
    if len(args) == 4:
        return True 
    elif len(args) == 3:
        return True 
    elif len(args) == 2:
        return True 
    else:
        return False
    
def parallelogram_param_validator(args):
    if len(args) == 3:
        return True 
    elif len(args) == 4:
        return True 
    else:
        return False
    
def rhombus_param_validator(args):
    print(f"param_validator:rhombus_param_validator-  {args}")
    if len(args) == 3:
        return True 
    elif len(args) == 4:
        return True 
    else:
        return False  