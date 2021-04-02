import sys
from functools import wraps
from gc import get_referents
from types import ModuleType, FunctionType


BLACKLIST = type, ModuleType, FunctionType


def getsize(obj):
    """sum size of object & members."""
    if isinstance(obj, BLACKLIST):
        raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size


def memory_intensive(func):
    """
    Decorator for memory intensive functions. Calls gc.collect() before and after the function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        gc.collect()
        try:
            return func(*args, **kwargs)
        finally:
            gc.collect()

    return wrapper