from Model.BaseGameObjectModel import BaseGameObjectModel
from EventManager import *
import GameConfig

class ParachutistModel(BaseGameObjectModel):
    def __init__(self, eventManager, xPosition, yPosition, width, height):
        super().__init__(eventManager, xPosition, yPosition, width, height)
        self.reachdSeaLevel = False

    def notify(self, event):
        """
        Called by an event in the message queue.
        """
        # if isinstance(event, parachutistReachedSeaLevelEvent):
        #     self.eventManager.UnregisterListener(self)

        if isinstance(event, ParachutistReachedSeaLevelEvent):
            if self.xPosition == event.xPosition:
                self.eventManager.UnregisterListener(self)
        return

    def setReachedSeaLevel(self):
        self.reachdSeaLevel = True

    def getReachedSeaLevel(self):
        return self.reachdSeaLevel

    def setPosition(self, yNewPosition):
        if not (self.reachdSeaLevel):
            if yNewPosition >= GameConfig.surfaceHeight:
                self.eventManager.Post(ParachutistReachedSeaLevelEvent(self))
                self.eventManager.UnregisterListener(self)
            else:
                self.yPosition = yNewPosition
        return