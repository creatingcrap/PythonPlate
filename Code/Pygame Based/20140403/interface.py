import pygame, sys, carPlateRegistrationSystem, time
from pygame.locals import *
pygame.init()
width, height = 400, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Car Plate Registration System')


carPlateRegistrationSystem.clearFile()

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
                self.textpos.x = 40
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
        self.highlightRect = pygame.Rect(self.buttonRect[0]-1, self.buttonRect[1]-1, self.buttonRect[2]+2, self.buttonRect[3]+2)
    def generateButton(self):
        screen.fill(self.buttonColor, self.buttonRect)
        screen.blit(self.text, self.textpos)
    def highlightButton(self):
        screen.fill(self.highlightColor, self.highlightRect)
        self.generateButton()
    def update(self):
        if self.buttonRect.collidepoint(mousePosition):
            self.highlightButton()
            if mousePress[0] == True:
                for i in range(len(self.function)):
                    eval(self.function[i])
        else:
            self.generateButton()
            
class inputText(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, backgroundWidth, backgroundText, backgroundTextColor, backgroundColor, outlineColor, fontSize):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, fontSize)
        self.fontSize = fontSize
        self.backgroundText = self.font.render(backgroundText, 1, backgroundTextColor)
        self.textRect = self.backgroundText.get_rect()
        self.backgroundColor = backgroundColor
        self.outlineColor = outlineColor
        self.displayBox = False
        self.inputAccepted = False
        self.letterList = []
        self.shift = False
        self.capsLock = False
        self.getLetters = False
        self.string = ''
        if type(xpos) == str:
            if xpos == 'center':
                self.textRect.x = (width/2)-backgroundWidth/2
            if xpos == 'left':
                self.textRect.x = 40
            if xpos == 'right':
                self.textRect.x = width-self.textRect.width-10
        elif type(xpos) == int:
            self.textRect.x = xpos
        if type(ypos)== str:
            if ypos == 'center':
                self.textRect.y = height/2-textRect.height
        elif type(ypos) == int:
            self.textRect.y = ypos
        self.backgroundRect = pygame.Rect(self.textRect[0]-8, self.textRect[1]-8, backgroundWidth, self.textRect[3]+16)
        self.outlineRect = pygame.Rect(self.backgroundRect[0]-1, self.backgroundRect[1]-1, self.backgroundRect[2]+2, self.backgroundRect[3]+2) 
    def displayInputText(self):
        screen.fill(self.outlineColor, self.outlineRect)
        screen.fill(self.backgroundColor, self.backgroundRect)
        screen.blit(self.backgroundText, self.textRect)
    def displayInputBox(self):
        screen.fill(self.outlineColor, self.outlineRect)
        screen.fill(self.backgroundColor, self.backgroundRect)
    def printLetters(self):
        global runErrorCheck
        for i in range(len(self.letterList)):
            try:
                if self.letterList[i] >= 97 and self.letterList[i] <= 122:
                    self.letterList[i] = chr(self.letterList[i]-32)
                    runErrorCheck = False
                elif self.letterList[i] >= 48 and self.letterList[i] <= 57:
                    self.letterList[i] = chr(self.letterList[i])
                    runErrorCheck = False
                elif self.letterList[i] == 8:
                    self.letterList = self.letterList[:-2]
                    runErrorCheck = False
                else:
                   self.letterList = self.letterList[:-1]
            except:
                pass
        if len(self.letterList) >= 7:
            self.letterList = self.letterList[:-1]
        self.string = ''.join(self.letterList)
        generateText(self.string, self.textRect[0], self.textRect[1], (0, 0, 0), self.fontSize)
    def update(self):
        if self.backgroundRect.collidepoint(mousePosition):
            if mousePress[0] == True:
                self.displayBox = True
        if not self.backgroundRect.collidepoint(mousePosition):
            if mousePress[0] == True:
                self.displayBox = False
        if self.displayBox == True:
             self.displayInputBox()
             self.inputAccepted = True
        if self.displayBox == False:
            if not len(self.letterList) > 0:
                self.displayInputText()
            else:
                self.getLetters = False
                self.displayInputBox()
                self.printLetters()
            self.inputAccepted = False
        if self.inputAccepted == True:
            self.getLetters = True
            self.printLetters()

def generateText(text, xpos, ypos, color, fontSize):
    font = pygame.font.Font(None, fontSize)
    text = font.render(text, 1, color)
    textpos = text.get_rect()
    if type(xpos) == str:
        if xpos == 'center':
              textpos.x = (width/2)-textpos.width/2
        if xpos == 'left':
            textpos.x = 40
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

def check():
    global runErrorCheck, acceptedWord, realWord
    runErrorCheck = False
    acceptedWord = False
    runErrorCheck = True
    realWord = False
    check = carPlateRegistrationSystem.check()
    if check.word(inputBox.string.lower()) == True:
        realWord = True
    if check.wordLength(inputBox.string) == False:
        generateText('Word length must be equal to six characters.', 'center', 80, (255, 0, 0), 16)
    elif check.registered(inputBox.string) == True:
        generateText('Name already registered.', 'center', 80, (255, 0, 0), 16)
    elif check.restricted(inputBox.string.lower()) == True:
        generateText('Restricted name.', 'center', 80, (255, 0, 0), 16)
    elif accepted == True:
        generateText('Registered!', 'center', 80, (0,0,0), 16)
    else:
        generateText('Accepted!', 'center', 80, (0, 200, 0), 16)
        return True
    
def register():
    global runErrorCheck, totalPrice
    accepted = True
    carPlateRegistrationSystem.writeFile(inputBox.string)
    runErrorCheck = False
    if realWord == True:
        totalPrice += 110
    else:
        totalPrice += 70
    print('$' + str(totalPrice))
    
def update():
    global mousePosition, mousePress, keys, accepted
    keys = pygame.key.get_pressed()
    mousePosition = pygame.mouse.get_pos()
    mousePress = pygame.mouse.get_pressed()
    screen.fill((255, 255, 255))
    objects.update()
    if runErrorCheck == True:
        if check() == True:
            registerButton.update()
    pygame.display.update()

def price():
    pass
runErrorCheck = False
acceptedWord = False
accepted = False

totalPrice = 0

quitButton = button('Quit', 'center', 170, (0, 0, 0), (200, 200, 200), (0,0,0), 16, 'pygame.quit()', 'sys.exit()')
checkButton = button('Check availabilty', 220, 50, (0,0,0), (200,200,200), (0,0,0), 16, 'check()')
registerButton = button('Register plate', 'center', 107, (0,0,0), (200,200,200), (0,0,0), 16, 'register()')
inputBox = inputText(100, 50, 100, 'Type here...', (100,100,100), (200, 200, 200), (0, 0, 0), 16)
objects = pygame.sprite.Group()
objects.add(quitButton)
objects.add(checkButton)
objects.add(inputBox)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if inputBox.getLetters == True:
            if event.type == pygame.KEYDOWN:
                inputBox.letterList.append(event.key)
                
    update()

