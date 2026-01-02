from collections.abc import Generator
from typing import Callable

import pygame
from warelib import WareCallback
from warelib.decorators import reset as ware_reset

from .callbacks import EOCTrialMain, EOCTrialSetup, EOCTrialThumbnail
from .types import TrialData


def setup(func: Callable[[TrialData], None]) -> EOCTrialSetup:
    return EOCTrialSetup(func)


def thumbnail(
    func: Callable[
        ..., Generator[None, tuple[pygame.Surface, list[pygame.Event]], None]
    ],
) -> EOCTrialThumbnail:
    return EOCTrialThumbnail(func)


def mainloop(
    func: Callable[
        ..., Generator[None, tuple[pygame.Surface, list[pygame.Event]], None]
    ],
) -> EOCTrialMain:
    return EOCTrialMain(func)


def reset(func: Callable[[], None]) -> WareCallback[[], None]:
    return ware_reset(func)
