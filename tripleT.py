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
    self.PoE = None
    self.spaceSize = 260
    self.turn = None
    self.width = 1050
    self.height = self.width
    self.choiceScreen = pygame.image.load('choiceScreen.jpg')
    self.inChoiceScreen = True
    self.turnNumber = 1
    self.choiceXRect = pygame.Rect(404, 363, 234, 234)
    self.choiceORect = pygame.Rect(404, 685, 234, 234)
    self.xGroup = pygame.sprite.Group()
    self.oGroup = pygame.sprite.Group()
    #horizontally counted
    self.spacesTopLeft = {
        (1, 1): (141, 141),
        (1, 2): (141, 413),
        (1, 3): (141, 668),
        (2, 1): (413, 141),
        (2, 2): (413, 413),
        (2, 3): (413, 668),
        (3, 1): (668, 141),
        (3, 2): (668, 413),
        (3, 3): (668, 668)
    }

    self.occupations = {
        (1, 1): None,
        (1, 2): None,
        (1, 3): None,
        (2, 1): None,
        (2, 2): None,
        (2, 3): None,
        (3, 1): None,
        (3, 2): None,
        (3, 3): None,
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
    if self.xOrO == 'x':
      spriteTurn = Sprite('x.png', (self.spacesTopLeft[space]))
      self.xGroup.add(spriteTurn)
      self.occupations[space] = False
      self.turn = True
    if self.xOrO == 'o':
      spriteTurn = Sprite('o.png', (self.spacesTopLeft[space]))
      self.oGroup.add(spriteTurn)
      self.occupations[space] = True
      self.turn = False
    self.turnNumber += 1

  def winner(self):
    for x in range(1, 4):
      first = self.occupations[(x, 1)]
      column = first == self.occupations[(x, 2)] and first == self.occupations[(x, 3)] and first != None
      if column:
        return first
    for x in range(1, 4):
      first = self.occupations[(1, x)]
      row = first == self.occupations[(2, x)] and first == self.occupations[(3, x)] and first != None
      if row:
        return first
    middle = self.occupations[(2, 2)]
    diagonal = middle == self.occupations[(1, 1)] and middle == self.occupations[(3, 3)] and middle != None
    if diagonal:
      return middle
    diagonal = middle == self.occupations[(1, 3)] and middle == self.occupations[(3, 1)] and middle != None
    if diagonal:
      return middle

  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.exit = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.x, self.y = self.CoordsToSpace(event.pos)
        if self.occupations[(self.x, self.y)] == None and not self.inChoiceScreen:
          self.placeSymbol((self.x, self.y))
        if self.inChoiceScreen:
          if self.choiceORect.collidepoint(event.pos):
            self.xOrO = 'o'
            self.turn = True
            self.inChoiceScreen = False
          elif self.choiceXRect.collidepoint(event.pos):
            self.xOrO = 'x'
            self.turn = False
            self.inChoiceScreen = False

  def updateGame(self):
    win = self.winner()
    if win:
      print('easy W for O')
    elif win is not None:
      print("X takes the dub")
    if win is None:
      if self.turn == False:
        self.xOrO = 'x'
      elif self.turn == True:
        self.xOrO = 'o'

  def draw(self):
    if self.inChoiceScreen:
      self.gameDisplay.blit(self.choiceScreen, (0, 0))
    else:
      self.gameDisplay.blit(self.background, (0, 0))
      for sprite in self.xGroup:
        sprite.draw(self.gameDisplay)
      for sprite in self.oGroup:
        sprite.draw(self.gameDisplay)

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