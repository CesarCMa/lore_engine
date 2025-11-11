.PHONY: run
run:
	poetry run python -m lore_engine

.PHONY: unit-tests
unit-tests:
	poetry run pytest tests/unit
