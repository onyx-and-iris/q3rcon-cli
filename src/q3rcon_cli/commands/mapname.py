from aioq3rcon import Client
from clypi import Command, arg
from typing_extensions import override

from q3rcon_cli.console import Console


class Mapname(Command):
    """Prints the current map name of the server."""

    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)

    @override
    async def run(self):
        async with Client(self.host, self.port, self.password) as client:
            if response := await client.send_command('mapname'):
                Console.print_cvar(response)
