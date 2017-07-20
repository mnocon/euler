import time
def time_execution(function):
    def wrapper(*args, **kwargs):
        t0 = time.clock()
        value = function(*args, **kwargs)
        t1 = time.clock()
        print("Execution time: {:.3f} secs".format(t1 - t0))
        return value

    return wrapper
