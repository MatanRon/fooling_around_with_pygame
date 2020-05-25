from View.BaseGameObjectView import BaseGameObjectView
from EventManager import *
from GameConfig import *
import pygame
import os


class GameView(object):

    def __init__(self, eventManager, gameWindow, model):

        self.isinitialized = False
        self.eventManager = eventManager
        eventManager.RegisterListener(self)

        self.gameWindow = gameWindow
        self.model = model
        self.myfont = pygame.font.SysFont('Comic Sans MS', 20)

        self.background = self.loadImage('background.png')
        self.seaImage = self.loadImage('sea.png')

    def notify(self, event):

        if isinstance(event, InitializeEvent):
             self.initialize()

        if isinstance(event, TickEvent):
            currentScore = self.model.getScore()
            currentLifePoints = self.model.getLifePoints()
            self.updatePlayerStatusDisplay(currentScore, currentLifePoints)
            pass

        # if isinstance(event,onBoatLandingEvent) or isinstance(event,onWaterLandingEvent):
        #     currentScore = self.model.getScore()
        #     currentLifePoints = self.model.getLifePoints()
        #     self.updatePlayerStatusDisplay(currentScore, currentLifePoints)


    def updatePlayerStatusDisplay(self, currentScore, currentLifePoints):


        # boatImage = self.loadImage('boat.png')

        # self.gameWindow.blit(self.background, (0, 0))
        # self.gameWindow.blit(self.seaImage, (0, screenHight - 242)) # TODO: image sizes magic - export to function

        # updatedText = 'Score: ' + str(currentScore) + ' \n' + 'Life points : ' + str(currentLifePoints)
        # textsurface = self.myfont.render(updatedText, True, (0, 0, 0))
        # self.gameWindow.blit(textsurface, (0,  30))
        # pygame.display.update()

        scoreText = 'Score: ' + str(currentScore)
        textsurface = self.myfont.render(scoreText, True, (255, 255, 255))
        self.gameWindow.blit(textsurface, (0,  530))

        scoreText = 'Life Points: ' + str(currentLifePoints)
        textsurface = self.myfont.render(scoreText, True, (255, 255, 255))
        self.gameWindow.blit(textsurface, (0,  550))
        pygame.display.update()

    def loadImage(self, imageName):
        current_path = os.path.dirname(__file__)
        resource_path = os.path.join(current_path, 'resources')
        return pygame.image.load(os.path.join(resource_path, imageName))

    def renderall(self):

        # if not self.isinitialized:
        #     return


        background = self.loadImage('background.png')
        seaImage = self.loadImage('sea.png')
        # boatImage = self.loadImage('boat.png')

        self.window.blit(background, (0, 0))
        self.window.blit(seaImage, (0, GameConfig.screenHight - 242)) # TODO: image sizes magic - export to function
        # xCurrentPosition, yCurrentPosition = self.model.getPosition()
        # self.window.blit(boatImage, (xCurrentPosition, GameConfig.surfaceHeight))  # TODO: image sizes magic - export to function
        pygame.display.update()


    def initialize(self):
        if not (self.isinitialized):
            self.updatePlayerStatusDisplay(0, lifePoints)
            self.isinitialized = True
        return



