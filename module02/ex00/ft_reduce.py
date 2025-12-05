def ft_reduce(function, iterable, initializer = None):
    it = iter(iterable)
    if initializer is None:
        try:
            accumulator = next(it)
        except Stopteration:
            raise TypeError("ft_reduce() of empty sequence with no initial value")
    else:
        accumulator = initializer
    for element in it:
        accumulator = function(accumulator, element)
    return accumulator