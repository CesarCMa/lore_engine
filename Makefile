.PHONY: run
run:
	poetry run python -m lore_engine

.PHONY: unit-tests
unit-tests:
	poetry run pytest tests/unit

.PHONY: run-logs
run-logs:
	mkdir -p logs
	poetry run python -m lore_engine 2>&1 | tee logs/app.log
