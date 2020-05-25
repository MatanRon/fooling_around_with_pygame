from View.BaseGameObjectView import BaseGameObjectView
from EventManager import *
import GameConfig
import pygame


class ParachutistView(BaseGameObjectView):

    def __init__(self, eventManager, model, window):
        super().__init__(eventManager, model, window)
        self.image = self.loadImage('pocahontasdiving3.png')

    def notify(self, event):

        if isinstance(event, InitializeEvent):
            self.initialize()

        if isinstance(event, TickEvent):
            self.renderall()

        if isinstance(event, ParachutistReachedSeaLevelEvent):
            position = self.model.getPosition()
            if position[0] == event.xPosition:
                self.eventManager.UnregisterListener(self)


    def renderall(self):

        if not self.isinitialized:
            return

        if self.model.getReachedSeaLevel():
            self.eventManager.UnregisterListener(self)
            return

        xCurrentPosition, yCurrentPosition = self.model.getPosition()
        self.window.blit(self.image, (xCurrentPosition, yCurrentPosition))
        pygame.display.update()

        return
