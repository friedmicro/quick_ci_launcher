## MacOS installation instructions

### Core Dependencies
* make (install through xcode with: `xcode -select --install`)
* pip3 [here](https://pip.pypa.io/en/stable/installation)
* pyenv (see instructions [here](https://github.com/pyenv/pyenv#installation))
* virtualenv (see instructions [here](https://virtualenv.pypa.io/en/latest/installation.html))
* nodejs (for frontend only; recommended install through nvm [here](https://github.com/nvm-sh/nvm#installing-and-updating))

#### If on an M1 Mac and you plan to work on the frontend GUI
* Install Rosetta 2: `softwareupdate --install-rosetta`

### Optional Dependencies (for things like scanner functionality)
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
* `make dev-npm-desktop-gui`: Test the electron GUI; note this executes slightly different from Linux because we are not running a dedicated binary rather we are using an npm package here.

### To build a single binary
Change any of the above tasks from `dev` to `build` and run them; ex: `make build-cli`. With noteable exception that you will need to run `build-desktop-gui` for the desktop GUI.
