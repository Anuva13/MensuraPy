import math
from unit_converter import * # Module to convert dimensions to base unit 'm'

def square(dictionary, target_unit = 'm'):
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for key, values in dictionary.items() for item in [key] + values]
    side_value = flat_list[1]
    side_unit = flat_list[0]
    
    # Convert side to target unit (default is meters)
    side = convert_to_base_unit(side_value, side_unit, target_unit)
    
    # Compute perimeter of a square in the target unit
    perimeter = 4 * side
    result = f"{perimeter} {target_unit}"
    # Returns the perimeter of a square.
    return result