PIP := python -m pip

build: build-deps
	python -m build

install: build
	$(PIP) install dist/*.tar.gz

uninstall:
	$(PIP) uninstall .

clean:
	rm -rvf dist/ build/ src/*.egg-info

build-deps:
	@$(PIP) install --upgrade pip > /dev/null
	@python -c 'import build' > /dev/null 2>&1 || $(PIP) install build
