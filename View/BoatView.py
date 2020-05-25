from View.BaseGameObjectView import BaseGameObjectView
from EventManager import *
import GameConfig
import pygame


class BoatView(BaseGameObjectView):

    def __init__(self, eventManager, model, window):
        super().__init__(eventManager,model, window)


    def notify(self, event):

        if isinstance(event, InitializeEvent):
            self.initialize()

        if isinstance(event, TickEvent):
            self.renderall()

        # if isinstance(event,onBoatLandingEvent):
        #     self.score += successScore
        #
        # if isinstance(event,onWaterLandingEvent):
        #     self.lifePoints -= 1
        #     if 0 == self.lifePoints:
        #         print ('No more life points - Game Over')
        #         self.eventManager.Post(QuitEvent())


    def renderall(self):

        if not self.isinitialized:
            return

        # clear display
        # self.window.fill((255, 255, 255))

        # a little hack here - For the sake of game image display continuity,\
        # background and sea display under the boatView's responsibility instead of the gameView's responsibility.
        # In an ideal situation I would pass it there
        background = self.loadImage('background.png')
        seaImage = self.loadImage('sea.png')
        boatImage = self.loadImage('boat.png')

        self.window.blit(background, (0, 0))
        self.window.blit(seaImage, (0, GameConfig.screenHight - 242)) # TODO: image sizes magic - export to function
        xCurrentPosition, yCurrentPosition = self.model.getPosition()
        self.window.blit(boatImage, (xCurrentPosition, GameConfig.surfaceHeight))  # TODO: image sizes magic - export to function
        pygame.display.update()






