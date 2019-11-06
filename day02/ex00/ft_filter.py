def ft_filter(function_to_apply, list_of_inputs):
    assert callable(function_to_apply), "Needs to be a function"
    return [x for x in list_of_inputs if function_to_apply(x)]
