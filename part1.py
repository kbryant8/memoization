cache = {}

def memoize(func, args):
    if (str(func) + str(args)) not in cache:
        cache[str(func) + str(args)] = func(args)
    return cache[str(func) + str(args)]
    
    