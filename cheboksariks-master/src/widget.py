from src.masks import account_mask, card_mask


def convert_date(input_date: str) -> str:
    """Функция принимает строку вида 2021-01-01T00:00:00 и возвращает строку вида 01.01.2021"""
    date_parts = input_date.split("T")[0].split("-")
    return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"


def number_or_account(input_string: str) -> str:
    """Функция принимает строку и возвращает ее маску"""
    if "Счет" in input_string:  # Если входная строка содержит "Счет", вызываем функцию для маскировки счета
        masked_input = account_mask(input_string.split()[-1])
    else:  # Иначе вызываем функцию для маскировки карты
        masked_input = card_mask(input_string.split()[-1])

    return input_string.replace(input_string.split()[-1], masked_input)
