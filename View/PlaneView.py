from View.BaseGameObjectView import BaseGameObjectView
from EventManager import *
import GameConfig
import pygame


class PlaneView(BaseGameObjectView):

    def __init__(self, eventManager, model, window):
        super().__init__(eventManager,model, window)


    def notify(self, event):

        if isinstance(event, InitializeEvent):
            self.initialize()

        if isinstance(event, TickEvent):
            self.renderall()


    def renderall(self):

        if not self.isinitialized:
            return

        planeImage = self.loadImage('plane.png')

        xCurrentPosition, yCurrentPosition = self.model.getPosition()
        self.window.blit(planeImage, (xCurrentPosition, yCurrentPosition))
        pygame.display.update()






