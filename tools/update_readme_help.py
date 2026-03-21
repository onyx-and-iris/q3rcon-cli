#!/usr/bin/env python3
import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
README_PATH = REPO_ROOT / 'README.md'
HELP_CMD = ['hatch', 'run', 'q3rcon-cli', '--help']


def get_help_output():
    result = subprocess.run(HELP_CMD, capture_output=True, text=True, check=True)
    output = result.stdout.strip()
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    output = ansi_escape.sub('', output)
    return output


def update_readme(help_text):
    readme = README_PATH.read_text()

    pattern = re.compile(
        r'```console\nUsage: q3rcon-cli \[OPTIONS\] COMMAND.*?```', re.DOTALL
    )
    new_block = f'```console\n{help_text}\n```'
    new_readme, n = pattern.subn(new_block, readme, count=1)
    if n == 0:
        raise RuntimeError(
            'Could not find the q3rcon-cli usage console block to replace in README.md'
        )
    README_PATH.write_text(new_readme)
    print('README.md updated with latest --help output.')


def main():
    help_text = get_help_output()
    update_readme(help_text)


if __name__ == '__main__':
    main()
