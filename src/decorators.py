import functools


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                error_type = type(e).__name__
                log_message = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"
                raised_exception = e
            else:
                raised_exception = None

            if filename:
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)

            if raised_exception:
                raise raised_exception

            return result

        return wrapper

    return decorator
