from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        positional_args = [str(a) for a in args]
        keyword_args = [f"{k}={v}" for k, v in kwargs.items()]

        all_args = positional_args + keyword_args
        args_str = ", ".join(all_args)

        print(f"Вызов: {func.__name__}({args_str})")

        result = func(*args, **kwargs)

        print(f"Результат: {result}")

        return result
    return wrapper
