from collections.abc import Generator
from typing import Callable

import pygame
from warelib import WareCallback
from warelib.decorators import reset as ware_reset

from eoclib.callbacks import EOCWareMain, EOCWareSetup, EOCWareThumbnail
from eoclib.types import WareData


def setup(func: Callable[[WareData], None]) -> EOCWareSetup:
    return EOCWareSetup(func)


def thumbnail(
    func: Callable[
        ..., Generator[None, tuple[pygame.Surface, list[pygame.Event]], None]
    ],
) -> EOCWareThumbnail:
    return EOCWareThumbnail(func)


def mainloop(
    func: Callable[
        ..., Generator[None, tuple[pygame.Surface, list[pygame.Event]], None]
    ],
) -> EOCWareMain:
    return EOCWareMain(func)


def reset(func: Callable[[], None]) -> WareCallback[[], None]:
    return ware_reset(func)
