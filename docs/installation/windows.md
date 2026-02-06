## Windows installation instructions

### Core Dependencies
* chocolatey (because that is easier than linking to a bunch of packages; feel free to install these however though [here](https://chocolatey.org/install))
* make (`choco install make`)
* python3 (Download through Windows store or preferably from the python website [here](https://www.python.org/downloads/windows/) as this will give you more control over the version)
* pip3 [here](https://pip.pypa.io/en/stable/installation)
* nodejs (for frontend only; `powershell -c "irm https://community.chocolatey.org/install.ps1|iex"`, `choco install nodejs --version="24.13.0"`...recommend looking at the website if this command breaks [here](https://nodejs.org/en/download))

### Optional Dependencies (for things like scanner functionality)
* sunshine (on remote machines): For a protocol to stream applications
* moonlight (on client): For a program to stream applications
* rdp client (on client): For connecting with RDP systems
* emulators: For testing emulator functionality

### Athena Dependencies
* Run: `make dep-windows`

### To be build everything as standalone binaries
Running git bash (your shell needs access to a few utilities not available in command prompt) `make build`.

### To run applications without building them:
* `make dev-ncurses`: Test the ncurses GUI
* `make dev-cli`: Test the CLI (you will need to pass parameters into this)
* `make dev-scanner`: Test the program scanner (you will likely need to build the generator binary if you change that)
* `make dev-generator`: Test the generator (you will likely need to have several temp folders created first)
* `make dev-api`: Test the REST API
* `make dev-npm-desktop-gui`: Test the electron GUI; note this executes slightly different from Linux because we are not running a dedicated binary rather we are using an npm package here.

### To build a single binary
Change any of the above tasks from `dev` to `build` and run them; ex: `make build-cli`. With noteable exception that you will need to run `build-desktop-gui` for the desktop GUI.
