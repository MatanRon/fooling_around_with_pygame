import pygame
from Model import BaseGameObjectModel
from EventManager import *
from abc import ABC, abstractmethod
import os

class BaseGameObjectView(ABC):
    """
    Draws the model state onto the screen.
    """

    def __init__(self, eventManager, model, window):
        """
        eventManager Allows posting messages to the event queue.
        model : a strong reference to the game object model.

        Attributes:
        isinitialized (bool): pygame is ready to draw.
        screen (pygame.Surface): the screen surface.
        clock (pygame.time.Clock): keeps the fps constant.
        smallfont (pygame.Font): a small font.
        """

        self.eventManager = eventManager
        eventManager.RegisterListener(self)
        self.model = model
        self.isinitialized = False
        self.screen = None
        self.clock = None
        self.smallfont = None
        self.window = window

    def loadImage(self, imageName):
        current_path = os.path.dirname(__file__)
        resource_path = os.path.join(current_path, 'resources')
        return pygame.image.load(os.path.join(resource_path, imageName))

    def initialize(self):
        if not (self.isinitialized):
            self.clock = pygame.time.Clock()
            self.isinitialized = True
        return

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        pass


    def renderall(self):
        """
        Draw the current game state on screen.
        Does nothing if isinitialized == False (pygame.init failed)
        """
        pass


