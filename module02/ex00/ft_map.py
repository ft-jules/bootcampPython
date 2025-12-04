def ft_map(function, iterable, *args):
    if args:
        all_iterables = (iterables,) + args
        for elements in zip(*all_iterables):
            yield function(*elements)
    else:
        for elements in iterable:
            yield function(element)