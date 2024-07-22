from datetime import datetime
from typing import Any


def filter_by_state(data: list, state: Any = "EXECUTED") -> list:
    """
    Фильтрация списка словарей по значению ключа 'state'.

    Args:
        data (list): Список словарей.
        state (str, optional): Значение для ключа 'state'. Defaults to 'EXECUTED'.

    Returns:
        list: Новый список, содержащий только те словари,
              у которых ключ 'state' содержит переданное значение.
    """
    filtered_data = [d for d in data if d["state"] == state]
    return filtered_data


def sort_by_date(data: list, order: Any = "desc") -> list:
    """
    Сортировка списка словарей по ключу 'date'.

    Args:
        data (list): Список словарей.
        order (str, optional): Порядок сортировки ('desc' - по убыванию,
                              'asc' - по возрастанию). Defaults to 'desc'.

    Returns:
        list: Новый список, в котором исходные словари отсортированы по дате.
    """
    if order not in ("desc", "asc"):
        raise ValueError("Invalid order value. Must be 'desc' or 'asc'.")

    return sorted(data, key=lambda item: datetime.fromisoformat(item["date"]), reverse=(order == "desc"))
