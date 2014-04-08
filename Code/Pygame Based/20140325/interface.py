import pygame, sys
from pygame.locals import *

pygame.init()
width, height = 400, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Car Plate Registration System')
def generateText(self, text, xpos, ypos, color, fontSize):
    font = pygame.font.Font(None, fontSize)
    text = font.render(text, 1, color)
    textpos = text.get_rect()
    if type(xpos) == str:
        if xpos == 'center':
              textpos.x = (480/2)-textpos.width/2
        if xpos == 'left':
            textpos.x = 10
        if xpos == 'right':
            textpos.x = 480-textpos.width-10
    elif type(xpos) == int:
        textpos.x = xpos
    if type(ypos)== str:
        if ypos == 'center':
            textpos.y = 720/2-textpos.height
    elif type(ypos) == int:
        textpos.y = ypos
    screen.blit(text, textpos) 
class button(pygame.sprite.Sprite):
    def __init__(self, text, xpos, ypos, textColor, buttonColor, highlightColor, fontSize, *function):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, fontSize)
        self.text = self.font.render(text, 1, textColor)
        self.textpos = self.text.get_rect()
        self.buttonColor = buttonColor
        self.highlightColor = highlightColor
        self.function = function
        if type(xpos) == str:
            if xpos == 'center':
                self.textpos.x = (width/2)-self.textpos.width/2
            if xpos == 'left':
                self.textpos.x = 10
            if xpos == 'right':
                self.textpos.x = width-self.textpos.width-10
        elif type(xpos) == int:
            self.textpos.x = xpos
        if type(ypos)== str:
            if ypos == 'center':
                self.textpos.y = height/2-textpos.height
        elif type(ypos) == int:
            self.textpos.y = ypos
        self.buttonRect = pygame.Rect(self.textpos[0]-15, self.textpos[1]-8, self.textpos[2]+30, self.textpos[3]+16)
        self.highlightRect = pygame.Rect(self.buttonRect[0]-2, self.buttonRect[1]-2, self.buttonRect[2]+4, self.buttonRect[3]+4)
    def generateButton(self):
        screen.fill(self.buttonColor, self.buttonRect)
        screen.blit(self.text, self.textpos)
    def highlightButton(self):
        screen.fill(self.highlightColor, self.highlightRect)
        self.generateButton()
    def update(self):
        global mousePosition, mousePress
        if self.buttonRect.collidepoint(mousePosition):
            self.highlightButton()
            if mousePress[0] == True:
                for i in range(len(self.function)):
                    eval(self.function[i])
        else:
            self.generateButton()
def update():
    global mousePosition, mousePress
    mousePosition = pygame.mouse.get_pos()
    mousePress = pygame.mouse.get_pressed()
    screen.fill((255, 255, 255))
    buttonGroup.update()
    pygame.display.update()
    
buttonGroup = pygame.sprite.Group()
quitButton = button('Quit', 'center', 160, (0, 0, 0), (200, 200, 200), (0,0,0), 16, 'pygame.quit()', 'sys.exit()')
buttonGroup.add(quitButton)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    update()

