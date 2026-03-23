# q3rcon-cli

[![Hatch project](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pypa/hatch/master/docs/assets/badge/v0.json)](https://github.com/pypa/hatch)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![PyPI - Version](https://img.shields.io/pypi/v/q3rcon-cli.svg)](https://pypi.org/project/q3rcon-cli)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/q3rcon-cli.svg)](https://pypi.org/project/q3rcon-cli)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

*with uv*

```console
uv tool install q3rcon-cli
```

*with pipx*

```console
pipx install q3rcon-cli
```

The CLI should now be discoverable as q3rcon-cli.

## Configuration

#### Flags

Pass `--host`, `--port` and `--password` as flags:

```console
q3rcon-cli --host=localhost --port=28960 --password=rconpassword
```

Additional Flags:

-   `--interactive`: Boolean flag, enable REPL mode.

#### Environment Variables

example .envrc:

```env
#!/usr/bin/env bash

export Q3RCON_CLI_HOST=localhost
export Q3RCON_CLI_PORT=28960
export Q3RCON_CLI_PASSWORD="<rcon password>"
```

## Use

```console
Usage: q3rcon-cli [OPTIONS] COMMAND

┏━ Subcommands ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ fastrestart  Executes a fast restart of the server                                               ┃
┃ gametype     Get or set the current gametype of the server                                       ┃
┃ hostname     Get or set the current hostname of the server                                       ┃
┃ map          Get the current map or change to a new one                                          ┃
┃ mapname      Prints the current map name of the server                                           ┃
┃ maprestart   Restarts the current map                                                            ┃
┃ maprotate    Rotates the map to the next one in the map rotation list                            ┃
┃ plugins      Prints the currently loaded plugins of the server                                   ┃
┃ status       Prints the status of the server                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━ Options ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ -i, --interactive   Whether to start in interactive mode (defaults to false)                     ┃
┃ -v, --version       Show the version and exit                                                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━ Connection options ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ -h, --host <HOST>          The host to connect to                                                ┃
┃ -p, --port <PORT>          The port to connect to                                                ┃
┃ -P, --password <PASSWORD>  The password for authentication                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Special Thanks

- [lapetus-11](https://github.com/Iapetus-11) for writing the [aio-q3-rcon](https://github.com/Iapetus-11/aio-q3-rcon) package.
- [Daniel Melchor](https://github.com/danimelchor) for creating the wonderful [clypi](https://github.com/danimelchor/clypi) library.

## License

`q3rcon-cli` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
