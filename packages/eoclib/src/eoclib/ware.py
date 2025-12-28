from typing import TypedDict
from eoclib.callbacks import EOCWareSetup, EOCWareThumbnail, EOCWareMain, EOCWareReset
from eoclib.types import WareData
from warelib import Ware


class EOCWareGlobals(TypedDict):
    data: WareData


class EOCWareCallbacks(TypedDict):
    setup: EOCWareSetup
    thumbnail: EOCWareThumbnail
    mainloop: EOCWareMain
    reset: EOCWareReset


class EOCWare(Ware[EOCWareGlobals, EOCWareCallbacks]):
    pass
