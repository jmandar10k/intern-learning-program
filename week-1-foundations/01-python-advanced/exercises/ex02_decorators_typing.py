"""Week 1 / 01 Python advanced / Exercise 2: decorators, context managers, typing.

Run:  python ex02_decorators_typing.py
Optional type check:  pip install mypy && mypy ex02_decorators_typing.py
"""
from __future__ import annotations

import functools
import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from typing import Protocol, TypedDict, TypeVar

T = TypeVar("T")


def timed(fn: Callable[..., T]) -> Callable[..., T]:
    """Print how long fn took. functools.wraps keeps fn's name and docstring."""

    @functools.wraps(fn)
    def wrapper(*args, **kwargs) -> T:
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            print(f"[timed] {fn.__name__} took {(time.perf_counter() - start) * 1000:.2f} ms")

    return wrapper


def retry(times: int, exceptions: tuple[type[Exception], ...] = (Exception,)):
    """Decorator with arguments: three levels of functions."""

    def decorator(fn: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs) -> T:
            last: Exception | None = None
            for attempt in range(1, times + 1):
                try:
                    return fn(*args, **kwargs)
                except exceptions as exc:  # noqa: PERF203
                    last = exc
                    print(f"[retry] attempt {attempt} failed: {exc}")
            assert last is not None
            raise last

        return wrapper

    return decorator


@contextmanager
def stage(name: str) -> Iterator[None]:
    print(f"-> {name}")
    try:
        yield
    finally:
        print(f"<- {name}")


# --- Typing: structural interfaces and dict-shaped records ---------------------------

class EtaModel(Protocol):
    def predict_minutes(self, distance_km: float, courier_load: int) -> float: ...


class LinearEta:
    def __init__(self, base: float = 12.0, per_km: float = 4.2, per_load: float = 3.0) -> None:
        self.base, self.per_km, self.per_load = base, per_km, per_load

    def predict_minutes(self, distance_km: float, courier_load: int) -> float:
        return self.base + self.per_km * distance_km + self.per_load * courier_load


class EtaResult(TypedDict):
    order_id: int
    eta_minutes: float
    at_risk: bool


@timed
def score_orders(model: EtaModel, orders: list[tuple[int, float, int]]) -> list[EtaResult]:
    out: list[EtaResult] = []
    for order_id, dist, load in orders:
        eta = model.predict_minutes(dist, load)
        out.append({"order_id": order_id, "eta_minutes": round(eta, 1), "at_risk": eta > 45})
    return out


_calls = {"n": 0}


@retry(times=3, exceptions=(ConnectionError,))
def flaky_lookup() -> str:
    _calls["n"] += 1
    if _calls["n"] < 3:
        raise ConnectionError("simulated transient failure")
    return "ok"


def main() -> None:
    with stage("scoring"):
        results = score_orders(LinearEta(), [(1, 2.0, 0), (2, 6.5, 2), (3, 8.0, 3)])
    for r in results:
        print(r)
    with stage("flaky lookup"):
        print("lookup:", flaky_lookup())
    print(f"score_orders.__name__ = {score_orders.__name__!r} (thanks to functools.wraps)")
    print(
        "\nYour turn:\n"
        "  1. Write @validate_non_negative that raises ValueError if any float arg < 0.\n"
        "  2. Add a second EtaModel (e.g. per-zone base) without inheriting from LinearEta;\n"
        "     confirm mypy accepts it because it matches the Protocol.\n"
        "  3. Remove functools.wraps and observe what changes."
    )


if __name__ == "__main__":
    main()
