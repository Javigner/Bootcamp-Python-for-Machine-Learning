import sys

def ft_filter(function_to_apply, list_of_inputs):
    if (isinstance(list_of_inputs, list) == False and isinstance(list_of_inputs, range) == False):
        sys.exit("list_of_inputs must be a list")
    if (callable(function_to_apply) == False):
        sys.exit("function_to_aply must be a function")
    result = []
    for element in list_of_inputs:
        if (function_to_apply(element) == True):
            result.append(element)
    return result
