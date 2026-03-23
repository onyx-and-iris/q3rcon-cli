from aioq3rcon import Client
from clypi import Command, Spinner, arg
from typing_extensions import override

from q3rcon_cli import console


class Fastrestart(Command):
    """Executes a fast restart of the server."""

    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)

    @override
    async def run(self):
        async with Spinner('Executing fast restart', suffix='...'):
            async with Client(self.host, self.port, self.password) as client:
                response = await client.send_command('fast_restart', interpret=True)

        console.out.print_response(response)
