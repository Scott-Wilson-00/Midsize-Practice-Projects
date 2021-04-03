import pygame
import random
import pyperclip
pygame.init()

# Initialize display, icon, and caption
# Display
screenHeight, screenWidth = 700, 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
# Caption
pygame.display.set_caption("Password Generator")
# Icon
icon = pygame.image.load("lock.png")
pygame.display.set_icon(icon)

# General text variables
black = (0, 0, 0)
regularFont = pygame.font.Font('freesansbold.ttf', 20)
midSizeFont = pygame.font.Font('freesansbold.ttf', 30)
titleFont = pygame.font.Font('freesansbold.ttf', 40)

# Password variables
numOfChars = 10
password = ''


def GetTextPosition(text, x_offset=0, y_offset=0):
    """
    Allows text placement to be handled with cartesian plane style coordinates

    :param text: the text for which the center of screen coordinates will be returned
    :param x_offset: offset on the x axis (positive:right, negative:left)
    :param y_offset: offset on the y axis (positive:up, negative:down)
    :return: the coordinates at which the given text will be at the center of the screen
    """
    x_pos = ((screenWidth-text.get_width())/2) + x_offset
    y_pos = ((screenHeight-text.get_height())/2) - y_offset
    return x_pos, y_pos


# Initialize GUI Text Elements
titleText = titleFont.render('Password Generator', True, black)
lowerText = regularFont.render('Lowercase Characters', True, black)
upperText = regularFont.render('Uppercase Characters', True, black)
numberText = regularFont.render('Numbers', True, black)
symbolText = regularFont.render('Symbols', True, black)
miscCharText = regularFont.render('Miscellaneous Characters', True, black)
lengthText = regularFont.render('Length:', True, black)

# Initialize GUI Text Element Positions
titleTextPos = GetTextPosition(titleText, 0, 250)
lowerTextPos = GetTextPosition(lowerText, -225, 150)
upperTextPos = GetTextPosition(upperText, -225, 50)
numberTextPos = GetTextPosition(numberText, 150, 50)
symbolTextPos = GetTextPosition(symbolText, 150, 150)
miscCharTextPos = GetTextPosition(miscCharText, -225, -50)
lengthTextPos = GetTextPosition(lengthText, 150, -50)

# Initialize GUI text buttons
plusText = midSizeFont.render("+", True, black)
minusText = midSizeFont.render("-", True, black)
genPassText = regularFont.render("Generate Secure Password", True, black)
copyText = regularFont.render("Copy To Clipboard", True, black)

# Initialize GUI text button positions
plusTextPos = GetTextPosition(plusText, 250, -35)
minusTextPos = GetTextPosition(minusText, 250, -65)
genPassTextPos = GetTextPosition(genPassText, 0, -125)
copyTextPos = GetTextPosition(copyText, 0, -300)

# Initialize text GUI button rects
plusTextRect = screen.blit(plusText, plusTextPos)
minusTextRect = screen.blit(minusText, minusTextPos)
genPassTextRect = screen.blit(genPassText, genPassTextPos)
copyTextRect = screen.blit(copyText, copyTextPos)

bDimensions = 20
# Initialize toggle button rects
lowerButtonRect = pygame.rect.Rect(325, 190, bDimensions, bDimensions)
upperButtonRect = pygame.rect.Rect(325, 290, bDimensions, bDimensions)
numButtonRect = pygame.rect.Rect(625, 290, bDimensions, bDimensions)
symbolButtonRect = pygame.rect.Rect(625, 190, bDimensions, bDimensions)
miscCharButtonRect = pygame.rect.Rect(325, 390, bDimensions, bDimensions)

# Initialize password generation/button variables
buttonBorderSize = 3
lowerBool, lower = True, 0
upperBool = numsBool = symbolBool = miscCharBool = False
upper = nums = symbol = miscChar = buttonBorderSize



