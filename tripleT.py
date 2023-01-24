import os
import random

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class Sprite(pygame.sprite.Sprite):
  """
    filename is the filename
    upperleft is tuple of coords of upperleft
    """

  def __init__(self, fileName, upperLeft):
    super().__init__()
    self.upperLeft = upperLeft
    self.image = pygame.image.load(fileName)
    self.rect = self.image.get_rect()
    self.rect[0] = self.upperLeft[0]
    self.rect[1] = self.upperLeft[1]

  def draw(self, gameDisplay):
    """
        draws a sprite
        """
    gameDisplay.blit(self.image, self.upperLeft)

  def getPos(self):
    return self.upperLeft

  def getX(self):
    return self.upperLeft[0]

  def getY(self):
    return self.upperLeft[1]

  def setX(self, newValue):
    self.upperLeft = (newValue, self.upperLeft[1])

  def setY(self, newValue):
    self.upperLeft = (self.upperLeft[0], newValue)


class Game():

  def __init__(self):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    self.exit = False
    self.background = pygame.image.load('board.png')

    self.width = 1050
    self.height = self.width
    self.gameDisplay = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption("τθt")
    self.clock = pygame.time.Clock()

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.exit = True

  def updateGame(self):
    pass

  def draw(self):
    self.gameDisplay.blit(self.background, (0, 0))

  def gameloop(self):
    while not self.exit:
      self.handleEvents()
      self.updateGame()
      self.draw()
      pygame.display.update()
      self.clock.tick(35)


if __name__ == "__main__":
  game = Game()
  game.gameloop()
  pygame.quit()
  quit()