from classes.game import bcolors, Person
from classes.magic import Spell
from classes.items import Item
import random

# Create magic spells ==============================================================
#black magic
fire = Spell('Fire', 10, 60, "black")
thunder = Spell('Thunder', 20, 120, "black")
blizzard = Spell('Blizzard', 30, 120, "black")
meteor = Spell('Meteor', 25, 120, "black")
quake = Spell('Quake', 14, 140, "black")

#white magic 
cure = Spell('Cure', 10, 120)
cura = Spell('Cura', 18, 200)
curaga = Spell('Curaga', 35, 500)

#Create items =====================================================================================
potion = Item("Potion", "potion", "Heals for 50 points", 50)
hipotion = Item("Hi-Potion", "potion", "Heals for 100 points", 100)
superpotion = Item("super-Potion", "potion", "Heals for 100 points", 500)
elixer = Item("Elixer", "elixer", "Fully restores Hit/Magic points of one party member", 9999)
hielixer = Item("Mega-Elixer", "elixer", "Fully restores Hit/Magic points of party", 9999)
grenade = Item("Grenade", "attack", "Deals 500 points of damage", 500)


#List of player's magic spells 
player1Magic = [fire, cure]
player2Magic = [thunder, cure]

#List of player items and their quantity
player1Items = [{"item": potion, "quantity": 2}, 
               {"item": elixer, "quantity": 2},
               {"item": grenade, "quantity": 2}]

player2Items = [{"item": potion, "quantity": 5}, 
               {"item": hielixer, "quantity": 3}, 
               {"item": grenade, "quantity": 2}]

#Instantiate persons
player1 = Person("Nishant",1160, 140, 100, 60, player1Magic, player1Items)
player2 = Person("  Purvi",1280, 120, 80, 60, player2Magic, player2Items)

players = [player1, player2]    

enemyChoiceOptions = 2  #Attack, Magic
enemyMagic = [fire, thunder, cure, curaga]

enemy1 = Person("  Ravan", 1200, 200, 150, 43, enemyMagic, [])
enemy2 = Person("   Kans", 1000, 180, 120, 43, enemyMagic, [])

enemies = [enemy1, enemy2]

running = True

