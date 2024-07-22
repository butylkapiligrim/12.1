import json
import os
from pathlib import Path

from unittest.mock import MagicMock, Mock, mock_open, patch

"""# Для создания заглушек импортируем Mock и patch."""

import requests
from dotenv import load_dotenv

from src.utils import get_curr_rate, read_json_f, summ_amount

load_dotenv()
API_KEY = os.getenv("api_key")

"""# Импортируем Mock и patch с целью создания заглушек."""


@patch("requests.get")
def test_get_transaction_ruble_api_error(mock_get: Mock) -> None:
    """# Заглушка ответа создается для вызова исключения при проверке статуса."""
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.RequestException
    mock_get.return_value = mock_response

    result = get_curr_rate("USD")
    assert result == 1.0


@patch("requests.get")
def test_get_transaction_ruble_api_success(mock_get: MagicMock) -> None:
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}
    t = {"amount": 100, "currency": "USD"}
    assert get_curr_rate(t) == 75.0


"""# Заглушка ответа создается для вызова исключения при проверке статуса."""
@patch("builtins.open", create=True)
def test_read_transactions_works(mock_open: MagicMock) -> None:
    # Создаем тестовые данные
    test_data = [{"amount": 100, "currency": "RUB"}]
    # Подготавливаем мокированный файл с помощью mock_open
    mock_open.return_value.read.return_value = json.dumps(test_data)
    # Проверяем, что функция возвращает правильный список транзакций
    result = read_json_f(Path("test_transactions.json"))
    assert result == []


"""# Тестируем функцию read_transactions при наличии пустого файла."""


def test_read_transactions_emp_file() -> None:
    # Создаем пустой файл
    with open("test_transactions.json", "w") as f:
        pass

    """# Проверяем, что функция возвращает список, не содержащий элементов."""
    result = read_json_f(Path("test_transactions.json"))
    assert result == []

    os.remove("test_transactions.json")

    """  
    Проверяется, что функция sum_amount правильно извлекает сумму из переданного словаря,
    который содержит информацию об операции. Ожидается, что функция вернет сумму 31957.58."""
    """


def test_sums_amount() -> None:
    assert (
            summ_amount(
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            )
            == 31957.58
    )
