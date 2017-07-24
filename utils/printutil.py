def console_print(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        print(value)
        return value

    return wrapper
