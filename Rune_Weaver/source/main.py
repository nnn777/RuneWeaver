#Rune Weaver v. 0.01
#Copyright (c) 2013 - 2014 RevertedSoft <revertedsoft.com>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation file (the "Software"), to deal
#with the Software without limitation in the rights to use, copy, modify, merge
#publish, distribute, but NOT to sell copies of the Software, subject to the
#following condition:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

""" This module holds the main method."""

import pygame, sys
from pygame.locals import *
from . import pygcurse, equipment, player, creature, ui
from .globs import *

#create the player variable ###PLACEHOLDER###
playerChar = player.Player("player",20,5,'@','red',factionDict['player'],10,10,10,10,10,10,0,50)

#create new creatures ###TODO### TEMPORARY

newCreature1 = creature.Humanoid("goblin", 15,5,'G', "green", experience=10, ai="passive", faction=factionDict["goblins"])
newCreature2 = creature.Humanoid("goblin", 25,5,'G', "green", experience=10, ai="defensive", faction=factionDict["goblins"])
newCreature3 = creature.Humanoid("goblin", 15,10,'G', "green", experience=10, ai="defensive", faction=factionDict["goblins"])
newCreature4 = creature.Humanoid("Orc", 13,12,'O', "blue", strength=12, constitution=12, faction=factionDict["monsters"], ai="wanderer", weapon = WEAPONLIST[1])
newCreature5 = creature.Humanoid("Hobgoblin", 16,12,'H', "green", strength=17, constitution=15, faction=factionDict["goblins"], ai="wanderer", weapon = WEAPONLIST[1], torsoArmor=ARMORLIST[1])
newCreature6 = creature.Humanoid("Orc", 19,12,'O', "blue", strength=12, constitution=12, faction=factionDict["monsters"], ai="wanderer", weapon = WEAPONLIST[1])

creatureList = []
creatureList.append(playerChar)
creatureList.append(newCreature1)
creatureList.append(newCreature2)
creatureList.append(newCreature3)
creatureList.append(newCreature4)
creatureList.append(newCreature5)
creatureList.append(newCreature6)

def exitGame():
    pygame.quit()
    sys.exit()

def main():
    

    testButton = ui.Button((1,2), (10,3), win, [ui.Text("Test",(1,1))], True, (255,0,0), (0,0,255), (255,0,0))

    userinterface = ui.Menu((40,0), (20,40), win, [ui.Text("Player",(1,1))], True, (0,255,0), [testButton])
    

    play = [True, True]

    while play[0] == True:
        
        
        dungeon.printWorld(win, creatureList, BLACK)
        #change the userinterface every iteration
        userinterface.alterText([ui.Text(playerChar.name + " HP:" + str(playerChar.currentHealth) + "/" + str(playerChar.maxHealth),(1,1)), ui.Text("STR: " + str(playerChar.strength), (1,5)), ui.Text("CON: " + str(playerChar.constitution), (1,6)), ui.Text("DEX: " + str(playerChar.dexterity), (1,7)), ui.Text("AGI: " + str(playerChar.agility), (1,8)), ui.Text("INT: " + str(playerChar.intelligence), (1,9)), ui.Text("WIS: " + str(playerChar.wisdom), (1,10)), ui.Text("Armor: " + str(playerChar.armor),(1,11))])
        userinterface.printMenu()
        eventLog.printUI()
        inputBox.printUI()
        win.update()
        win.fill((' '))
        if play[1] == True:
            play = playerChar.turn(creatureList)
        else:
            for creatures in creatureList[1:]:
                ai = creatures.ai(creatures, creatureList, dungeon)
                ai.behavior()
                if creatures.dead:
                    creatureList.remove(creatures)
                play[1] = True
        

    exitGame()
