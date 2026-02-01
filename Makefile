REMOTE_USER = ${ATHENA_REMOTE_USER}
REMOTE_IP = ${ATHENA_REMOTE_IP}
REMOTE_PATH = ${ATHENA_REMOTE_PATH}

build: clean
	pyinstaller generator.py
	pyinstaller athena-ncurses.py
	pyinstaller athena-cli.py
	pyinstaller scan_games.py
	pyinstaller athena-daemon.py
	pyinstaller combine.py
	pyinstaller combine_partials.py
	pyinstaller athena-client-daemon.py
	pyinstaller athena-api.py
	mv dist/athena-cli dist/athena
	mv dist/athena/athena-cli dist/athena/athena
	mv dist/scan_games dist/scanner
	mv dist/scanner/scan_games dist/scanner/scanner

dev-ncurses:
	python3 athena-ncurses.py

dev-cli:
	python3 athena-cli.py

dev-scanner:
	python3 scan_games.py

dev-generator:
	python3 generators/generator.py

dev-api:
	python3 athena-api.py

build-test: build
	./dist/generator/generator

build-test-ui: build-test
	./dist/athena/athena

build-test-daemon:
	cp daemon/config.json dist/
	cp initial_config.bin dist/

build-test-unix-daemon: build-test
	ssh -t -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${REMOTE_USER}@${REMOTE_IP} "sudo rm -rf ${REMOTE_PATH}; sudo mkdir ${REMOTE_PATH}"
	ssh -t -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${REMOTE_USER}@${REMOTE_IP} "sudo chown -R ${REMOTE_USER}:${REMOTE_USER} ${REMOTE_PATH}"
	scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -r dist/* ${REMOTE_USER}@${REMOTE_IP}:${REMOTE_PATH}
	ssh -t -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${REMOTE_USER}@${REMOTE_IP} "sudo systemctl restart athena"

virtual-env:
	pyenv install 3.13.7
	pyenv virtualenv 3.13.7 athena

deps:
	pip install pyinstaller
	pip install cryptography
	pip install LnkParse3
	pip install flask

dep-windows: deps
	pip install windows-curses

clean:
	rm -rf build
	rm -rf dist
