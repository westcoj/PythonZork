'''
Created on Nov 8, 2017

@author: Cody
'''
#!/usr/bin/env python
from Game import *

def main():
    game = Game()
    print ("Type Bag, Stats (HP and ATK), List (For Enemies), Move (Cardinal Direction) or Attack (Nerd Bombs, Kisses, Chocolate Bars, or Sour Straws)")
    print ("Starting game, your location: ")
    game.getMsg()
    
    while(1):
        game.command(game.getInput())
        game.getMsg()
        if(game.gameOver()):
            print ("Enemies Defeated, Celebrate Good Times, Have a Homebrew (Galaxy IPA preferebly)")
            break
        if(game.deadGuy()):
            print ("You Have Died")
            break
        
    
    
    
    

if __name__ == '__main__':
    main()
