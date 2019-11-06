def ft_map(function_to_apply, list_of_inputs):
    assert callable(function_to_apply), "Needs to be a function"
    return [function_to_apply(x) for x in list_of_inputs]
