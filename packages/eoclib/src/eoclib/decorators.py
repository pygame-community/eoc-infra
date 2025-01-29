from collections.abc import Generator
from typing import Callable

import pygame
from eoclib.callbacks import EOCWareMainloop, EOCWareSetup, EOCWareThumbnail
from eoclib.types import WareConfig, WareData


def setup(
    *args, **kwargs
) -> Callable[[Callable[[WareConfig, WareData], None]], EOCWareSetup]:
    def callback(func: Callable[[WareConfig, WareData], None]) -> EOCWareSetup:
        return EOCWareSetup(func)

    return callback


def thumbnail(
    *args, **kwargs
) -> Callable[
    [Callable[..., Generator[None, tuple[pygame.Surface, list[pygame.Event]], None]]],
    EOCWareThumbnail,
]:
    def callback(
        func: Callable[
            ..., Generator[None, tuple[pygame.Surface, list[pygame.Event]], None]
        ],
    ) -> EOCWareThumbnail:
        return EOCWareThumbnail(func)

    return callback


def mainloop(
    *args, **kwargs
) -> Callable[
    [Callable[..., Generator[None, tuple[pygame.Surface, list[pygame.Event]], None]]],
    EOCWareMainloop,
]:
    def callback(
        func: Callable[
            ..., Generator[None, tuple[pygame.Surface, list[pygame.Event]], None]
        ],
    ) -> EOCWareMainloop:
        return EOCWareMainloop(func)

    return callback
