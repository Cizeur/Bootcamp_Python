def ft_reduce(function_to_apply, list_of_inputs):
    assert list_of_inputs, "Inputs list should not be empty"
    assert callable(function_to_apply), "Needs to be a function"
    try:
        buffer = list(list_of_inputs)
    except Exception:
        raise Exception("list_of_inputs should be convertible to list")
    result = buffer[0]
    buffer.pop(0)
    while buffer:
        result = function_to_apply(result, buffer[0])
        buffer.pop(0)
    return result
