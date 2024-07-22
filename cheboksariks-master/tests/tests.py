# from src.masks import account_mask, card_mask
from src.processing import filter_by_state, sort_by_date
from src.widget import convert_date, number_or_account

#
#
# nums_card_input = str(input("Введите номер карты: "))
# card_mask(nums_card_input)
#
# nums_check_input = str(input("Введите номер счета: "))
# tests_mask(nums_check_input)

print(convert_date("2018-07-11T02:26:18.671407"))

inputs = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

for input_str in inputs:
    print(number_or_account(input_str))

"""Проверка модуля processing"""

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

""" Фильтрация по статусу 'CANCELED'"""
canceled_data = filter_by_state(data, state="CANCELED")
print(canceled_data)

""" Сортировка по дате по возрастанию"""
sorted_data = sort_by_date(data, order="asc")
print(sorted_data)
