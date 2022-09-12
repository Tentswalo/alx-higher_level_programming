#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        r = fct(*args)
        return r
    except Exception as erros:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
