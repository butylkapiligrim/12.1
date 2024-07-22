from random import randint
from typing import Any, Generator, List


def transaction_info(transaction_descriptions: List[dict]) -> Generator[str, None, None]:
    """
    transaction_descriptions, возвращающий описания транзакций.
    """
    for transaction in transaction_descriptions:
        yield transaction["description"]


# Пример использования генератора """transaction_info"""


transactions_1 = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Перевод со счета на счет"},
    {"id": 4, "description": "Перевод с карты на карту"},
    {"id": 5, "description": "Перевод организации"},
]

descriptions_1 = transaction_info(transactions_1)

for _ in range(4):
    print(next(descriptions_1))


def filter_by_money(transaction_descriptions: List[dict], currency: str) -> Generator[Any, None, None]:
    """
    Генератор, возвращающий операции с заданной валютой из списка transactions.
    """
    for transaction in transaction_descriptions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


# Пример использования легендарной функции
transactions_2 = [
    {"id": 939719570, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
    {"id": 142264268, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
    {"id": 873106923, "operationAmount": {"currency": {"name": "RUB", "code": "RUB"}}},
    {"id": 895315941, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
]

dollars_transactions = filter_by_money(transactions_2, "USD")

for _ in range(2):
    print(next(dollars_transactions)["id"])
"""
Этот код испорльзует функцию `filter_by_money`, для фильтрации операции в
списке `transactions_2` по валюте,возвращая итератор с этими операциями.
"""


def card_number_generator(start: int, end: int) -> Generator[str, Any, None]:
    """
    Генератор номеров карт,должен генерировать номера карт
    вот так "**** **** **** ****",где * — цифра.
    Еще генерирует в указоной рендже (диопозоне)
    """
    for i in range(start, end + 1):
        yield "".join([str(randint(start, end)) for _ in range(16)])


# Пример не по матиматике , а по работе геератора
for card_number_1 in card_number_generator(1, 5):
    print(" ".join([card_number_1[i : i + 4] for i in range(0, len(card_number_1), 4)]))
