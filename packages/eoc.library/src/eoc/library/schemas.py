from collections.abc import Mapping
from typing import Any, TypedDict

from .callbacks import EOCWareMain, EOCWareReset, EOCWareSetup, EOCWareThumbnail
from .types import WareData


class EOCWareLayout(TypedDict):
    data: type[WareData]
    setup: type[EOCWareSetup]
    thumbnail: type[EOCWareThumbnail]
    mainloop: type[EOCWareMain]
    reset: type[EOCWareReset]


eoc_globals_callbacks_schema: EOCWareLayout = {
    "data": Mapping[str, Any],
    "setup": EOCWareSetup,
    "thumbnail": EOCWareThumbnail,
    "mainloop": EOCWareMain,
    "reset": EOCWareReset,
}
