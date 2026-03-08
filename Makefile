.PHONY: install test train run clean

install:
	pip install -r requirements.txt

test:
	pytest tests/

train:
	python scripts/train.py --epochs 10

run:
	python scripts/run_inference.py --disease TARGET_DISEASE_1

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
