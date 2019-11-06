import sys

def ft_map(function_to_apply, list_of_inputs):
    if (isinstance(list_of_inputs, list) == False):
        sys.exit("list_of_inputs must be a list")
    if (callable(function_to_apply) == False):
        sys.exit("function_to_aply must be a function")
    apply = []
    for element in list_of_inputs:
        apply.append(function_to_apply(element))
    return apply