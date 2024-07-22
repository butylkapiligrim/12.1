import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture()
def list_for_functions() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date(list_for_functions: list[dict]) -> None:
    assert sort_by_date(list_for_functions, order="asc") == [
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]


def test_filter_by_state(list_for_functions: list[dict]) -> None:
    assert filter_by_state(list_for_functions, state="CANCELED") == [
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
    ]
