from aioq3rcon import Client
from clypi import Command, Spinner, arg
from typing_extensions import override

from q3rcon_cli import config, console


class Maprestart(Command):
    """Restarts the current map."""

    host: str = arg(inherited=True)
    port: int = arg(inherited=True)
    password: str = arg(inherited=True)

    @classmethod
    def with_configure(cls, host, port, password):
        """Configures the command with the appropriate configuration and runs it.


        This classmethod is used if we invoke the maprestart command from another command (e.g. gametype),
        since the pre_run_hook is not called in that case.
        """
        instance = cls(host, port, password)
        (
            instance.timeout,
            instance.fragment_read_timeout,
            instance.interpret,
        ) = config.get(instance.prog().split()[0].lower())
        return instance

    @override
    async def run(self):
        async with Spinner('Restarting map', suffix='...'):
            async with Client(
                self.host,
                self.port,
                self.password,
                timeout=self.timeout,
                fragment_read_timeout=self.fragment_read_timeout,
            ) as client:
                response = await client.send_command(
                    'map_restart', interpret=self.interpret
                )

        console.out.print_response(response)
