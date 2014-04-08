# --- Text Based Car Plate Registration System --- #

#This class handles conversion between letters and numbers.
class conversion():
    #Goes through string and checks if any numbers can be changed to a letter, if it can, it will add to a list and return a string of that list.
    def numbersToLetters(self, string):
        "Converts numbers to letters; returns string"
        self.list = []
        for i in range(len(string)):
            if string[i] == '0':
                self.list.append('o')
            if string[i] == '1':
                self.list.append('l')
            if string[i] == '3' or string[i] == '5':
                self.list.append('e')
            if string[i] == '8':
                self.list.append('b')
            else:
                self.list.append(string[i])
        return ''.join(self.list)
    #Goes through string and checks if any letters can be changed to numbers, if it can, it will add to a list and return a string of that list.
    def lettersToNumbers(self, string):
        "Converts letters to numbers; returns string"
        self.list = []
        for i in range(len(string)):
            if string[i] == 'o':
                self.list.append('0')
            if string[i] == 'i' or string[i] == 'l':
                self.list.append('1')
            if string[i] == 'e':
                self.list.append('5')
            if string[i] == 'b':
                self.list.append('8')
            else:
                self.list.append(string[i])
        return ''.join(self.list)

#This class handles the cross referencing of various strings and text files.
class check():
    #Checks if string is in registered plates text file
    def registered(self, string):
        "Checks if string is in registered plates file; returns boolean"
        self.registeredPlates = open('registeredPlates.txt').read().splitlines()
        if string in self.registeredPlates:
            return True
        else:
            return False
    #Checks if string is in restricted plates text file
    def restricted(self, string):
        "Checks if string is in restricted plates file; returns boolean"
        self.restrictedWords = open('restrictedWords.txt').read().splitlines()
        if string in self.restrictedWords:
            return True
        else:
            return False
    #Checks if string is in dictionary text file
    def word(self, string):
        "Checks if string is in dictionary; returns boolean"
        self.wordList = open('wordList.txt').read().splitlines()
        if string in self.wordList:
            return True
        else:
            return False

#Sets object names.
conversion = conversion()
check = check()

#Initialises variables
successfulRegistrations = 0
failedRegistrations = 0
totalCost = 0

#Loop
while successfulRegistrations < 10 and failedRegistrations < 10:
    plate = input('Enter plate: ')
    
    #User exiting function
    if plate == 'exit':
        break

    #Lowers characters in 'plate' and sets to new variable 'loweredPlate'
    plateList = []
    for i in range(len(plate)):
        try:
            plateList.append(plate[i].lower())
        except:
            plateList.append(plate[i])
    loweredPlate = ''.join(plateList)

    plateWord = conversion.numbersToLetters(loweredPlate)

    #Checks if plate can be registered, if not: will restart loop
    if check.registered(plate) == True:
        print('Not available due to previously registered plate.')
        failedRegistrations += 1
        continue
    if check.restricted(plateWord) == True:
        print('Not available due to restricted word.')
        failedRegistrations += 1
        continue
    
    else:
        #Writes plate to text file
        registeredPlates = open('registeredPlates.txt', 'r+')
        registeredPlates.seek(0, 2)
        registeredPlates.write(plate + '\n')
        registeredPlates.close()
        
        print('plate word is', plateWord)

        #Checks if 'plateWord' is in dicitionary, if it is: price is raised
        if check.word(plateWord):
            cost = 130
        else:
            cost = 85
            
        print('Plate costs: $' + str(cost))
        totalCost += cost
        successfulRegistrations += 1

#Prints successful registrations, if there arent any, it will output
if successfulRegistrations > 0:
    print(successfulRegistrations, '$' + str(totalCost))
else:
    print('No registrations.')
