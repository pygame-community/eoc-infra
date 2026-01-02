"""This file is a part of the source code for eoc.core.
This project has been licensed under the MIT license.

Copyright (c) 2025-present pygame-community
"""

__title__ = "eoc.core"
__author__ = "pygame-community"
__license__ = "MIT"
__copyright__ = "Copyright 2025-present pygame-community"
__version__ = "0.1.0"


import warelib
from warelib import ExceptionsConfig

from .exceptions import (
    AsyncTrialCallbackEnded,
    InvalidTrialStructure,
    TrialCallbackBegun,
    TrialCallbackEnded,
    TrialCallbackMustEnd,
    TrialCallbackNotBegun,
    TrialMustEnd,
)

warelib.init(
    exceptions_config=ExceptionsConfig(
        {
            "WareMustEnd": TrialMustEnd,
            "WareCallbackMustEnd": TrialCallbackMustEnd,
            "WareCallbackEnded": TrialCallbackEnded,
            "AsyncWareCallbackEnded": AsyncTrialCallbackEnded,
            "WareCallbackBegun": TrialCallbackBegun,
            "WareCallbackNotBegun": TrialCallbackNotBegun,
            "InvalidWareStructure": InvalidTrialStructure,
        }
    )
)

from .callbacks import *  # noqa: F403
from .trial import *  # noqa: F403
