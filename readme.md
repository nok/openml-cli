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

```bash
oml config {view, set, unset}
oml dataset {search, list, show, download}
```

## Examples

Configuration:

```bash
oml config view
oml config set --name apikey --value YOUR_APIKEY
```

Datasets:

```bash
oml dataset search <term>
oml dataset list
oml dataset list --limit <num> --offset <num>
oml dataset list --limit <num> --offset <num> --json
oml dataset show --id <num>
oml dataset show --id <num> --json
oml dataset show --id <num> --browser
oml dataset download --id <num>
```


## License

The module is Open Source Software released under the [MIT](license.txt) license.
