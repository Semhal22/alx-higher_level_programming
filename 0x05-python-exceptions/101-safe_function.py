#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = None
    try:
        result = fct(*args)
    except (ZeroDivisionError, TypeError, IndexError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
    finally:
        return result
