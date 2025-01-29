from typing import TypedDict

from eoc.lib.callbacks import EOCWareMainloop, EOCWareSetup, EOCWareThumbnail


class WareConfig(TypedDict):
    pass


class WareData(TypedDict):
    pass


class EOCWareGlobals(TypedDict):
    data: WareData


class EOCWareCallbacks(TypedDict):
    setup: EOCWareSetup
    thumbnail: EOCWareThumbnail
    mainloop: EOCWareMainloop
