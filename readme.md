# openml-cli

Use the application `openml` on the command line to interact with the official [API](https://openml.github.io/OpenML/REST-API/) of [OpenML](https://www.openml.org) directly.


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
oml dataset {list, show, download}
```

## Examples

Configuration:

```bash
oml config view
oml config set --name apikey --value YOUR_APIKEY
```

Datasets:

```bash
oml dataset list
oml dataset list --limit 5 --offset 10
oml dataset list --limit 5 --offset 10 --json
oml dataset show --id 1
oml dataset show --id 1 --json
oml dataset show --id 1 --browser
```


## License

The module is Open Source Software released under the [MIT](license.txt) license.
