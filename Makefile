VENV = ./.venv
PYTHON = $(VENV)/bin/python3.11

# .PHONY run
run: 
	$(PYTHON) main.py

test:
	$(PYTHON) ./tests/runner.py