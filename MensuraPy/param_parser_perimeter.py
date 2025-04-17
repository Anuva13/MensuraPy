from param_validator_perimeter import * # Module to validate arguments
import re # Module used to extract the user input values into values and units
def param_parser(args):
    
    # Recieving arguments
    print(f"perimeter:perimeter-  {args}")
    # Based on the shape of polygon call the relevant method to split the arguments & list them
    try:
        match args[0]:
            case 'square':
                return square_param_parser(args), args[0]    
            case _:
                print("Error: Invalid shape")
    except IndexError:
        print("Something went wrong- Index not in range!")
            
# Regex operation to determine the 'unit' and 'value' of the args recieved from method 'square_param_parser'
def extract_value_and_unit(value_string):
    # Regular expression to match the numeric value followed by a unit
    match = re.match(r"(\d+\.?\d*)\s*(\w+)", value_string)
    
    if match:
        value = float(match.group(1))  # Extract the value as a float
        unit = match.group(2)          # Extract the unit
        print(f"param_parser_surface_area:extract_value_and_unit-  {value},{unit}")              
        return value, unit
    else:
        return None, None  # If no match is found
    
# Packing the extracted parameters from method 'extract_value_and_unit'
def pack_value_and_unit(value, unit):
    # Initialise an empty dict
    data = {}

    # Adding multiple values under the same key manually
    data.setdefault(unit, []).append(value)
    return data    
            
def square_param_parser(args):
    
    """Call param_validator to check if the arguments are suitable for the calculation
    and if it returns True"""
    if square_param_validator(args):
        # extract argument 1 and send to extractor and recieve the 'value' and 'unit' splitted and made suitable for calculation
        side = args[1]
        value, unit = extract_value_and_unit(side)
    
        # Pack 'value' and 'unit' in 'data' to be used for calculation in area program
        data = pack_value_and_unit(value, unit)
        print(f"param_parser_perimeter:pack_value_and_unit-  {data}")
        # Return extracted and packed 'value' and 'unit' to Module 'area'
        return data
    else:
        return {}