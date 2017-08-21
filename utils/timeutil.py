import time
def time_execution(function):
    def wrapper(*args, **kwargs):
        print("Start {}".format(function.__name__))
        t0 = time.clock()
        value = function(*args, **kwargs)
        t1 = time.clock()
        print("Execution time of {} : {:.3f} secs".format(function.__name__, t1 - t0))
        return value

    return wrapper
