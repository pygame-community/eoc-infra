from collections.abc import MutableMapping
from typing import Any, TypedDict

from .callbacks import EOCTrialMain, EOCTrialReset, EOCTrialSetup, EOCTrialThumbnail
from .types import TrialData


class EOCTrialLayout(TypedDict):
    data: type[TrialData]
    setup: type[EOCTrialSetup]
    thumbnail: type[EOCTrialThumbnail]
    mainloop: type[EOCTrialMain]
    reset: type[EOCTrialReset]


eoc_globals_callbacks_schema: EOCTrialLayout = {
    "data": MutableMapping[str, Any],
    "setup": EOCTrialSetup,
    "thumbnail": EOCTrialThumbnail,
    "mainloop": EOCTrialMain,
    "reset": EOCTrialReset,
}
