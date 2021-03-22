import pygame
from pygame.locals import *

class Board:
    def __init__(self, width, height):
        self.BLACK = (0, 0, 0)
        self.width = width
        self.height = height
        self.isX = 'x'
        self.winner = None
        self.draw = None


        # Board status - None = Empty, 0 = 0, 1 = X
        self.boardStatus = [[None] * 3, [None] * 3, [None] * 3]

        gameDisplay.fill(backgroundColor)
        self.showBoard()

    # Draw the game board
    def showBoard(self):
        pygame.draw.line(gameDisplay, self.BLACK, (self.width/3, 0), (self.width/3, self.height), 15)
        pygame.draw.line(gameDisplay, self.BLACK, (2*self.width/3, 0), (2*self.width/3, self.height), 15)
        pygame.draw.line(gameDisplay, self.BLACK, (0, self.height/3), (self.width, self.height/3), 15)
        pygame.draw.line(gameDisplay, self.BLACK, (0, 2*self.height/3), (self.width, 2*self.height/3), 15)

    # drawX and drawO converts center coordinates to appropriate upper left corner coordinates and shows image
    def drawX(self, centerCoords):
        self.xCoord = centerCoords[0] - 91 / 2
        self.yCoord = centerCoords[1] - 86 / 2
        gameDisplay.blit(xImg, (self.xCoord, self.yCoord))

    def drawO(self, centerCoords):
        self.xCoord = centerCoords[0] - 95 / 2
        self.yCoord = centerCoords[1] - 95 / 2
        gameDisplay.blit(oImg, (self.xCoord, self.yCoord))

    # Action taken when mouse is clicked
    def user_click(self):
        # get coordinates of mouse click
        x, y = pygame.mouse.get_pos()

        # get column of mouse click (1-3)
        if (x < self.width / 3):
            col = 1

        elif (x < self.width / 3 * 2):
            col = 2

        elif (x < self.width):
            col = 3

        else:
            col = None

        # get row of mouse click (1-3)
        if (y < self.height / 3):
            row = 1

        elif (y < self.height / 3 * 2):
            row = 2

        elif (y < self.height):
            row = 3

        else:
            row = None

        # Make the desired move
        if (row and col and self.boardStatus[row - 1][col - 1] is None):
            self.playMove(row, col)
            self.check_win()

    #Row and column definitions are wrong !!!
    def playMove(self, row, col):
        '''
        Centers for each of the nine squares
        (((56.5, 56.5), (180, 56.5), (303.5, 56.5)),
        ((56.5, 180), (180, 180), (303.5, 180)),
        ((56.5, 303.5), (180, 303.5), (303.5, 303.5)))
        '''

        if row == 1:
            posx = 56.5

        if row == 2:

            posx = 180

        if row == 3:
            posx = 303.5

        if col == 1:
            posy = 56.5

        if col == 2:
            posy = 180

        if col == 3:
            posy = 303.5

        # Updating board status
        self.boardStatus[row - 1][col - 1] = self.isX

        # Draw X or O visually given center coordinates
        if (self.isX == 'x'):
            self.drawX((posy,posx))
            self.isX = 'o'

        else:
            self.drawO((posy, posx))
            self.isX = 'x'
        pygame.display.update()

    def draw_status(self):
        if self.winner is None:
            message = self.isX.upper() + "'s Turn"
        else:
            message = self.winner.upper() + " won !"
        if self.draw:
            message = "Game Draw !"

        print(message)

    def check_win(self):

        # Check for winning rows
        # Checks if entire row has the same mark, X or O. Initial none cases pose a problem here
        # Which is solved with the "is not None" part
        # Also draws a line on the winning row
        for row in range(0, 3):
            if ((self.boardStatus[row][0] == self.boardStatus[row][1] == self.boardStatus[row][2]) and (self.boardStatus[row][0] is not None)):
                self.winner = self.boardStatus[row][0]
                pygame.draw.line(gameDisplay, (250, 0, 0),
                             (0, (row + 1) * self.height / 3 - self.height / 6),
                             (self.width, (row + 1) * self.height / 3 - self.height / 6),
                             4)
                break

        # Same logic with the rows
        for col in range(0, 3):
            if ((self.boardStatus[0][col] == self.boardStatus[1][col] == self.boardStatus[2][col]) and (self.boardStatus[0][col] is not None)):
                self.winner = self.boardStatus[0][col]
                pygame.draw.line(gameDisplay, (250, 0, 0), ((col + 1) * self.width / 3 - self.width / 6, 0),
                             ((col + 1) * self.width / 3 - self.width / 6, self.height), 4)
                break

        # Pretty much the same with row and column
        if (self.boardStatus[0][0] == self.boardStatus[1][1] == self.boardStatus[2][2]) and (self.boardStatus[0][0] is not None):
            # Main diagonal
            self.winner = self.boardStatus[0][0]
            pygame.draw.line(gameDisplay, (250, 70, 70), (50, 50), (350, 350), 4)

        if (self.boardStatus[0][2] == self.boardStatus[1][1] == self.boardStatus[2][0]) and (self.boardStatus[0][2] is not None):
            # Off diagonal
            self.winner = self.boardStatus[0][2]
            pygame.draw.line(gameDisplay, (250, 70, 70), (350, 50), (50, 350), 4)

            # Explain
        if (all([all(row) for row in self.boardStatus]) and self.winner is None):
            self.draw = True

        self.draw_status()



# Images
xImg = pygame.image.load("images/x.png")  # 91x86
oImg = pygame.image.load("images/o.png")  # 95x95

# Initialize module
pygame.init()


# Display and some settings
screenSize = (360, 360)
backgroundColor = (255, 255, 255)
gameName = 'Tic-Tac-Toe but You Can\'t Win'

# Initialize display
gameDisplay = pygame.display.set_mode(screenSize)
pygame.display.set_caption(gameName)
gameBoard = Board(*screenSize)

# Is game running
running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            gameBoard.user_click()


    pygame.display.update()

pygame.quit()