def BlitText():
    """
    Blit text elements to screen
    
    :return: None
    """
    screen.blit(titleText, titleTextPos)
    screen.blit(lowerText, lowerTextPos)
    screen.blit(upperText, upperTextPos)
    screen.blit(numberText, numberTextPos)
    screen.blit(symbolText, symbolTextPos)
    screen.blit(miscCharText, miscCharTextPos)
    screen.blit(lengthText, lengthTextPos)
    screen.blit(plusText, plusTextPos)
    screen.blit(minusText, minusTextPos)
    screen.blit(numOfCharsVisual, numOfCharsPos)
    screen.blit(genPassText, genPassTextPos)
    pygame.draw.line(screen, black, (270, 485), (530, 485), 2)
    screen.blit(copyText, copyTextPos)
    pygame.draw.line(screen, black, (320, 659), (480, 659), 2)
    screen.blit(passwordText, passwordTextPos)



def DrawButtons():
    """
    Draw toggle buttons to screen
    
    :return: None
    """
    pygame.draw.rect(screen, black, lowerButtonRect, lower)
    pygame.draw.rect(screen, black, upperButtonRect, upper)
    pygame.draw.rect(screen, black, numButtonRect, nums)
    pygame.draw.rect(screen, black, symbolButtonRect, symbol)
    pygame.draw.rect(screen, black, miscCharButtonRect, miscChar)


def GeneratePassword():
    """
    Generates a new password to be displayed
    
    :return: The new password
    """
    password = ''
    choices = ''
    if lowerBool:
        choices = choices + 'abcdefghijklmnopqrstuvwxyz'
    if upperBool:
        choices = choices + 'abcdefghijklmnopqrstuvwxyz'.upper()
    if numsBool:
        choices = choices + '11223344556677889900'
    if symbolBool:
        choices = choices + '!@#$%&?'
    if miscCharBool:
        choices = choices + "(){}[]/\,;:<>\'\""

    try:
        for i in range(numOfChars):
            password = password + random.choice(choices)
    except IndexError:
        return ''

    return password


# Main loop
running = True
while running:

    # Updates the display's number of characters shown
    numOfCharsVisual = midSizeFont.render(str(numOfChars), True, black)
    numOfCharsPos = GetTextPosition(numOfCharsVisual, 215, -50)

    # Updates the password shown
    passwordText = midSizeFont.render(password, True, black)
    passwordTextPos = GetTextPosition(passwordText, 0, -210)

    # Update screen background, text, and buttons
    screen.fill((200, 200, 200))
    BlitText()
    DrawButtons()
    pygame.display.update()

    # Runs through all the events detected
    for event in pygame.event.get():

        # Ends the program
        if event.type == pygame.QUIT:
            running = False
            break

        # Registers the user's mouse button click and it's position
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # Increases # of characters in the password
            if plusTextRect.collidepoint(pos):
                if numOfChars < 30:
                    numOfChars += 1
            # Decreases # of characters in the password
            elif minusTextRect.collidepoint(pos):
                if numOfChars > 8:
                    numOfChars -= 1
            # Generates a new password
            elif genPassTextRect.collidepoint(pos):
                password = GeneratePassword()
            # Copies the password to user's clipboard
            elif copyTextRect.collidepoint(pos):
                pyperclip.copy(password)

            # Toggle password generation settings
            elif lowerButtonRect.collidepoint(pos):
                lowerBool = not lowerBool
                if lowerBool:
                    lower = 0
                else:
                    lower = buttonBorderSize
            elif upperButtonRect.collidepoint(pos):
                upperBool = not upperBool
                if upperBool:
                    upper = 0
                else:
                    upper = buttonBorderSize
            elif numButtonRect.collidepoint(pos):
                numsBool = not numsBool
                if numsBool:
                    nums = 0
                else:
                    nums = buttonBorderSize
            elif symbolButtonRect.collidepoint(pos):
                symbolBool = not symbolBool
                if symbolBool:
                    symbol = 0
                else:
                    symbol = buttonBorderSize
            elif miscCharButtonRect.collidepoint(pos):
                miscCharBool = not miscCharBool
                if miscCharBool:
                    miscChar = 0
                else:
                    miscChar = buttonBorderSize

