import aspectlib
from part1 import memoize
from aspectlib import Proceed
from aspectlib import Aspect
cache = {}
    
@Aspect(bind=True)
def memoize_aspect(cutpoint, *args, **kwargs):
    if (str(cutpoint.__name__) + str(args)) not in cache:
        cache[str(cutpoint.__name__) + str(args)] = yield Proceed(*args, **kwargs) # call the actual function with all parameters

    return cache[str(cutpoint.__name__) + str(args)]


