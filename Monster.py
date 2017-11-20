"""
 * The following module contains the monster classes for the game that the 
 * player fights against. Different monsters have different values and
 * weaknesses.
 *
 * @author Cody West
 * @version Zork Clone
 * @date 11/08/2017
"""
import random
from Observer import Observable

class Monster(Observable):
    '''
    Super class for monsters to use
    '''


    def __init__(self, atk, health, name):
        '''
        Default constructer for all monsters
        '''
        self.__atk = atk
        self.__health = health
        self.__name = name
        self.observers = [] #Possibly __ but not sure
        

    def attack(self,player):
        """Attacks player for monsters damage value

        Args:
            player: the player to attack

        """
        player.hit(self.__atk);
        
    
    def hurt(self,atkVal,player):
        """Damages monster based on pased values

        Args:
            player: the player that's attacking
            atkVal: Damage modifier of the weapon used

        """
        self.__health -= atkVal*player.getATK();
        for observer in self.observers:
            observer.update(self.__health,self)
        
    def __str__(self, *args, **kwargs):
        """Prints name of monster

        Returns:
            Name of monster
        """
        return self.__name
    
    def getAtk(self):
        """Gets attack value of monster

        Returns:
            Attack of monster
        """
        return self.__atk
    
    def getHP(self):
        """Gets health value of monster

        Returns:
            Health of monster
        """
        return self.__health
    
    def getName(self):
        """Gets name value of monster

        Returns:
            Name of monster
        """
        return self.__name
        
        
        
class Zombie(Monster):
    '''
    Zombie monster that attacks the player. Weak to sour straws
    '''
    
    def __init__(self):
        """
        Constructer that sets up a zombie style monster
        """
        atkVal = random.randint(0,10)
        healthVal = random.randint(50,100)
        nameVal = "Zombie"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        """Attacks player for damage value

        Args:
            player: the player to attack

        """
        super().attack(player)
        
    def hurt(self,weapon,player):
        """Determines damage value of weapon and passes to super method

        Args:
            player: the player that's attacking
            weapon: Type of weapon used

        """
        if weapon.getName() == "SourStraws":
            atkVal3 = weapon.damage()*2
            
        else:
            atkVal3 = weapon.damage()
        super().hurt(atkVal3,player)
        
class Vampire(Monster):
    '''
    Vampire monster that attacks the player, immune to chocolate bars
    '''
    
    def __init__(self):
        """
        Constructer that sets up a vampire style monster
        """
        atkVal = random.randint(10,20)
        healthVal = random.randint(100,200)
        nameVal = "Vampire"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        """Attacks player for damage value

        Args:
            player: the player to attack

        """
        super().attack(player)
        
    def hurt(self,weapon,player):
        """Determines damage value of weapon and passes to super method

        Args:
            player: the player that's attacking
            weapon: Type of weapon used

        """
        if weapon.getName() == "ChocolateBars":
            atkval3 = 0;
            
        else:
            atkVal3 = weapon.damage()
            
        super().hurt(atkVal3,player)
        
class Ghoul(Monster):
    '''
    Ghoul monster that attacks the player, weak to Nerd Bombs
    '''
    
    def __init__(self):
        """
        Constructer that sets up a ghoul style monster
        """
        atkVal = random.randint(15,30)
        healthVal = random.randint(40,80)
        nameVal = "Ghoul"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        """Attacks player for damage value

        Args:
            player: the player to attack

        """
        super().attack(player)
        
    def hurt(self,weapon,player):
        """Determines damage value of weapon and passes to super method

        Args:
            player: the player that's attacking
            weapon: Type of weapon used

        """
        if weapon.getName() == "NerdBombs":
            atkval3 = weapon.damage() * 5
            
        else:
            atkVal3 = weapon.damage()
            
        super().hurt(atkVal3,player)
        
class Werewolf(Monster):
    '''
    Werewolf monster that attacks the player, immune to Sour Straws and Chocolate Bars
    '''
    
    def __init__(self):
        """
        Constructer that sets up a werewolf style monster
        """
        atkVal = random.randint(0,40)
        healthVal = 200
        nameVal = "Werewolf"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        """Attacks player for damage value

        Args:
            player: the player to attack

        """
        super().attack(player)
        
    def hurt(self,weapon,player):
        """Determines damage value of weapon and passes to super method

        Args:
            player: the player that's attacking
            weapon: Type of weapon used

        """
        if weapon.getName() == "ChocolateBars" or weapon.getName() == "SourStraws":
            atkVal3 = 0;
            
        else:
            atkVal3 = weapon.damage()
            
        super().hurt(atkVal3,player)
        

class Person(Monster):
    '''
    Person who attacks the player with a negative value, healing them. Immune to all weapons
    '''
    
    def __init__(self):
        """
        Constructer that sets up a person style monster
        """
        atkVal = -3
        healthVal = 100
        nameVal = "Person"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        """Attacks player for (negative) damage value

        Args:
            player: the player to attack

        """
        super().attack(player)
        
    def hurt(self,weapon,player):
        """Determines damage value of weapon and passes to super method
            People cannot be hurt no matter what weapon is used

        Args:
            player: the player that's attacking
            weapon: Type of weapon used

        """
        super().hurt(0,player)

        
    