from aioq3rcon import Client
from clypi import Command, Spinner, arg
from typing_extensions import override

from q3rcon_cli import console


class Maprestart(Command):
    """Restarts the current map."""

    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)

    @override
    async def run(self):
        async with Spinner('Restarting map...'):
            async with Client(
                self.host, self.port, self.password, fragment_read_timeout=1
            ) as client:
                if response := await client.send_command('map_restart'):
                    console.out.print_response(response)
