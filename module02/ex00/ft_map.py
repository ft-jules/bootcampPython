def ft_map(function, iterable, *args):
    if args:
        all_iterables = (iterable,) + args
        for element in zip(*all_iterables):
            yield function(*element)
    else:
        for element in iterable:
            yield function(element)