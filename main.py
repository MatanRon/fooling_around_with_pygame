import EventManager
from View import GameView, BoatView, ParachutistView, PlaneView
from Controller import GameController, BoatController, ParachutistController, PlaneController
from Model import GameModel, BoatModel, ParachutistModel, PlaneModel
import GameConfig

import pygame

def run():

    pygame.init()

    gameWindow = pygame.display.set_mode((GameConfig.screenHight, GameConfig.screenWidth))
    pygame.display.set_caption("Parachutists Game")

    eventManager = EventManager.EventManager()

    planeModel = PlaneModel.PlaneModel(eventManager, GameConfig.screenWidth, 20, 150, 100) # todo: fix args
    planeController = PlaneController.PlaneController(eventManager, planeModel)
    planeView = PlaneView.PlaneView(eventManager, planeModel, gameWindow)


    boatModel = BoatModel.BoatModel(eventManager,
                          GameConfig.boatStartXPosition,
                          GameConfig.boatStartYPosition,
                          GameConfig.boatWidth,
                          GameConfig.boatHight)
    boatController = BoatController.BoatController(eventManager, boatModel)
    boatView = BoatView.BoatView(eventManager, boatModel, gameWindow)



    gameModel = GameModel.GameModel(eventManager, gameWindow, planeModel)
    gameView = GameView.GameView(eventManager, gameWindow, gameModel)
    gameController = GameController.GameController(eventManager, gameWindow, gameModel, planeModel, boatModel)
    #gameModel.run()
    gameController.run()
if __name__ == '__main__':
    run()