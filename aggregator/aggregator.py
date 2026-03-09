import functools 
from collections import deque 

class NotAliveError(Exception): 
    pass 

def circuit_breaker(state_count, error_count, network_errors, sleep_time_sec):
    history = deque(maxlen=state_count) 
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal history 
            if len(history) >= error_count: 
                if all(entry is False for entry in list(history)[-error_count:]):
                    raise NotAliveError("Too many errors!")
            try:
                result = func(*args, **kwargs)  
            except network_errors:
                history.append(False) 
                raise 
            else:
                history.append(True) 
                return result 
        return wrapper 
    return decorator
