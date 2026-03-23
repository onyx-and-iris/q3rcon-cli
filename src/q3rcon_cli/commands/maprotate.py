from aioq3rcon import Client
from clypi import Command, Spinner, arg
from typing_extensions import override

from q3rcon_cli import console


class Maprotate(Command):
    """Rotates the map to the next one in the map rotation list."""

    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)

    @override
    async def run(self):
        async with Spinner('Rotating map', suffix='...'):
            async with Client(
                self.host,
                self.port,
                self.password,
                timeout=3,
                fragment_read_timeout=1,
            ) as client:
                response = await client.send_command('map_rotate', interpret=True)

        console.out.print_response(response)
