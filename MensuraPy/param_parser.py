from param_validator import *
import re
def param_parser(args):
    
    # Recieving arguments
    print(f"Recieved arguments in param parser {args}")
    # Split the arguments recieved from area and enlist them
    match args[0]:
        case 'square':
            return square_param_parser(args), args[0]    
        case 'rectangle':
            return rectangle_param_parser(args), args[0]
        case 'circle':
            print(f"Arguments parsed for circle {args}")
        case 'triangle':
            print(f"Arguments parsed for triangle {args}")
        case _:
            print("Invalid")
            
# regex operation to determine the unit and values of the args
def extract_value_and_unit(value_string):
    # Regular expression to match the numeric value followed by a unit
    match = re.match(r"(\d+\.?\d*)\s*(\w+)", value_string)
    
    if match:
        value = float(match.group(1))  # Extract the value as a float
        unit = match.group(2)          # Extract the unit
        print(value,unit)
        return value, unit
    else:
        return None, None  # If no match is found
    
# packing the extracted parameters
def pack_value_and_unit(value, unit):
    # Initialise an empty dict
    data = {}

    # Adding multiple values under the same key manually
    data.setdefault(unit, []).append(value)
    return data
            
def square_param_parser(args):
    
    # Call param_validator to validate the arguments being suitable for the calculation
    # Sending arguments to param_validator for validation and if it returns true
    if square_param_validator(args):
        side = args[1]
        # extract argument 1 and send to extractor
        value, unit = extract_value_and_unit(side)
    
        # Assigning the packed value and unit to be used for calculation in area program
        data = pack_value_and_unit(value, unit)
        return data
    else:
        return {}
    
def rectangle_param_parser(args):
    # Initialising a list to append the extracted unit and values
    data_packer = []    
    if rectangle_param_validator(args):
        # extract arguments and send to extractor
        for i in range(len(args)-1):
            dimension = args[i+1]
            value, unit = extract_value_and_unit(dimension)
            data = pack_value_and_unit(value, unit)
            # Inserting the extracted value and unit in the initialised list
            data_packer.append(data)
        print(f"test3 {data_packer}")
        return data_packer
    else:
        return data_packer
                
            
        
    
        
       
            
    
