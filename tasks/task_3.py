from functools import wraps

POSITIVE_START = 0


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int)) and arg <= POSITIVE_START:
                raise ValueError("Позиционный аргумент arg должен быть положительными")

        for key, value in kwargs.items():
            if isinstance(value, (int)) and value <= POSITIVE_START:
                raise ValueError(
                    "Именованный аргумент kwargs должен быть положительными.")

        return func(*args, **kwargs)
    return wrapper
