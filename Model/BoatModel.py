from Model.BaseGameObjectModel import BaseGameObjectModel

class BoatModel(BaseGameObjectModel):
    def __init__(self, eventManager, xPosition, yPosition, width, height):
        super().__init__(eventManager, xPosition, yPosition, width, height)

    def notify(self, event):
        """
        Called by an event in the message queue.
        """

    def setPosition(self, xNewPosition):
        self.xPosition = xNewPosition

    #def getPosition(self):
    #   return self.xPosition