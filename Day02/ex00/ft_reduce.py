import sys

def ft_reduce(function_to_apply, list_of_inputs):
    if (isinstance(list_of_inputs, list) == False and isinstance(list_of_inputs, range) == False):
        sys.exit("list_of_inputs must be a list")
    if (callable(function_to_apply) == False):
        sys.exit("function_to_aply must be a function")
    result = list_of_inputs[0]
    i = 1
    while(i < len(list_of_inputs)):
        result = function_to_apply(result, list_of_inputs[i])
        i += 1
    return result