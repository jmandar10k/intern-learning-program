# 01 Python advanced

Level: intermediate. Time: ≈ 1 day (notes 1 h, core link 1.5 h, exercises 3 h).
Links: [study-materials.md](../study-materials.md#01-python-advanced).

You already write Python. This topic is about writing Python that other people can rely on:
clear objects, lazy data processing, reusable behavior, types and tests.

## After this topic you can

- Design small class hierarchies with `@dataclass`, properties, class methods and dunder methods.
- Use generators and iterators to process data lazily, and explain when that matters.
- Write decorators (with `functools.wraps`, with arguments) and context managers.
- Add type hints that a checker such as mypy can verify, including `Protocol`, `TypedDict`,
  generics and `Optional`.
- Write pytest tests with fixtures, parametrization and `pytest.raises`.
- Package code with `pyproject.toml` so it installs with `pip install -e .`.

## Concepts

### OOP that stays small

- Prefer `@dataclass` (or `@dataclass(frozen=True)` for value objects) over hand-written
  `__init__`/`__repr__`/`__eq__`.
- Use `@property` for derived values (`order.is_peak`), not stored duplicates that can drift.
- `@classmethod` for alternative constructors (`Order.from_dict(row)`), `@staticmethod` for
  helpers that need neither instance nor class.
- Composition over inheritance: a `DeliveryBatch` *has* orders; it is not an `Order`.
- Dunder methods make objects behave like built-ins: `__len__`, `__iter__`, `__contains__`,
  `__lt__` (for sorting).

### Iterators and generators

- An iterable produces an iterator (`iter(x)`); an iterator yields values with `next()` until
  `StopIteration`.
- A generator function (`yield`) builds an iterator lazily: memory stays flat no matter how many
  rows you stream.
- Generator pipelines: `read → parse → filter → batch`, each a generator; nothing runs until
  consumed.
- Gotcha: a generator is consumed once. Iterating it twice silently yields nothing the second
  time. (Silent bugs like this are the theme of Week 3.)
- `itertools`: `islice`, `groupby` (needs sorted input), `chain`, `batched` (3.12+).

### Decorators and context managers

- A decorator is a function that takes a function and returns a function. Always use
  `functools.wraps` to preserve name and docstring.
- Decorators with arguments are three levels deep: `def retry(times): def deco(fn): def wrapper(...)`.
- Built-ins worth knowing: `functools.lru_cache`/`cache`, `functools.cached_property`.
- Context managers (`with`) guarantee cleanup; write them with `contextlib.contextmanager` or
  `__enter__`/`__exit__`.

### Typing

- Hints are documentation a tool can check. Run `mypy yourfile.py`.
- Use built-in generics: `list[int]`, `dict[str, float]`, `X | None`.
- `Protocol` describes "anything with these methods" (structural typing), which is useful for tools
  and model interfaces in Week 2.
- `TypedDict` for dict-shaped records (LangGraph state in Week 2 uses it).
- `TypeVar` / generics for containers and helpers.

### Testing

- pytest discovers `test_*.py` files and `test_*` functions; plain `assert` is enough.
- Fixtures (`@pytest.fixture`) share setup; `@pytest.mark.parametrize` covers many cases cheaply.
- Test behavior, edge cases (empty input, NaN, one element) and failure paths (`pytest.raises`).
- A test that would have caught a silent bug is the best fix (Week 3 grading rewards this).

### Packaging

- One `pyproject.toml` declares name, version, dependencies and build backend.
- `src/` layout prevents accidentally importing the un-installed package.
- `pip install -e .` installs in editable mode for development.

## Exercises

In [exercises/](exercises/):

| File | What it shows |
|---|---|
| `ex01_oop_generators.py` | Dataclasses, properties, dunder methods, a generator pipeline, the consumed-once gotcha |
| `ex02_decorators_typing.py` | A timing decorator, a retry decorator with arguments, a context manager, `Protocol` and `TypedDict` |
| `test_ex01.py` | pytest tests with fixtures and parametrization; run `python -m pytest -q` |
| `packaging-example/` | A minimal `pyproject.toml` package you can `pip install -e` |

## Common mistakes

- Mutable default arguments (`def f(x=[])`).
- Forgetting `functools.wraps`, which breaks debugging and introspection.
- Iterating a generator twice.
- Type hints that lie (annotated `-> float`, returns `None` on some paths).
