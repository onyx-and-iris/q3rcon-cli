from aioq3rcon import Client
from clypi import Command, Spinner, arg
from typing_extensions import override

from q3rcon_cli import console


class Fastrestart(Command):
    """Executes a fast restart of the map."""

    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)

    @override
    async def run(self):
        async with Spinner('Executing fast restart', suffix='...'):
            async with Client(
                self.host,
                self.port,
                self.password,
                timeout=self.timeout,
                fragment_read_timeout=self.fragment_read_timeout,
            ) as client:
                response = await client.send_command(
                    'fast_restart', interpret=self.interpret
                )

        console.out.print_response(response)
