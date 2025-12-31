from warelib.exceptions import (
    WareMustEnd,
    WareCallbackMustEnd,
    WareCallbackBegun,
    WareCallbackNotBegun,
    WareCallbackEnded,
    AsyncWareCallbackEnded,
)


class TrialMustEnd(WareMustEnd):
    """Exception raised when an entire trial is requested to end"""


class TrialCallbackMustEnd(WareCallbackMustEnd):
    """Exception raised when a trial callback is requested to end"""


class TrialCallbackEnded(WareCallbackEnded):
    """Exception raised when a trial callback has ended"""


class AsyncTrialCallbackEnded(AsyncWareCallbackEnded):
    """Exception raised when an async trial callback has ended"""


class TrialCallbackBegun(WareCallbackBegun):
    """Exception raised when a trial callback has already begun a generator"""


class TrialCallbackNotBegun(WareCallbackNotBegun):
    """Exception raised when a trial callback has not begun a generator"""


class InvalidTrialStructure(ValueError):
    """Exception raised when a trial module structure is invalid"""
