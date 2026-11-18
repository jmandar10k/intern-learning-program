import pytest

from freshcart_eta import eta_minutes


def test_eta_basic():
    assert eta_minutes(0) == 12.0


def test_eta_rain_adds_time():
    assert eta_minutes(2, rain=True) > eta_minutes(2)


def test_eta_rejects_negative():
    with pytest.raises(ValueError):
        eta_minutes(-1)
