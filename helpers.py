import gc
from datetime import timedelta
from functools import wraps


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


def shift_date(date, days_to_shift):
    '''shift date on days_to_shift earlier'''
    date -= timedelta(days_to_shift)
    return date


def not_none(y):
    return {x for x in set(y) if x==x}