#Driver code for the game ================================================
while running:
    print(bcolors.BOLD + "Player              Hit points                              Magic points")
    print("-----------------------------------------------------------------------------" + bcolors.ENDC)
    for player in players:
        player.getStats()

    for enemy in enemies:
        enemy.getEnemyStats()

    for player in players:
        print(bcolors.BOLD + "-----------------------------------------------------------------------------" + bcolors.ENDC)
        index = player.chooseAction()

        if index == 0:
            damage = player.generateDamage()
            enemy = player.chooseTarget(enemies)
            enemies[enemy].takeDamage(damage)

            if enemies[enemy].getHitPoints() == 0:
                print(bcolors.OKGREEN + bcolors.BOLD + enemies[enemy].name, "dead !" + bcolors.ENDC)
                del enemies[enemy]
                if len(enemies) == 0:
                    continue 
            
            print(bcolors.OKGREEN + "     " + player.name.replace(" ", "") + " attacked " + enemies[enemy].name.replace(" ", "") + " for", str(damage), "points",bcolors.ENDC)

        elif index == 1:
            magicChoice = player.chooseSpell()
                                
            if magicChoice == -1:
                continue

            spell = player.magic[magicChoice]
            spellDamage = spell.generateSpellDamage()

            currentMagicPoints = player.getMagicPoints()
            if spell.cost > currentMagicPoints:
                print(bcolors.FAIL + bcolors.BOLD + "Insufficient magic points" + bcolors.ENDC)
                continue

            player.reduceMagicPoints(spell.cost)

            if spell.type == "white":
                player.heal(spellDamage)
                print(bcolors.OKGREEN + player.name, "chose to heal with " + spell.name + " for " + str(spellDamage) + " points" + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.chooseTarget(enemies)
                enemies[enemy].takeDamage(spellDamage)
                print("          " + bcolors.OKGREEN + player.name.replace(" ", "") + " attacked " + enemies[enemy].name.replace(" ", "") + " with " + bcolors.BOLD + spell.name.replace(" ", "") + " for " + str(spellDamage) + " points" + bcolors.ENDC)

                if enemies[enemy].getHitPoints() == 0:
                    print(bcolors.OKGREEN + bcolors.BOLD + enemies[enemy].name.replace(" ", ""), "dead !" + bcolors.ENDC)
                    del enemies[enemy] 

        elif index == 2:
            player.chooseItems()
            itemChoice = int(input(bcolors.BOLD + bcolors.OKGREEN +  "        Choose item:" + bcolors.ENDC)) - 1
            if itemChoice == -1:
                continue

            if player.items[itemChoice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "No " + player.items[itemChoice]["item"].name.replace(" ", ""), "left !" + bcolors.ENDC)
                continue

            player.items[itemChoice]["quantity"] -= 1
            item = player.items[itemChoice]["item"]
        
            if item.type == "potion":
                player.heal(item.property)
                print(bcolors.OKGREEN + "        " + item.name.replace(" ", ""), "heals " + player.name.replace(" ", "") + " for", item.property, "points"+ bcolors.ENDC)
                player.getStats()

            elif item.type == "elixer":
                if item.name == "Mega-Elixer":
                    print(bcolors.OKGREEN + bcolors.BOLD + "Fully restores hit and magic points for all players" + bcolors.ENDC)
               
                    for i in players:
                        i.hitPoints = i.maxHitPoints
                        i.magicPoints = i.maxMagicPoints
                        i.getStats()
                
                else:
                    player.hitPoints = player.maxHitPoints
                    player.magicPoints = player.maxMagicPoints
                    print(bcolors.OKGREEN + bcolors.BOLD + "Fully restores hit and magic points for " + player.name + bcolors.ENDC)
                    player.getStats()
                continue

            elif item.type == "attack":
                enemy = player.chooseTarget(enemies)
                enemies[enemy].takeDamage(item.property)
                print("        " + bcolors.OKGREEN + player.name.replace(" ", ""), "attacked " + enemies[enemy].name.replace(" ", "") + " with", item.name.replace(" ", ""), "for", item.property, "points"+ bcolors.ENDC)
                
                if enemies[enemy].getHitPoints() == 0:
                    print(bcolors.OKGREEN + bcolors.BOLD + enemies[enemy].name.replace(" ", ""), "dead !" + bcolors.ENDC)
                    del enemies[enemy] 


        else:
            print(bcolors.FAIL + bcolors.BOLD + "Possible choices: 1, 2 or 3" + bcolors.ENDC)
            continue

# When you win  ======================================================================================================================
    defeatedEnemyCount = 0
    for enemy in enemies:
        if enemy.getHitPoints() == 0:
            defeatedEnemyCount += 1
    
    if defeatedEnemyCount == len(enemies):
        print(bcolors.OKGREEN + bcolors.BOLD + "You won ! Game over. " + bcolors.ENDC)
        running = False

# Enemy action =============================================================================================================================
    for enemy in enemies:
        enemyChoice = random.randrange(0, enemyChoiceOptions)

        if enemyChoice == 0:
            enemyDamage = enemy.generateDamage()
            target = random.randrange(0, len(players))
            players[target].takeDamage(enemyDamage)

            print("\n" + bcolors.FAIL + enemy.name + " attacked " + players[target].name.replace(" ", "") + 
                  " for", str(enemyDamage) + " points" +bcolors.ENDC +"\n")
        elif enemyChoice == 1:
            spell, magicDamage = enemy.chooseEnemySpell()
            enemy.reduceMagicPoints(spell.cost)

            if spell.type == "white":
                enemy.heal(magicDamage)
                print(bcolors.OKGREEN + enemy.name.replace(" ", ""), "chose to heal with " + spell.name.replace(" ", "") + " for " + str(magicDamage) + " points" + bcolors.ENDC)
            elif spell.type == "black":
                target = random.randrange(0, len(players))
                players[target].takeDamage(magicDamage)
                print(bcolors.FAIL + enemy.name.replace(" ","") + " attacked " + players[target].name.replace(" ", "") + " with " + bcolors.BOLD + spell.name.replace(" ", "") + " for " + str(magicDamage) + " points" + bcolors.ENDC)

                if players[target].getHitPoints() == 0:
                    print(bcolors.FAIL + bcolors.BOLD + players[target].name.replace(" ", ""), " dead !" + bcolors.ENDC)
                    del players[target]

# When you lose  ======================================================================================================================
    defeatedPlayerCount = 0
    for player in players:
        if player.getHitPoints() == 0:
            defeatedPlayerCount += 1
        
    if defeatedPlayerCount == len(players):
        print(bcolors.FAIL + bcolors.BOLD + "You lose ! Game over." + bcolors.ENDC)
        running = False

            




