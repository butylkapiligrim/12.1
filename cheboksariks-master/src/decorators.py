import datetime
import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который логирует вызов функции и ее результат в файл или в консоль.

    Args:
        filename: Имя файла для записи логов. Если не указано, логи будут выводиться в консоль.

    Returns:
        Декорируемая функция.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def processing(*args: Any, **kwargs: Any) -> Any:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                message_log = f"{timestamp} {func.__name__} ok"
            except Exception as e:
                result = None
                message_log = f"{timestamp} {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

            if filename:
                with open(filename, "a") as f:
                    f.write(message_log + "\n")
            else:
                print(message_log)
            return result

        return processing

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)  # Вывод в файл mylog.txt
