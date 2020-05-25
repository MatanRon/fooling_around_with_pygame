import pygame
from random import randrange
from EventManager import *
from Model import ParachutistModel
from GameConfig import *
# from Controller import  ParachutistController
# from View import ParachutistView
# from ParachutistDescriptor import ParachutistDescriptor

class GameModel(object):
    """
    Tracks the game state.
    """

    def __init__(self, eventManager, gameWindow, planeModel):
        """
        evManager (EventManager): Allows posting messages to the event queue.

        Attributes:
        running (bool): True while the engine is online. Changed via QuitEvent().
        """

        self.eventManager = eventManager
        eventManager.RegisterListener(self)
        self.clock = pygame.time.Clock()

        self.lifePoints = lifePoints
        self.score = 0
        self.running = False
        self.parachutistControllersList = []
        self.parachutistViewsList = []


        # self.gameWindow = gameWindow
        # self.planeModel = planeModel

    def addParachutist(self, parachutistController, parachutistView):
        self.parachutistControllersList.append(parachutistController)
        self.parachutistViewsList.append(parachutistView)

    def stopRuning(self):
        self.running = False

    def startRuning(self):
        self.running = True

    def isRuning(self):
        return self.running

    def getLifePoints(self):
        return self.lifePoints

    def getScore(self):
        return self.score

    def notify(self, event):
        """
        Called by an event in the message queue.
        """

        if isinstance(event, QuitEvent):
            self.running = False

        if isinstance(event,onBoatLandingEvent):
            self.score += successScore

        if isinstance(event,onWaterLandingEvent):
            self.lifePoints -= 1
            if 0 == self.lifePoints:
                print ('No more life points - Game Over')
                self.eventManager.Post(QuitEvent())

    # def run(self):
    #     """
    #     Starts the game engine loop.
    #
    #     This pumps a Tick event into the message queue for each loop.
    #     The loop ends when this object hears a QuitEvent in notify().
    #     """
    #     self.running = True
    #     self.eventManager.Post(InitializeEvent())
    #     parachutistControllersList = []
    #     parachutistViewsList = []
        # while self.running:
        #     newTick = TickEvent()
        #     self.eventManager.Post(newTick)
        #
        #     # randomly generate parachutists so that
        #     # on each TickEvent there's a chance of one in a 'parachutistCreationRate' to create new parachutist
        #
        #     if randrange(50) == 1 :
        #         planeCurrentPosition = self.planeModel.getPosition()
        #
        #         parachutistModel = ParachutistModel.ParachutistModel(self.eventManager,
        #                                                              planeCurrentPosition[0], 0, 100, 100) # todo: fix passed arguments
        #         parachutistController = ParachutistController.ParachutistController(self.eventManager, parachutistModel)
        #         parachutistView = ParachutistView.ParachutistView(self.eventManager, parachutistModel, self.gameWindow)
        #
        #         parachutistViewsList.append(parachutistView)
        #         parachutistControllersList.append(parachutistController)
        #         self.eventManager.Post(InitializeEvent())