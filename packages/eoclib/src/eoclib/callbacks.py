import pygame
from warelib.ware_callbacks import GeneratorWareCallback, WareCallback

from eoclib.types import WareConfig, WareData


class EOCWareSetup(WareCallback[[WareConfig, WareData], None]):
    pass


class EOCWareThumbnail(
    GeneratorWareCallback[[], None, tuple[pygame.Surface, list[pygame.Event]], None]
):
    pass


class EOCWareMainloop(
    GeneratorWareCallback[[], None, tuple[pygame.Surface, list[pygame.Event]], None]
):
    pass
