import pygame
from warelib.callbacks import GeneratorWareCallback, WareCallback

from .types import TrialData


class EOCTrialSetup(WareCallback[[TrialData], None]):
    pass


class EOCTrialThumbnail(
    GeneratorWareCallback[[], None, tuple[pygame.Surface, list[pygame.Event]], None]
):
    pass


class EOCTrialMain(
    GeneratorWareCallback[[], None, tuple[pygame.Surface, list[pygame.Event]], None]
):
    pass


class EOCTrialReset(WareCallback[[], None]):
    pass
