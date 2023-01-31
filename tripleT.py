import os
import random
import math

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


def clamp(n, smallest, largest):
  return max(smallest, min(n, largest))


class FaultyCoordinate(Exception):
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
    self.xToken = pygame.image.load('x.png')
    self.oToken = pygame.image.load('o.png')

    self.spaceSize = 260
    self.width = 1050
    self.height = self.width
    self.xOrO = 'x'
    #horizontally counted
    self.spacesTopLeft = {
        (1, 1): (141, 141),
        (1, 2): (409, 143),
        (1, 3): (671, 143),
        (2, 1): (143, 409),
        (2, 2): (143, 671),
        (2, 3): (409, 409),
        (3, 1): (671, 409),
        (3, 2): (409, 671),
        (3, 3): (671, 671)
    }
    self.occupations = {
        (1, 1): False,
        (1, 2): False,
        (1, 3): False,
        (2, 1): False,
        (2, 2): False,
        (2, 3): False,
        (3, 1): False,
        (3, 2): False,
        (3, 3): False,
    }

    self.gameDisplay = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption("τtT")
    self.clock = pygame.time.Clock()

  def CoordsToSpace(self, pos):

    x = clamp(math.floor((pos[0] + 141) / self.spaceSize), 1, 3)
    y = clamp(math.floor((pos[1] + 141) / self.spaceSize), 1, 3)
    return (x, y)

  def placeSymbol(self, space):
    '''
    places x or o in the designated space
    '''
    #add turn logic here
    self.gameDisplay.blit(self.xToken, (self.spacesTopLeft[space]))
    space = True

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.exit = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.x, self.y = self.CoordsToSpace(event.pos)
        if self.occupations[(self.x, self.y)] == False:
          self.placeSymbol((self.x, self.y))

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