import pygame

class Board:
    def __init__(self):
        self.BLACK = (0,0,0)

        # Center for each of the nine squares
        self.squareCenters = (((56.5,56.5), (180, 56.5), (303.5, 56.5)),
                 ((56.5, 180), (180, 180), (303.5, 180)),
                 ((56.5, 303.5),(180, 303.5),(303.5, 303.5)))

        # Rectangle object for each of the nine squares
        self.squareOne = pygame.Rect(0, 0,113,113)
        self.squareTwo = pygame.Rect(127, 0, 233, 113)
        self.squareThree = pygame.Rect(247, 0, 360, 113)

        self.squareFour = pygame.Rect(0, 127, 113, 233)
        self.squareFive = pygame.Rect(127, 127, 233, 233)
        self.squareSix = pygame.Rect(247, 127, 360, 233)

        self.squareSeven = pygame.Rect(0, 247, 113, 360)
        self.squareEight = pygame.Rect(127, 247, 233, 360)
        self.squareNine = pygame.Rect(247, 247, 360, 360)

        # Board status - None = Empty, 0 = 0, 1 = X
        self.boardStatus = [[None, None, None],
                            [None, None, None],
                            [None, None, None]]


    # Draw the game board
    def drawBoard(self):
        pygame.draw.line(gameDisplay, self.BLACK, (120, 0), (120, 360), 15)
        pygame.draw.line(gameDisplay, self.BLACK, (240, 0), (240, 360), 15)
        pygame.draw.line(gameDisplay, self.BLACK, (0, 120), (360, 120), 15)
        pygame.draw.line(gameDisplay, self.BLACK, (0, 240), (360, 240), 15)

    def updateBoard(self):
        pass

    # Draw X and O given center coordinates
    def drawX(self, centerCoords):
        self.xCoord = centerCoords[0] - 91 / 2
        self.yCoord = centerCoords[1] - 86 / 2
        gameDisplay.blit(xImg, (self.xCoord, self.yCoord))

    def drawO(self, centerCoords):
        self.xCoord = centerCoords[0] - 95 / 2
        self.yCoord = centerCoords[1] - 95 / 2
        gameDisplay.blit(oImg, (self.xCoord, self.yCoord))


# Images
xImg = pygame.image.load("images/x.png") # 91x86
oImg = pygame.image.load("images/o.png") # 95x95

# Initialize module and board
pygame.init()
gameBoard = Board()

# Display and some settings
screenSize = (360,360)
backgroundColor = (255,255,255)
gameName = 'Tic-Tac-Toe but You Can\'t Win'

# Initialize display
gameDisplay = pygame.display.set_mode(screenSize)
pygame.display.set_caption(gameName)


# Is game running
running = True


# Main loop
while running:
    gameDisplay.fill(backgroundColor)
    mouse_pos = pygame.mouse.get_pos()
    gameBoard.drawBoard()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0] and gameBoard.squareOne.collidepoint(mouse_pos):
            pass




    pygame.display.flip()


pygame.quit()
