"""Week 1 / 01 Python advanced / Exercise 1: OOP and generators.

Run:  python ex01_oop_generators.py
"""
from __future__ import annotations

import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from freshcart_data import make_orders  # noqa: E402


@dataclass(frozen=True)
class Order:
    order_id: int
    zone: str
    hour: int
    items: int
    distance_km: float
    delivery_minutes: float

    @property
    def is_peak(self) -> bool:
        return 17 <= self.hour <= 19

    @property
    def is_late(self) -> bool:
        return self.delivery_minutes > 45

    @classmethod
    def from_row(cls, row: dict) -> "Order":
        return cls(
            order_id=int(row["order_id"]),
            zone=str(row["zone"]),
            hour=int(row["hour"]),
            items=int(row["items"]),
            distance_km=float(row["distance_km"]),
            delivery_minutes=float(row["delivery_minutes"]),
        )


@dataclass
class DeliveryBatch:
    zone: str
    orders: list[Order] = field(default_factory=list)  # never use a mutable default directly

    def add(self, order: Order) -> None:
        if order.zone != self.zone:
            raise ValueError(f"order {order.order_id} is in {order.zone}, batch is {self.zone}")
        self.orders.append(order)

    def __len__(self) -> int:
        return len(self.orders)

    def __iter__(self) -> Iterator[Order]:
        return iter(self.orders)

    @property
    def late_rate(self) -> float:
        return sum(o.is_late for o in self.orders) / len(self) if self.orders else 0.0


# --- Generator pipeline: nothing runs until consumed --------------------------------

def read_rows(n: int) -> Iterator[dict]:
    df = make_orders(n=n, with_noise=True)
    for row in df.to_dict(orient="records"):
        yield row


def parse(rows: Iterable[dict]) -> Iterator[Order]:
    for row in rows:
        if row["distance_km"] != row["distance_km"]:  # NaN check without numpy
            continue
        yield Order.from_row(row)


def only_zone(orders: Iterable[Order], zone: str) -> Iterator[Order]:
    return (o for o in orders if o.zone == zone)


def main() -> None:
    orders = parse(read_rows(500))
    north = only_zone(orders, "north")
    batch = DeliveryBatch("north")
    for o in north:
        batch.add(o)
    print(f"north batch: {len(batch)} orders, late rate {batch.late_rate:.1%}")
    print(f"first order peak? {next(iter(batch)).is_peak}")

    # Gotcha: generators are consumed once.
    gen = parse(read_rows(100))
    first_pass = sum(1 for _ in gen)
    second_pass = sum(1 for _ in gen)
    print(f"generator first pass={first_pass}, second pass={second_pass}  <- silent!")

    print(
        "\nYour turn:\n"
        "  1. Add __lt__ to Order so sorted(batch) sorts by delivery_minutes.\n"
        "  2. Write a generator `batched(orders, size)` yielding lists of `size` orders.\n"
        "  3. Make DeliveryBatch.late_rate a functools.cached_property. What breaks when\n"
        "     you add() after reading it? Why is that a silent bug?"
    )


if __name__ == "__main__":
    main()
