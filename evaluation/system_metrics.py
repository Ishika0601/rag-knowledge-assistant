import time

def measure_latency(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        latency = time.time() - start
        return result, latency
    return wrapper
