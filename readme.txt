As the name of this repository implies, the main goal of this nice game implementation is to have some fun with the capabilities of the (awesome) Pygame library.

The design of the project was done according to CMV principles (Controller Model Viewer)
This is alongside an event-driven implementation. That is, actions are triggered by events whose source is other entities in the project. The update of the project's entities about events is orchestrated by a dedicated event manager.

The rules:
The plane passes and randomly throws Pocahontas once in a while, which performs a free fall straight down. 
The player's role is to catch as many Pocahontases as possible.
Each Pocahontas rescue will add 10 points to the player.
Each fall of Pocahontas into the water will result in the loss of one life point.
