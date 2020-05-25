from random import randrange
import pygame
from EventManager import *
from random import randrange
from Model import GameModel, ParachutistModel, BoatModel
from Controller import  ParachutistController
from View import ParachutistView
from GameConfig import *


class GameController(object):
    """
    Handles keyboard input.
    """

    def __init__(self, eventManager, gameWindow, model, planeModel, boatModel):
        """
        eventManager Allows posting messages to the event queue.
        model (GameEngine): a strong reference to the game Model.
        """
        self.eventManager = eventManager
        eventManager.RegisterListener(self)
        self.gameWindow = gameWindow

        self.model = model
        self.planeModel = planeModel
        self.boatModel = boatModel

    def hit(self, other):
        return not ((self.x + self.width < other.x) or (self.y + self.height < other.y) or (
                    self.x > other.x + other.width) or (
                            self.y > other.y + self.height))
    def notify(self, event):
        """
        Receive events posted to the message queue.
        """

        if isinstance(event, TickEvent):
            # Called for each game tick. We check our keyboard presses here.

            # check for quit operation
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                    self.eventManager.Post(QuitEvent())


        if isinstance(event, ParachutistReachedSeaLevelEvent):
            self.handleParachutistLanding(event)
            # position = self.model.getPosition()
            # if position[0] == event.xPosition:
            #     self.eventManager.UnregisterListener(self)


    def handleParachutistLanding(self, ParachutistReachedSeaLevelEvent):
        currentParachtistModel = ParachutistReachedSeaLevelEvent.parachutistModel
        boatModel = self.boatModel

        onBoatLanding = self.intersects(currentParachtistModel, boatModel)

        if onBoatLanding:
            self.eventManager.Post(onBoatLandingEvent())
        else:
            self.eventManager.Post(onWaterLandingEvent())


    def intersects(self, gameObjectModelA, gameObjectModelB):
        position  = gameObjectModelA.getPosition()
        aXPosition = position[0]
        aYPosition = position[1]
        aHight = gameObjectModelA.getHight()
        aWidth = gameObjectModelA.getWidth()

        position  = gameObjectModelB.getPosition()
        bXPosition = position[0]
        bYPosition = position[1]
        bHight = gameObjectModelB.getHight()
        bWidth = gameObjectModelB.getWidth()

        return not ((aXPosition + aWidth < bXPosition) or
                    (aYPosition + aHight < bYPosition) or
                    (aXPosition > bXPosition + bWidth) or
                    (aYPosition > bYPosition + aHight))

    def run(self):
        """
        Starts the game engine loop.

        This pumps a Tick event into the message queue for each loop.
        The loop ends when this object hears a QuitEvent in notify().
        """
        self.model.startRuning()
        self.eventManager.Post(InitializeEvent())
        # parachutistControllersList = []
        # parachutistViewsList = []
        while self.model.isRuning():
            newTick = TickEvent()
            self.eventManager.Post(newTick)

            # randomly generate parachutists so that
            # on each TickEvent there's a chance of one in a 'parachutistCreationRate' to create new parachutist
            if randrange(50) == 1 :
                planeCurrentPosition = self.planeModel.getPosition()

                parachutistModel = ParachutistModel.ParachutistModel(self.eventManager,
                                                                     planeCurrentPosition[0],
                                                                     0,
                                                                     parachutistWidth,
                                                                     parachutistHight)
                parachutistController = ParachutistController.ParachutistController(self.eventManager, parachutistModel)
                parachutistView = ParachutistView.ParachutistView(self.eventManager, parachutistModel, self.gameWindow)

                self.model.addParachutist(parachutistController, parachutistView)
                self.eventManager.Post(InitializeEvent())







            # randomly generate parachutists so that
            # on each TickEvent there's a chance of one in a 'parachutistCreationRate' to create
            # new parachutist

            # if randrange(50) == 2 :
            #     planeCurrentPosition = self.planeModel.getPosition()
            #
            #     parachutistModel = ParachutistModel.ParachutistModel(self.eventManager,
            #                                                          planeCurrentPosition[0], 0, 100, 100) # todo: fix passed arguments
            #     parachutistController = ParachutistController.ParachutistController(self.eventManager, parachutistModel)
            #     parachutistView = ParachutistView.ParachutistView(self.eventManager, parachutistModel, self.gameWindow)
            #     self.eventManager.Post(InitializeEvent())

        # if isinstance(event, parachutistReachedSeaLevelEvent):
        #     boatCurrentLocation = 0 #fixme: add BoatModel.getBoatLocation()
        #     if event.xPosition