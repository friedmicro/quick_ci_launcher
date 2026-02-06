## Contributing

### Development Environment Setup
Please setup your environment according the installation guide for your respective OS. Please do note that at this time Windows, MacOS, and Linux are supported.

### Code Contribution Guidelines
* In general we largely follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
* For what this doesn't cover, please refer to the [PEP 8 Style Guide](https://peps.python.org/pep-0008/).
* Otherwise, assume general best practices.
* New code should have tests (if application)

### PR Guidelines
* Keep PRs small and atomic (a PR should not be stable irrespective of when it is merged)
* PR should be descriptive and include a clear description of the changes made.

### Types of contributions accepted
* Planned features: please see the end of this document for a list of what is currently planned
* Bug fixes: assuming these do not break existing functionality (we track issues in Github issues, feel free to take a look)
* Performance improvements: are always welcome assuming they don't sacrifice readability or maintainability beyond what is reasonable.
* Documentation fixes\improvements: are always welcome

### Types of contributions not accepted
* Breaking changes to existing public APIs: this includes rest APIs, CLI interfaces, utility libraries, data models, and config settings.
* Untested or highly brittle features: if a feature cannot be reliably enabled it won't be loaded into the application. Exceptions to this are if the feature if being broken across multiple PRs.
* Unplanned features: we do want to include features that do not match the scope of project; if you would like to have a feature added to the planned features list, please open an issue so the maintainers can discuss it.

### Planned Features
* Configuration GUI: A graphical user interface for managing configuration settings.
* Launcher GUI: A GUI interface for automatically launching applications (currently we have ncurses)
* Unit tests for the code: There are currently no unit tests for the codebase due to this starting as a personal project years ago. For long term maintainability we need to change this.
* Integration tests for the code: There are currently no integration tests, these are necessary due to the number of components we have
* More robust error handling: Athena is designed to fail fast and provide tools for recovery. The error messages could use some improvement
* Cut down package size: Currently each binary includes all dependencies locally linked. We're doing this for portability\convience, but it does bloat the package size a fair amount.

### Areas in need of maintainers\assistance
* Dedicated package maintainers for various Linux distributions. If you are interested please open an issue to reach out.
