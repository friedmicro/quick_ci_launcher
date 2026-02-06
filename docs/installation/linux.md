## Linux installation instructions

### Core Dependencies
* make (recommended install through your package manager)
* python3 (recommended install through your package manager)
* pip3 (recommended install through your package manager)
* pyenv (see instructions [here](https://github.com/pyenv/pyenv#installation))
* virtualenv (see instructions [here](https://virtualenv.pypa.io/en/latest/installation.html))
* nodejs (for frontend only; recommended install through nvm [here](https://github.com/nvm-sh/nvm#installing-and-updating))
* electron (for frontend only; recommended install through your package manager)
* zip (for bundling electron only; recommended install through your package manager)

### Optional Dependencies (for things like scanner functionality)
* waydroid: For android support
* sunshine (on remote machines): For a protocol to stream applications
* moonlight (on client): For a program to stream applications
* rdp client (on client): For connecting with RDP systems
* emulators: For testing emulator functionality

### Athena Dependencies
* Run `make virtual-env`
* Run: `pyenv activate athena`
* Run: `make deps`

### To be build everything as standalone binaries
`make build`

### To run applications without building them:
* `make dev-ncurses`: Test the ncurses GUI
* `make dev-cli`: Test the CLI (you will need to pass parameters into this)
* `make dev-scanner`: Test the program scanner (you will likely need to build the generator binary if you change that)
* `make dev-generator`: Test the generator (you will likely need to have several temp folders created first)
* `make dev-api`: Test the REST API
* `make dev-desktop-gui`: Test the electron GUI without building it

### To build a single binary
Change any of the above tasks from `dev` to `build` and run them; ex: `make build-cli`.
