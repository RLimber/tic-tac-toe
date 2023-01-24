import os
import random
import math

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


def clamp(n, smallest, largest):
  return max(smallest, min(n, largest))


class IgnoreCoordinate(Exception):
  pass


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
    self.spaceSize = 230
    self.width = 1050
    self.height = self.width
    self.xOrO = 'x'
    #horizontally counted
    self.spacesTopLeft = {
        1: (143, 143),
        2: (409, 143),
        3: (671, 143),
        4: (143, 409),
        7: (143, 671),
        5: (409, 409),
        6: (671, 409),
        8: (409, 671),
        9: (671, 671)
    }
    self.gameDisplay = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption("τtT")
    self.clock = pygame.time.Clock()

  def CoordsToCell(self, pos):

    #x = math.floor(pos[0] / self.spaceSize)
    #y = math.floor(pos[1] / self.spaceSize)
    #if x != clamp(x, 0, 3):
    #  raise IgnoreCoordinate('nah')
    #if y != clamp(y, 0, 3):
    #  raise IgnoreCoordinate('nope')
    #print(x, y)
    #return (x, y)
    for k, v in self.spacesTopLeft.items():
      if self.spacesTopLeft[k][0] <= pos[0] <= self.spacesTopLeft[k + 1][0] and self.spacesTopLeft[k][1] <= pos[1] <= self.spacesTopLeft[k + 1][1]:
        print(k)
        return k

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.exit = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.x, self.y = self.CoordsToCell(event.pos)

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