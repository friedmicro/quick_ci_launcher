build: clean
	pyinstaller athena-ncurses.py
	mv dist/athena-ncurses/_internal dist/
	mv dist/athena-ncurses/athena-ncurses dist/athena
	rm -rf dist/main

build-test: build
	./generators/start.sh

build-test-ui: build-test
	./dist/athena

deps:
	pip install pyinstaller
	pip install cryptography
	pip install LnkParse3

clean:
	rm -rf build
	rm -rf dist
