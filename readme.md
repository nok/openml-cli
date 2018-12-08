# openml-cli

Use the command line tool `oml` to interact with the official [API](https://openml.github.io/OpenML/REST-API/) of [OpenML](https://www.openml.org).


## Installation

```bash
$ pip install openml-cli
```

If you want the [latest changes](changelog.md), you can install the package from the [master](https://github.com/nok/openml-cli/tree/master) branch:

```bash
$ pip uninstall -y openml-cli
$ pip install --no-cache-dir https://github.com/nok/openml-cli/zipball/master
```


## Usage

<details>
    <summary><code>oml config {view, set, unset}</code></summary>
<br>

Description: List or edit the configuration.

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


## License

The module is Open Source Software released under the [MIT](license.txt) license.
