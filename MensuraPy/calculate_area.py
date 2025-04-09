import math
from unit_converter import * # Module to convert dimensions to base unit 'm'

def square(dictionary):
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for key, values in dictionary.items() for item in [key] + values]
    side = flat_list[1]
    area = side * side
    result = str(area) + flat_list[0] + str(2)
    # Returns the area of a square.
    return result

def rectangle(list, target_unit='m'):
    print(f"area:area-  {list}")
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for d in list for key, values in d.items() for item in [key] + values]
    # '1' and '3' i.e. odd numbers have values and even numbers have keys (units)
    length = flat_list[1]
    length_unit = flat_list[0]
    breadth = flat_list[3]
    breadth_unit = flat_list[2]
    
    # Convert both to target unit (default is meters)
    length_converted = convert_to_base_unit(length, length_unit, target_unit)
    breadth_converted = convert_to_base_unit(breadth, breadth_unit, target_unit)
    
    # Compute area in square of the target unit
    area = length_converted * breadth_converted
    result = f"{area} {target_unit}²"
    # Returns the area of a rectangle
    return result

def circle(dictionary):
    print(f"area:area-  {dictionary}")
    flat_list = [item for key, values in dictionary.items() for item in [key] + values]
    radius = flat_list[1]
    area = math.pi * radius ** 2
    result = str(area) + flat_list[0] + str(2)
    # Returns the area of a circle.
    return result

def triangle(list):
    print(f"area:area-  {list}")
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for d in list for key, values in d.items() for item in [key] + values]
    print(f"area:area-  {flat_list}")
    # '1' and '3' i.e. odd numbers have values and even numbers have keys (units)
    l = len(flat_list)
    if l == 2:
        side = flat_list[1]
        area = math.sqrt(3) / 4 * side ** 2
        result = str(area) + flat_list[0] + str(2)
        return result
        
    elif l == 4:
        base = flat_list[1]
        height = flat_list[3]
        result = 0.5 * base * height
        result = str(area) + flat_list[0] + str(2)
        return result
        
    elif l == 6:
        unit_1 = flat_list[0]
        unit_2 = flat_list[2]
        unit_3 = flat_list[4]
        value_1 = flat_list[1]
        value_2 = flat_list[3]
        value_3 = flat_list[5]
        
        if unit_1 == 'degrees' and value_1 < 180:
            angle_radians = math.radians(value_1)
            area = 0.5 * value_2 * value_3 * math.sin(angle_radians)
            result = str(area) + unit_3 + str(2)
            return result
        
        elif unit_2 == 'degrees' and value_2 < 180:
            angle_radians = math.radians(value_2)
            area = 0.5 * value_1 * value_3 * math.sin(angle_radians)
            result = str(area) + unit_1 + str(2)
            return result
        
        elif unit_3 == 'degrees' and value_3 < 180:
            angle_radians = math.radians(value_3)
            area = 0.5 * value_1 * value_2 * math.sin(angle_radians)
            result = str(area) + unit_2 + str(2)
            return result
        
        else:
            s = (value_1 + value_2 + value_3)/2
            # Returns the area of a triangle when 3 sides are given
            area = math.sqrt(s * (s - value_1) * (s - value_2) * (s - value_3))
            result = str(area) + unit_1 + str(2)
            return result

    
    