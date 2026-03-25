from .fastrestart import Fastrestart
from .gametype import Gametype
from .hostname import Hostname
from .map import Map
from .mapname import Mapname
from .maprestart import Maprestart
from .maprotate import Maprotate
from .plugins import Plugins
from .status import Status

Subcommands = (
    Fastrestart
    | Gametype
    | Hostname
    | Map
    | Mapname
    | Maprestart
    | Maprotate
    | Plugins
    | Status
)
