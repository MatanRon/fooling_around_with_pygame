import pygame
from Model import BaseModel
from EventManager import *
from abc import ABC, abstractmethod

class BaseGameObjectController(ABC):
    """
    Controls the object.
    """

    def __init__(self, eventManager, model):
        """
        eventManager allows posting messages to the event queue.
        model a strong reference to the game object Model.
        """
        self.eventManager = eventManager
        eventManager.RegisterListener(self)
        self.model = model

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """
        pass