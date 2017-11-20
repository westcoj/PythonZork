"""
 * The following module sets up the Game class which contains all info needed to run
 * a game. Interprets user input on the console as strings and processes them
 * according to the game.
 *
 * @author Cody West
 * @version Zork Clone
 * @date 11/08/2017
"""
from Tile import *
from Player import *
from pip._vendor.distlib.compat import raw_input
from builtins import str
class Game:
    '''
    Sets up the neihborhood and player for the game. Interprets user input on the console as strings and processes them
    according to the game.
    '''


    def __init__(self):
        """Default constructer for Game, sets up neighborhood and player"""
        
        self.__map = Neighborhood()
        self.__player = Player()
        print("Welcome to the Neighborhood")
        self.__currSpot = self.__map.getGrid()[0][0]
        self.__currX = 0
        self.__currY = 0
        self.__currMsg = self.__map.getGrid()[0][0].getDesc() + "|[" + str(self.__currX) + "][" + str(self.__currY) + "]"
        

    def getInput(self):
        """Function for getting user input in non-graphical game

        Returns:
            Returns input from user

        """
        print("Type in a Command")
        msg = raw_input()
        return msg
    
    
    def playerMove(self, dirT):
        """Moves player in neighborhood in a specified direction

        Args:
            dirT: Cardinal direction to move

        Returns:
            True if the move is successful
            False if the move is illegal

        """
        x=0
        y=0
        if dirT == "North":
            x = -1
        elif dirT == "South":
            x = 1
        elif dirT == "West":
            y = -1
        elif dirT == "East":
            y= 1
        else:
            self.__currMsg = "Invalid Direction"
            return False
        if isinstance(self.__currSpot, House):
            if(self.__currSpot.clear()):
                if(self.__currX+x>=0 and self.__currX+x<=len(self.__map.getGrid())):
                    try:
                        if (self.__currY+y>=0 and self.__currY+y<len(self.__map.getGrid()[self.__currX+x])):
                            self.__currX += x
                            self.__currY += y
                            self.__currSpot = self.__map.getGrid()[self.__currX][self.__currY]
                            self.__currMsg = self.__currSpot.getDesc() + "|[" + str(self.__currX) + "][" + str(self.__currY) + "]"
                            return True
                        else:
                            self.__currMsg="Can't go that way"
                            return False
                    except IndexError:
                        self.__currMsg = "Can't go that way"
                        return False
                else:
                    self.__currMsg = "Can't go that way"
                    return False
            else:
                self.__currMsg = "Kill the monsters first"
                return False
                
        else:
            if(self.__currX+x>=0 and self.__currX+x<=len(self.__map.getGrid())):
                try:
                    if (self.__currY+y>=0 and self.__currY+y<len(self.__map.getGrid()[self.__currX+x])):
                        self.__currX += x
                        self.__currY += y
                        self.__currSpot = self.__map.getGrid()[self.__currX][self.__currY]
                        self.__currMsg = self.__currSpot.getDesc() + "|[" + str(self.__currX) + "][" + str(self.__currY) + "]"
                        return True
                    else:
                        self.__currMsg="Can't go that way"
                        return False
                except IndexError:
                    self.__currMsg = "Can't go that way" 
                    return False
            else:
                self.__currMsg = "Can't go that way"
                return False
                
                
            
            
    def getMsg(self):
        """prints current game message for non graphical game
        """
        print (self.__currMsg)
        
    def retMsg(self):
        """Gets game message for graphical game

        Returns:
            The game's current message

        """
        return self.__currMsg
        
    def getMap(self):
        """Gets game's map of the neighbohood

        Returns:
            The game's neighborhood

        """
        return self.__map
    
    def getLoc(self):
        """Gets player's spot in neighborhood

        Returns:
            Player's spot in neighborhood

        """
        return self.__currSpot
        
        
    def command(self, msg):
        """Interprets user's input for game and what input does

        Args:
            msg: Input from user


        """
        words = []
        words = msg.split()
        if len(words) == 0:
            self.__currMsg = "Type A Command, An Actual One"
            return
        if words[0] == "Move" or words[0] == "Go":
            if len(words)>1:
                if words[1] == "North" or words[1] == "South" or words[1] == "East" or words[1] == "West":
                    self.playerMove(words[1])
                else:
                    self.__currMsg = "Bad Command"
            else:
                self.__currMsg = "Bad Command"
        
        elif words[0] == "Attack":
            if len(words)>1:
                if words[1] == "Chocolate":
                    self.playerAttack("Chocolate Bars")
                elif words[1] == "Nerd":
                    self.playerAttack("Nerd Bombs")
                elif words[1] == "Sour":
                    self.playerAttack("Sour Straws")
                elif words[1] == "Kisses":
                    self.playerAttack("Hershey's Kisses")
                else:
                    self.__currMsg = "No Such Item"
            else:
                self.__currMsg = "Bad Command"
  
        elif words[0] == "Bag":
            invBag = ""
            for x in self.__player.getBag():
                invBag = invBag + x.getName() + ": " + str(x.getUses()) + "|"
                
            self.__currMsg = invBag
            
        elif words[0] == "List":
            listM = ""
            if isinstance(self.__currSpot, House):
                for x in self.__currSpot.getList():
                    listM = listM + x.getName() + ": " + str(x.getHP()) + "|"
                self.__currMsg = listM
            else:
                self.__currMsg = "There are no monsters here"
            
        elif words[0] == "Stats":
            self.__currMsg = "Player Health; " + str(self.__player.getHP()) + "|Attack: " + str(self.__player.getATK())
            
            
        else:
            self.__currMsg = "Bad Command"
        words = []
                
    def monsterAttack(self):
        """Function allowing monsters in current house to attack player

        Returns:
            Nothing, or string of attacking monsters

        """
        if isinstance(self.__currSpot, House):
            if(self.__currSpot.clear()):
                return
            else:
                atkList = []
                for x in self.__currSpot.getList():
                    x.attack(self.__player)
                    atkList.append(x.getName() + " attacks you for " + str(x.getAtk()) + " |")
                return atkList
        
                
    def playerAttack(self,weapon):
        """Allows player to attack monsters in a house

        Args:
            weapon: Type of weapon to attack with

        Returns:
            Nothing on failed attack

        """
        if self.__player.checkItems(weapon):
            wep = self.__player.getItem(weapon)
            if isinstance(self.__currSpot, House):
                if(self.__currSpot.clear()):
                    self.__currMsg = "Everything is dead already"
                    return
                for x in self.__currSpot.getList():
                    x.hurt(wep,self.__player)
                wep.setUse()
                if(wep.getUses() == 0):
                    self.__player.getBag().remove(wep)
                
                self.__currMsg = "You Attack the Monster(s)|| "
                if(not self.__currSpot.clear()):
                    atkList = self.monsterAttack()
                    for x in atkList:
                        self.__currMsg = self.__currMsg + x
            else:
                self.__currMsg = "There's Nothing Here"
        else:
            self.__currMsg = "You don't have that"
            
    def gameOver(self):
        """Checks to see if all houses are cleared


        Returns:
            True if monsters are dead
            False if they are not

        """
        for x in self.__map.getGrid():
            for y in x:
                if isinstance(y, House):
                    if not y.clear():
                        return False
        
        return True  
    
    def deadGuy(self):
        """Checks to see if player is dead


        Returns:
            True if player is dead
            False if they are not

        """
        if(self.__player.getHP() <= 0):
            return True
        return False