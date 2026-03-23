from aioq3rcon import Client
from clypi import Command, Spinner, arg
from typing_extensions import override

from q3rcon_cli import console


class Status(Command):
    """Prints the status of the server."""

    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)

    @override
    async def run(self):
        async with Spinner('Fetching status', suffix='...'):
            async with Client(
                self.host, self.port, self.password, fragment_read_timeout=1
            ) as client:
                response = await client.send_command('status')

        console.out.print_status(response)
