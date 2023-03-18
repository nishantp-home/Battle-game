import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'   

class Person:

    attackDeviation = 10  #private constant

    def __init__(self, name, hitPoints, magicPoints, attack, defence, magic, items):
        self.name = name
        self.maxHitPoints = hitPoints
        self.hitPoints = hitPoints
        self.maxMagicPoints = magicPoints
        self.magicPoints = magicPoints
        self.attackHigh = attack + self.attackDeviation
        self.attackLow = attack - self.attackDeviation
        self.defence = defence
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']  #action at each turn

    #Different utility methods to handle different actions during a battle game
    def generateDamage(self):
        return random.randrange(self.attackLow, self.attackHigh)
    
    def takeDamage(self, damage):
        self.hitPoints -= damage
        if self.hitPoints < 0:
            self.hitPoints = 0
    
    def heal(self, healPoints):
        self.hitPoints += healPoints
        
    
    #utility funtions 
    def getHitPoints(self):
        return self.hitPoints
    
    def getMaxHitPoints(self):
        return self. maxHitPoints
    
    def getMagicPoints(self):
        return self.magicPoints
    
    def getMaxMagicPoints(self):
        return self.maxMagicPoints
    
    def reduceMagicPoints(self, cost):
        self.magicPoints -= cost
    

    def chooseAction(self):
        i = 1
        print(bcolors.BOLD + " ============================ "+ self.name + "'s turn" + " ============================ "+ bcolors.ENDC)
        print(bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        for action in self.actions:
            print("    " + str(i)+".", action)
            i += 1

        choice = input(bcolors.BOLD + "    Choose action:" + bcolors.ENDC)        
        index = int(choice) - 1
        return index
        

    def chooseSpell(self):
        i = 1
        print("        " + bcolors.BOLD +"MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print(bcolors.OKBLUE + "          " + str(i)+". ", spell.name, "(cost :", str(spell.cost)+")" + bcolors.ENDC)
            i += 1
        
        magicChoice = int(input(bcolors.BOLD + bcolors.OKBLUE + "          Choose spell:" + bcolors.ENDC)) - 1
        return magicChoice


    def chooseItems(self):
        i = 1
        print("        " +  bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print(bcolors.OKGREEN + "          " + str(i)+ ". " + item["item"].name, ":", item["item"].description,  "(x "+ str(item["quantity"]) + ")" + bcolors.ENDC)
            i += 1


    def getStats(self):

        hitPointsBar = ""
        magicPointsBar = ""
        hitPointsTicks = (self.hitPoints / self.maxHitPoints) * 25
        magicPointsTicks = (self.magicPoints / self.maxMagicPoints) * 10

        while hitPointsTicks > 0:
            hitPointsBar += "█"
            hitPointsTicks -= 1

        while magicPointsTicks > 0:
            magicPointsBar += "█"
            magicPointsTicks -=1

        
        while len(hitPointsBar) < 25:
            hitPointsBar += " "

        while len(magicPointsBar) < 10:
            magicPointsBar += " "

        hitPointsString = str(self.hitPoints) + "/" + str(self.maxHitPoints)
        magicPointString = str(self.magicPoints) + "/" + str(self.maxMagicPoints)
        maxHitPointStringLength = 9
        maxMagicPointStringLength = 5
        hitPointStringLength = len(hitPointsString)
        magicPointStringLength = len(magicPointString)

        hitPointSpaceCount = maxHitPointStringLength - hitPointStringLength
        magicPointSpaceCount = maxMagicPointStringLength - magicPointStringLength

        for i in range(hitPointSpaceCount):
            hitPointsString += " "
        
        for i in range(magicPointSpaceCount):
            magicPointString += " "

        print(bcolors.OKGREEN + self.name + ": " + 
              hitPointsString + " |" +  hitPointsBar  + "|"+ bcolors.ENDC +  
              bcolors.OKBLUE +"       " + magicPointString + " |" + magicPointsBar + "|" + bcolors.ENDC + "\n")


    def chooseTarget(self, enemies):
        
        if len(enemies) > 1:
            print(bcolors.BOLD + bcolors.FAIL+"    Enemies:" + bcolors.ENDC)
            i = 1
            for enemy in enemies:
                print("    " + bcolors.FAIL, str(i) + "." + enemy.name + bcolors.ENDC)
                i += 1
            enemyChoice = int(input("     " + bcolors.FAIL + bcolors.BOLD + "Choose enemy: " + bcolors.ENDC)) - 1 
        else:
            #print(bcolors.BOLD + bcolors.FAIL+"    Your enemy: " + enemies[0].name.replace(" ", ""),  bcolors.ENDC)
            enemyChoice = 0
        
        return enemyChoice


    def getEnemyStats(self):
        hitPointsBar = ""
        magicPointsBar = ""
        hitPointsTicks = (self.hitPoints / self.maxHitPoints) * 25
        magicPointsTicks = (self.magicPoints / self.maxMagicPoints) * 10

        while hitPointsTicks > 0:
            hitPointsBar += "█"
            hitPointsTicks -= 1

        while magicPointsTicks > 0:
            magicPointsBar += "█"
            magicPointsTicks -=1

        
        while len(hitPointsBar) < 25:
            hitPointsBar += " "

        while len(magicPointsBar) < 10:
            magicPointsBar += " "

        hitPointsString = str(self.hitPoints) + "/" + str(self.maxHitPoints)
        magicPointString = str(self.magicPoints) + "/" + str(self.maxMagicPoints)
        maxHitPointStringLength = 9
        maxMagicPointStringLength = 5
        hitPointStringLength = len(hitPointsString)
        magicPointStringLength = len(magicPointString)

        hitPointSpaceCount = maxHitPointStringLength - hitPointStringLength
        magicPointSpaceCount = maxMagicPointStringLength - magicPointStringLength

        for i in range(hitPointSpaceCount):
            hitPointsString += " "
        
        for i in range(magicPointSpaceCount):
            magicPointString += " "

        print(bcolors.FAIL + self.name + ": " + 
              hitPointsString + " |" +  hitPointsBar  + "|"+ bcolors.ENDC +  
              bcolors.HEADER +"       " + magicPointString + " |" + magicPointsBar + "|" + bcolors.ENDC + "\n")


    def chooseEnemySpell(self):
        magicChoice = random.randrange(0, len(self.magic))
        spell = self.magic[magicChoice]
        spellDamage = spell.generateSpellDamage()   
        percentageHitPoints = self.hitPoints / self.maxHitPoints * 100.0
        if self.magicPoints < spell.cost or spell.type == "white" and percentageHitPoints > 50:
            return self.chooseEnemySpell()
        else:
            return spell, spellDamage








