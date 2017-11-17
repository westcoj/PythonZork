'''
Created on Nov 8, 2017

@author: Cody
'''
import random
from Observer import Observable

class Monster(Observable):
    '''
    classdocs
    '''


    def __init__(self, atk, health, name):
        '''
        Constructor
        '''
        self.__atk = atk
        self.__health = health
        self.__name = name
        self.observers = [] #Possibly __ but not sure
        

    def attack(self,player):
        player.hit(self.__atk);
        
    
    def hurt(self,atkVal,player):
        self.__health -= atkVal*player.getATK();
        for observer in self.observers:
            observer.update(self.__health,self)
        
    def __str__(self, *args, **kwargs):
        return self.__name
    
    def getAtk(self):
        return self.__atk
    
    def getHP(self):
        return self.__health
    
    def getName(self):
        return self.__name
        
        
        
class Zombie(Monster):
    '''
    doxs
    '''
    
    def __init__(self):
        atkVal = random.randint(0,10)
        healthVal = random.randint(50,100)
        nameVal = "Zombie"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        super().attack(player)
        
    def hurt(self,weapon,player):
        if weapon.getName() == "SourStraws":
            atkVal3 = weapon.damage()*2
        else:
            atkVal3 = weapon.damage()
        super().hurt(atkVal3,player)
        
class Vampire(Monster):
    '''
    doxs
    '''
    
    def __init__(self):
        atkVal = random.randint(10,20)
        healthVal = random.randint(100,200)
        nameVal = "Vampire"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        super().attack(player)
        
    def hurt(self,weapon,player):
        if weapon.getName() == "ChocolateBars":
            atkval3 = 0;
        else:
            atkVal3 = weapon.damage()
            
        super().hurt(atkVal3,player)
        
class Ghoul(Monster):
    '''
    doxs
    '''
    
    def __init__(self):
        atkVal = random.randint(15,30)
        healthVal = random.randint(40,80)
        nameVal = "Ghoul"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        super().attack(player)
        
    def hurt(self,weapon,player):
        if weapon.getName() == "NerdBombs":
            atkval3 = weapon.damage() * 5
        else:
            atkVal3 = weapon.damage()
            
        super().hurt(atkVal3,player)
        
class Werewolf(Monster):
    '''
    doxs
    '''
    
    def __init__(self):
        atkVal = random.randint(0,40)
        healthVal = 200
        nameVal = "Werewolf"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        super().attack(player)
        
    def hurt(self,weapon,player):
        if weapon.getName() == "ChocolateBars" or weapon.getName() == "SourStraws":
            atkval3 = 0;
        else:
            atkVal3 = weapon.damage()
            
        super().hurt(atkVal3,player)
        

class Person(Monster):
    '''
    doxs
    '''
    
    def __init__(self):
        atkVal = -3
        healthVal = 100
        nameVal = "Person"
        super().__init__(atkVal, healthVal, nameVal)
        
    def attack(self,player):
        super().attack(player)
        
    def hurt(self,weapon,player):
        super().hurt(0,player)

        
    