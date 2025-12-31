from typing import TypedDict

from warelib import Ware

from .callbacks import EOCTrialMain, EOCTrialReset, EOCTrialSetup, EOCTrialThumbnail
from .types import TrialData


class EOCTrialGlobals(TypedDict):
    data: TrialData


class EOCTrialCallbacks(TypedDict):
    setup: EOCTrialSetup
    thumbnail: EOCTrialThumbnail
    mainloop: EOCTrialMain
    reset: EOCTrialReset


class EOCTrial(Ware[EOCTrialGlobals, EOCTrialCallbacks]):
    pass
