"""Tests for ex01. Run: python -m pytest -q"""
import pytest

from ex01_oop_generators import DeliveryBatch, Order, parse


@pytest.fixture
def north_order() -> Order:
    return Order(order_id=1, zone="north", hour=18, items=10, distance_km=3.0, delivery_minutes=50.0)


def test_properties(north_order: Order) -> None:
    assert north_order.is_peak
    assert north_order.is_late


@pytest.mark.parametrize("hour,expected", [(16, False), (17, True), (19, True), (20, False)])
def test_peak_boundaries(hour: int, expected: bool) -> None:
    o = Order(1, "north", hour, 1, 1.0, 10.0)
    assert o.is_peak is expected


def test_batch_rejects_wrong_zone(north_order: Order) -> None:
    batch = DeliveryBatch("south")
    with pytest.raises(ValueError):
        batch.add(north_order)


def test_empty_batch_late_rate_is_zero() -> None:
    assert DeliveryBatch("east").late_rate == 0.0


def test_parse_skips_nan_distance() -> None:
    rows = [
        {"order_id": 1, "zone": "north", "hour": 9, "items": 3, "distance_km": float("nan"), "delivery_minutes": 20},
        {"order_id": 2, "zone": "north", "hour": 9, "items": 3, "distance_km": 2.0, "delivery_minutes": 20},
    ]
    assert [o.order_id for o in parse(rows)] == [2]
