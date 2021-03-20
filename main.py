import pygame

# Upper left corner of image given desired center
def xUpperLeft(centerCoords):
    xCoord = centerCoords[0] - 91/2
    yCoord = centerCoords[1] - 86/2

    return (xCoord, yCoord)

def oUpperLeft(centerCoords):
    xCoord = centerCoords[0] - 95/2
    yCoord = centerCoords[1] - 95/2

    return (xCoord, yCoord)


# Board square coordinates
squareCenters = (((56.5,56.5), (180.5, 56.5), (304, 56.5)),
                 ((56.5, 180.5), (180.5, 180.5), (304, 180.5)),
                 ((56.5, 304),(180.5, 304),(304, 304)))

# Images
boardImg = pygame.image.load("images/board.png") # 360x360
xImg = pygame.image.load("images/x.png") # 91x86
oImg = pygame.image.load("images/o.png") # 95x95

# Initialize module
pygame.init()

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
    gameDisplay.blit(boardImg,(0,0))

    gameDisplay.blit(oImg, oUpperLeft(squareCenters[0][2]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    pygame.display.flip()


pygame.quit()
