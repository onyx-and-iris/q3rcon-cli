from collections import UserDict


class Config(UserDict):
    DEFAULT_TIMEOUT: int = 2
    DEFAULT_FRAGMENT_READ_TIMEOUT: float = 0.25

    def __init__(self):
        self.data = {
            'status': (2, 0.25, False),
            'fast_restart': (3, 1, True),
            'map_restart': (3, 1, True),
            'map': (3, 1, True),
            'map_rotate': (3, 1, True),
        }

    def __getitem__(self, key):
        return self.data.get(
            key, (self.DEFAULT_TIMEOUT, self.DEFAULT_FRAGMENT_READ_TIMEOUT, False)
        )


_config = Config()


def get(key: str):
    match key:
        case 'fast_restart' | 'fastrestart':
            return _config['fast_restart']
        case 'map_restart' | 'maprestart':
            return _config['map_restart']
        case 'map_rotate' | 'maprotate':
            return _config['map_rotate']
        case _:
            return _config[key]
