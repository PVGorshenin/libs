from datetime import timedelta


def shift_date(date, days_to_shift):
    '''shift date on days_to_shift earlier'''
    date -= timedelta(days_to_shift)
    return date


def not_none(y):
    return {x for x in set(y) if x==x}
