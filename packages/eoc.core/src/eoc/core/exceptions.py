from warelib.exceptions import (
    AsyncWareCallbackEnded,
    WareCallbackBegun,
    WareCallbackEnded,
    WareCallbackMustEnd,
    WareCallbackNotBegun,
    WareMustEnd,
)


class TrialMustEnd(WareMustEnd):
    """Exception raised when an entire trial is requested to end"""


EOCTrialMustEnd = TrialMustEnd


class TrialCallbackMustEnd(WareCallbackMustEnd):
    """Exception raised when a trial callback is requested to end"""


EOCTrialCallbackMustEnd = TrialCallbackMustEnd


class TrialCallbackEnded(WareCallbackEnded):
    """Exception raised when a trial callback has ended"""


EOCTrialCallbackEnded = TrialCallbackEnded


class AsyncTrialCallbackEnded(AsyncWareCallbackEnded):
    """Exception raised when an async trial callback has ended"""


EOCAsyncTrialCallbackEnded = AsyncTrialCallbackEnded


class TrialCallbackBegun(WareCallbackBegun):
    """Exception raised when a trial callback has already begun a generator"""


EOCTrialCallbackBegun = TrialCallbackBegun


class TrialCallbackNotBegun(WareCallbackNotBegun):
    """Exception raised when a trial callback has not begun a generator"""


EOCTrialCallbackNotBegun = TrialCallbackNotBegun


class InvalidTrialStructure(ValueError):
    """Exception raised when a trial module structure is invalid"""


InvalidEOCTrialStructure = InvalidTrialStructure
