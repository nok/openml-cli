# openml-cli

[![PyPI](https://img.shields.io/pypi/v/openml-cli.svg)](https://pypi.python.org/pypi/openml-cli)
[![PyPI](https://img.shields.io/pypi/pyversions/openml-cli.svg)](https://pypi.python.org/pypi/openml-cli)
[![GitHub license](https://img.shields.io/pypi/l/openml-cli.svg)](https://raw.githubusercontent.com/nok/openml-cli/master/license.txt)
[![Twitter](https://img.shields.io/twitter/follow/darius_morawiec.svg?label=follow&style=popout)](https://twitter.com/darius_morawiec)

Use the command line tool `oml` or `openml` to interact with the official [API](https://openml.github.io/OpenML/REST-API/) of [OpenML](https://www.openml.org).


## Installation

```bash
pip install openml-cli
```


## Usage

<details>
    <summary><code>oml config {view, set, unset}</code></summary>
<br>

Description: View or change your configuration.

Subcommands:

```bash
oml config view
oml config set <name> <value>
oml config unset <name>
```

Examples:

```bash
oml config set apikey <your_apikey>
```

</details>

<details>
    <summary><code>oml dataset {search, show, download, list}</code></summary>
<br>

Description: Search, filter or download datasets.

Subcommands:

```bash
oml dataset search <term>
oml dataset show <id>
oml dataset show <id> --json
oml dataset show <id> --browser
oml dataset download <id>
oml dataset list
oml dataset list --limit <num> --offset <num>
oml dataset list --limit <num> --offset <num> --json
```

Search and download a specific dataset:

```bash
oml dataset search mnist
oml dataset show 40996
oml dataset download 40996 --to ~/Downloads
```

</details>


## Example

```bash
oml config set apikey <your_apikey>
oml dataset search mnist
oml dataset show 40996
oml dataset download 40996 --to ~/Downloads
```


## License

The module is Open Source Software released under the [MIT](license.txt) license.
