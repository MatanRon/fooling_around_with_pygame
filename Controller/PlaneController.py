from Model.PlaneModel import PlaneModel
from Controller.BaseGameObjectController import BaseGameObjectController
from EventManager import *
import pygame
import GameConfig



class PlaneController(BaseGameObjectController):
    def __init__(self, eventManager, boatModel):
        super().__init__(eventManager, boatModel)

    def fly(self, xCurrentPosition):
        if xCurrentPosition <= 0 - self.model.getWidth():
            self.model.setPosition(GameConfig.screenWidth)
        else:
            self.model.setPosition(xCurrentPosition - self.model.getSpeed())
        return

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        if isinstance(event, TickEvent):
            xCurrentPosition = self.model.getPosition()[0]
            self.fly(xCurrentPosition)

        return




if __name__ == '__main__':
    pass