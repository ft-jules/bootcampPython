def ft_filter(function, iterable):
    if function is None:
        for element in iterable:
            if element:
                yield element
    else:
        for element in iterable:
            if function(element):
                yield element