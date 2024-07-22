import pytest

from src.widget import convert_date, number_or_account


@pytest.mark.parametrize("input_date,expected_output", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_convert_date(input_date: str, expected_output: str) -> None:
    assert convert_date(input_date) == expected_output


def test_number_or_acount() -> None:
    assert number_or_account("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert number_or_account("Счет 64686473678894779589") == "Счет **9589"
    assert number_or_account("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
