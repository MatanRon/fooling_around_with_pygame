import pygame
from EventManager import *
import GameConfig

class BaseGameObjectModel(pygame.sprite.Sprite):
    """
    Tracks the game state.
    """

    def __init__(self, eventManager, xStartPosition, yStartPosition, width, height):
        """
        evManager (EventManager): Allows posting messages to the event queue.

        Attributes:
        running (bool): True while the engine is online. Changed via QuitEvent().
        """

        pygame.sprite.Sprite.__init__(self) #askme: is there any better way to automaticly call superClass init ?

        self.eventManager = eventManager
        eventManager.RegisterListener(self)
        self.running = False
        self.xPosition = xStartPosition
        self.yPosition = yStartPosition
        self.speed = GameConfig.gameSpeed
        self.width = width
        self.height = height

    def notify(self, event):
        """
        Called by an event in the message queue.
        """

        if isinstance(event, QuitEvent):
            self.running = False

    def run(self):
        """
        Starts the game engine loop.

        This pumps a Tick event into the message queue for each loop.
        The loop ends when this object hears a QuitEvent in notify().
        """
        self.running = True
        self.evManager.Post(InitializeEvent())
        while self.running:
            newTick = TickEvent()
            self.evManager.Post(newTick)

    def getPosition(self):
        return self.xPosition, self.yPosition

    def setPosition(self, xPosition, yPosition):
        self.xPosition = xPosition
        self.yPosition = yPosition

    def getSpeed(self):
        return self.speed

    # def intersects(self, object):
    #     return not ((self.xPosition + self.width < object.xPosition) or
    #                 (self.yPosition + self.height < object.yPosition) or
    #                 (self.xPosition > object.xPosition + object.width) or
    #                 ( self.yPosition > object.yPosition + self.height))

    def getWidth(self):
        return self.width

    def getHight(self):
        return self.height