import pygame
from warelib.callbacks import GeneratorWareCallback, WareCallback

from eoclib.types import WareData


class EOCWareSetup(WareCallback[[WareData], None]):
    pass


class EOCWareThumbnail(
    GeneratorWareCallback[[], None, tuple[pygame.Surface, list[pygame.Event]], None]
):
    pass


class EOCWareMain(
    GeneratorWareCallback[[], None, tuple[pygame.Surface, list[pygame.Event]], None]
):
    pass


class EOCWareReset(WareCallback[[], None]):
    pass
