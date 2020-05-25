from Model.ParachutistModel import ParachutistModel
from Controller.BaseGameObjectController import BaseGameObjectController
from EventManager import *
import GameConfig



class ParachutistController(BaseGameObjectController):
    def __init__(self, eventManager, parachutistModel):
        super().__init__(eventManager, parachutistModel)


    def descent (self):
        xCurrentPosition, yCurrentPosition = self.model.getPosition()
        self.model.setPosition(yCurrentPosition + self.model.getSpeed())
        return

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        if self.model.getReachedSeaLevel():
            return

        if isinstance(event, TickEvent):
            #if not(self.model.getReachedSeaLevel()):
            self.descent()


        # if isinstance(event, parachutistReachedSeaLevelEvent):
        #     # if not (self.model.getReachedSeaLevel):
        #     if (event.xPosition == self.model.getPosition()):
        #         self.model.setReachedSeaLevel()
        #         self.eventManager.UnregisterListener(self)

        if isinstance(event, ParachutistReachedSeaLevelEvent):
            position = self.model.getPosition()
            if position[0] == event.xPosition:
                self.eventManager.UnregisterListener(self)
        return





if __name__ == '__main__':
    eventManager = EventManager()
    parachutistModel = ParachutistModel(eventManager,1,1,1,1)
    parachutist = ParachutistController(eventManager,parachutistModel)
    parachutist.descent()
    x = 1