import functools 

def circuit_breaker(state_count, error_count, networks_error, sleep_time_sec):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(args, kwargs) 
        return wrapper 
    return decorator
