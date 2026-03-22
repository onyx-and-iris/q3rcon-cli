from aioq3rcon import Client
from clypi import Command, Positional, arg
from typing_extensions import override

from q3rcon_cli import console


class Hostname(Command):
    """Get or set the current hostname of the server."""

    new_hostname: Positional[str] = arg(
        help='The new hostname to change to (optional). If not provided, the current hostname will be printed.',
        default='',
    )
    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)

    @override
    async def run(self):
        if not self.new_hostname:
            async with Client(self.host, self.port, self.password) as client:
                if response := await client.send_command('sv_hostname'):
                    console.out.print_cvar(response)
            return

        async with Client(self.host, self.port, self.password) as client:
            await client.send_command(f'sv_hostname {self.new_hostname}')
            if response := await client.send_command('sv_hostname'):
                console.out.print_cvar(response)
