from aioq3rcon import Client
from clypi import Command, Positional, Spinner, arg
from typing_extensions import override

from q3rcon_cli import console


class Gametype(Command):
    """Get or set the current gametype of the server."""

    new_gametype: Positional[str] = arg(
        help='The new gametype to change to (optional). If not provided, the current gametype will be printed.',
        default='',
    )
    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)
    force: bool = arg(
        False,
        short='f',
        help='Whether to force the gametype change even if players are currently in the server.',
    )

    @override
    async def run(self):
        if not self.new_gametype:
            async with Spinner('Fetching current gametype', suffix='...'):
                async with Client(self.host, self.port, self.password) as client:
                    response = await client.send_command('g_gametype')
            console.out.print_cvar(response)
            return

        async with Spinner(f'Changing gametype to {self.new_gametype}', suffix='...'):
            async with Client(self.host, self.port, self.password) as client:
                await client.send_command(f'g_gametype {self.new_gametype}')

        if self.force:
            async with Spinner('Forcing gametype change', suffix='...'):
                async with Client(self.host, self.port, self.password) as client:
                    client.timeout = 3
                    client.fragment_read_timeout = 1
                    await client.send_command('map_restart')

        console.out.print(
            f'Gametype changed successfully to {self.new_gametype}.', style='green'
        )
