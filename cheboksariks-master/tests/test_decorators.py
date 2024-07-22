from src.decorators import my_function


def test_my_function() -> None:
    assert my_function(1, 2) == 3
    assert my_function(2, 2) == 4
    assert my_function(3, 2) == 5
    assert my_function(4, 2) == 6
    assert my_function(5, 2) == 7
