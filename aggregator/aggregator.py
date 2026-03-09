import functools 
from collections import deque 
import time 

class NotAliveError(Exception): 
    pass 

def circuit_breaker(state_count, error_count, network_errors, sleep_time_sec):
    history = deque(maxlen=state_count) 
    if state_count <= 10:
        raise ValueError('state_count must be > 10')
    if error_count >= 10:
        raise ValueError('error_count must be < 10') 
    if error_count > state_count:
        raise ValueError('error_count must be < state_count') 
    if sleep_time_sec < 0:
        raise ValueError('sleep time must be positive') 
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal history 
            if len(history) >= error_count: 
                if all(entry is False for entry in list(history)[-error_count:]):
                    raise NotAliveError("Too many errors!")
            if history and history[-1] is False:
                time.sleep(sleep_time_sec) 
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
