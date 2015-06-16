.PHONY: clean
clean:
	@find ./ -name "*.pyc" -exec rm -f {} \;

.PHONY: install
install: clean
	@pip install -r requirements.txt

.PHONY: run
run:
	@gunicorn app:app

.PHONY: test
test:
	@nosetests tests -v
	@flake8 .