# Agent Instructions

## Package Management

This project uses Poetry for package management. Always run Python modules with the `poetry run` command:

```bash
poetry run python -m module_name
poetry run pytest
```

## Testing

- Unit tests are located in `tests/unit/`
- Test files should be named `test_<name_of_the_file>.py`
- Example: if testing `src/lore_engine/utils.py`, create `tests/unit/test_utils.py`
- Run unit tests with: `make unit-tests` or `poetry run pytest tests/unit`

## Code Quality

This project uses Ruff for both linting and formatting:

```bash
poetry run ruff check .
poetry run ruff format .
```
