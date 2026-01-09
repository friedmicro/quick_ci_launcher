build: clean
	pyinstaller ./generators/generator.py
	pyinstaller athena-ncurses.py
	pyinstaller athena-cli.py
	pyinstaller scan_games.py
	mv dist/athena-cli dist/athena
	mv dist/athena/athena-cli dist/athena/athena
	mv dist/scan_games dist/scanner
	mv dist/scanner/scan_games dist/scanner/scanner
	pyinstaller generators/combine.py
	pyinstaller generators/combine_partials.py

dev-ncurses:
	python3 athena-ncurses.py

dev-cli:
	python3 athena-cli.py

dev-scanner:
	python3 scan_games.py

dev-generator:
	python3 generators/generator.py

build-test: build
	./dist/generator/generator

build-test-ui: build-test
	./dist/athena/athena

virtual-env:
	pyenv install 3.13.7
	pyenv virtualenv 3.13.7 athena

deps:
	pip install pyinstaller
	pip install cryptography
	pip install LnkParse3

dep-windows: deps
	pip install windows-curses

clean:
	rm -rf build
	rm -rf dist
