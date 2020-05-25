from Model.BoatModel import BoatModel
from Controller.BaseGameObjectController import BaseGameObjectController
from EventManager import *
import pygame
import GameConfig



class BoatController(BaseGameObjectController):
    def __init__(self, eventManager, boatModel):
        super().__init__(eventManager, boatModel)

    def moveLeft(self, xCurrentPosition):
        if xCurrentPosition > -30:
            self.model.setPosition(xCurrentPosition - self.model.getSpeed())

    def moveRight(self, xCurrentPosition):
        if xCurrentPosition < GameConfig.screenWidth - GameConfig.gameSpeed :
            self.model.setPosition(xCurrentPosition + self.model.getSpeed())

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        if isinstance(event, TickEvent):

            pygame.event.get()

            keys = pygame.key.get_pressed()
            xCurrentPosition, yCurrentPosition = self.model.getPosition()

            if keys[pygame.K_LEFT]:
                 self.moveLeft(xCurrentPosition)

            if keys[pygame.K_RIGHT]:
                self.moveRight(xCurrentPosition)

            return




if __name__ == '__main__':
    pass