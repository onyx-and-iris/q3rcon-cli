import re

import clypi
from clypi import cprint


class Console:
    COLOUR_CODE_REGEX = re.compile(r'\^[0-9]')
    STATUS_PLAYER_REGEX = re.compile(
        r'^\s*(?P<slot>[0-9]+)\s+'
        r'(?P<score>[0-9-]+)\s+'
        r'(?P<ping>[0-9]+)\s+'
        r'(?P<guid>[0-9a-f]+)\s+'
        r'(?P<name>.*?)\s+'
        r'(?P<last>[0-9]+?)\s*'
        r'(?P<ip>(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}'
        r'(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])):?'
        r'(?P<port>-?[0-9]{1,5})\s*'
        r'(?P<qport>-?[0-9]{1,5})\s+'
        r'(?P<rate>[0-9]+)$',
        re.IGNORECASE | re.VERBOSE,
    )
    CVAR_REGEX = re.compile(
        r'^["](?P<name>[a-z_]+)["]\sis[:]\s'
        r'["](?P<value>.*?)["]\s'
        r'default[:]\s'
        r'["](?P<default>.*?)["]\s'
        r'info[:]\s'
        r'["](?P<info>.*?)["]$'
    )

    @staticmethod
    def remove_colour_codes(s: str) -> str:
        """Remove Quake 3 colour codes from a string."""
        return Console.COLOUR_CODE_REGEX.sub('', s)

    @staticmethod
    def print_response(response: str):
        response = Console.remove_colour_codes(response).removeprefix('print\n')

        cprint(f'\n{response}\n', fg='yellow')

    @staticmethod
    def print_status(response: str):
        _slots = []
        _scores = []
        _pings = []
        _guids = []
        _names = []
        _ips = []

        lines = response.splitlines()
        for line in lines:
            if m := Console.STATUS_PLAYER_REGEX.match(line):
                _slots.append(m.group('slot'))
                _scores.append(m.group('score'))
                _pings.append(m.group('ping'))
                _guids.append(m.group('guid'))
                _names.append(m.group('name'))
                _ips.append(m.group('ip'))

        if not _slots:
            cprint('\nNo players connected.\n', fg='yellow')
            return

        slots = clypi.boxed(_slots, title='Slot', width=15)
        scores = clypi.boxed(_scores, title='Score', width=15)
        pings = clypi.boxed(_pings, title='Ping', width=15)
        guids = clypi.boxed(_guids, title='GUID', width=40)
        names = clypi.boxed(_names, title='Name', width=30)
        ips = clypi.boxed(_ips, title='IP', width=30)
        print(f'\n{clypi.stack(slots, scores, pings, guids, names, ips, padding=0)}')

    @staticmethod
    def print_cvar(response: str):
        response = Console.remove_colour_codes(response).removeprefix('print\n')

        if m := Console.CVAR_REGEX.match(response):
            name = clypi.boxed(
                [m.group('name')], title='Name', width=max(len(m.group('name')) + 4, 30)
            )
            value = clypi.boxed(
                [m.group('value')],
                title='Value',
                width=max(len(m.group('value')) + 4, 30),
            )
            default = clypi.boxed(
                [m.group('default')],
                title='Default',
                width=max(len(m.group('default')) + 4, 30),
            )
            info = clypi.boxed(
                [m.group('info')], title='Info', width=max(len(m.group('info')) + 4, 30)
            )
            print(f'\n{clypi.stack(name, value, default, info, padding=0)}')
