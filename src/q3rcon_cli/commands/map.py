from aioq3rcon import Client
from clypi import Command, Positional, Spinner, arg
from typing_extensions import override

from q3rcon_cli.console import Console


class Map(Command):
    """Get the current map or change to a new one."""

    new_map: Positional[str] = arg(
        help='The new map to change to (optional). If not provided, the current map will be printed.',
        default='',
    )
    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)

    @override
    async def run(self):
        if not self.new_map:
            async with Client(self.host, self.port, self.password) as client:
                if response := await client.send_command('mapname'):
                    Console.print_cvar(response)
            return

        async with Spinner('Changing map...'):
            async with Client(
                self.host, self.port, self.password, fragment_read_timeout=1
            ) as client:
                await client.send_command(f'map mp_{self.new_map.removeprefix("mp_")}')
                if response := await client.send_command('mapname'):
                    Console.print_cvar(response)
