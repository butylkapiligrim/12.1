from src.masks import account_mask, card_mask


def test_card_mask() -> None:
    assert card_mask("1234567890123456") == "1234 56** **** 3456"
    assert card_mask("1596837868705199") == "1596 83** **** 5199"


def test_account_mask() -> None:
    assert account_mask("1234567890123456") == "**3456"
    assert account_mask("1596837868705199") == "**5199"
