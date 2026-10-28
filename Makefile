.PHONY: setup dev run stop test test-eval test\:eval migrate seed install clean

PYTHON = .venv/bin/python
PIP = .venv/bin/pip

setup: install migrate seed

dev: run

run:
	@fuser -k -9 8000/tcp 2>/dev/null || true
	$(PYTHON) manage.py runserver 0.0.0.0:8000

stop:
	@fuser -k -9 8000/tcp 2>/dev/null || true

test:
	$(PYTHON) manage.py test links

test-eval:
	@if [ -f backend/links/eval_hidden.py ]; then \
		$(PYTHON) manage.py test links.eval_hidden; \
	else \
		echo "[Evaluation] Hidden evaluation suite (links.eval_hidden) is reserved for grading."; \
	fi

test\:eval: test-eval

migrate:
	$(PYTHON) manage.py migrate

makemigrations:
	$(PYTHON) manage.py makemigrations

seed:
	$(PYTHON) manage.py seed

install:
	python3 -m venv .venv
	$(PIP) install -r requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
