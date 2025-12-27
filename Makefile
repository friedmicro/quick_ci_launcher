build: clean
	pyinstaller athena-ncurses.py
	pyinstaller scan_games.py
	mv dist/athena-ncurses dist/athena
	mv dist/athena/athena-ncurses dist/athena/athena
	mv dist/scan_games dist/scanner
	mv dist/scanner/scan_games dist/scanner/scanner
	pyinstaller generators/combine.py
	pyinstaller generators/combine_partials.py

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
