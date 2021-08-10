""" Module utilities """

from functools import wraps
import time


def time_it(function):
    """Decorator : calculate duration of a function

    Args:
        function (function): time this function
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print("temps de traitement : ", duration, "s")
        return result
    return wrapper