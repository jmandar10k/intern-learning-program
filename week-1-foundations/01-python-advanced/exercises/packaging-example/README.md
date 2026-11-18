# packaging-example

Minimal `src/`-layout package.

```bash
cd packaging-example
pip install -e ".[dev]"
python -m pytest -q
python -c "from freshcart_eta import eta_minutes; print(eta_minutes(3.0, 1))"
```

Your turn: add a console script entry point (`[project.scripts]`) named `freshcart-eta` that
prints an ETA from command-line arguments, reinstall, and run it.
