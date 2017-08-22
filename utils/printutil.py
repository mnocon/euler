def console_print(function):
    def wrapper(*args, **kwargs):
        print(args[1:], kwargs)
        value = function(*args, **kwargs)
        print(value)
        return value

    return wrapper
