import clypi
from aioq3rcon import Client, IncorrectPasswordError
from clypi import Command, Spinner, arg
from clypi import parsers as cp
from typing_extensions import override

from . import console
from .__about__ import __version__
from .commands import (
    Fastrestart,
    Gametype,
    Hostname,
    Map,
    Mapname,
    Maprestart,
    Maprotate,
    Plugins,
    Status,
)

Subcommands = (
    Fastrestart
    | Gametype
    | Hostname
    | Map
    | Mapname
    | Maprestart
    | Maprotate
    | Plugins
    | Status
)


class Q3rconCli(Command):
    subcommand: Subcommands | None = None
    host: str = arg(
        'localhost',
        short='h',
        help='The host to connect to',
        env='Q3RCON_CLI_HOST',
        group='Connection',
        parser=cp.Str(min=1),
    )
    port: int = arg(
        28960,
        short='p',
        help='The port to connect to',
        env='Q3RCON_CLI_PORT',
        group='Connection',
        parser=cp.Int(min=1, max=65535),
    )
    password: str = arg(
        '',
        short='P',
        help='The password for authentication',
        env='Q3RCON_CLI_PASSWORD',
        group='Connection',
        parser=cp.Str(min=8),
    )
    interactive: bool = arg(
        False,
        short='i',
        help='Whether to start in interactive mode (defaults to false)',
    )
    version: bool = arg(
        False,
        short='v',
        help='Show the version and exit',
    )

    @override
    async def run(self):
        if self.version:
            print(f'q3rcon-cli version: {clypi.style(__version__, fg="green")}')
            return

        if self.interactive:
            await self.run_interactive()
        else:
            await Status(self.host, self.port, self.password).run()

    async def run_interactive(self):
        print(
            clypi.style('Entering interactive mode. Type', fg='blue'),
            clypi.style("'Q'", fg='yellow'),
            clypi.style('to quit.', fg='blue'),
        )

        CMD_CONFIG = {
            'status': (2, 1, False),
            'fast_restart': (3, 1, True),
            'map_restart': (3, 1, True),
            'map': (3, 1, True),
            'map_rotate': (3, 1, True),
        }
        DEFAULT_TIMEOUT = 2
        DEFAULT_FRAGMENT_READ_TIMEOUT = 0.25
        while command := input(clypi.style('cmd: ', fg='green')):
            if command.lower() == 'q':
                break

            timeout, fragment_read_timeout, interpret = CMD_CONFIG.get(
                command.split()[0].lower(),
                (DEFAULT_TIMEOUT, DEFAULT_FRAGMENT_READ_TIMEOUT, False),
            )

            async with Spinner(f"Sending command: '{command}'", suffix='...'):
                async with Client(
                    self.host,
                    self.port,
                    self.password,
                    timeout=timeout,
                    fragment_read_timeout=fragment_read_timeout,
                ) as client:
                    try:
                        response = await client.send_command(
                            command, interpret=interpret
                        )
                    except TimeoutError:
                        console.err.print(
                            f"Timeout waiting for response for command: '{command}'"
                        )

            console.out.print_response(response)


def main():
    try:
        cli = Q3rconCli().parse()
        cli.start()
    except IncorrectPasswordError:
        console.err.print('Incorrect password provided.')
    except TimeoutError:
        console.err.print(
            f"Timeout waiting for response for command: '{type(cli.subcommand).__name__.lower()}'"
        )
