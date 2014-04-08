import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((480, 720))
pygame.display.set_caption('Car Plate Registration System')

class menu():
    global screen
        #textList = [[text, xpos, ypos, color, fontSize]]
    def createText(self, text, xpos, ypos, color, fontSize):
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
    def createButton(self, text, xpos, ypos, textColor, buttonColor, fontSize):
        font = pygame.font.Font(None, fontSize)
        text = font.render(text, 1, textColor)
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
         screen.fill(buttonColor, textpos)
         screen.blit(text, textpos)

menu = menu()
screen.fill((60, 60, 60))
menu.createButton('Hey', 'center', 600, (0, 0, 0), (200, 200, 200), 36)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

