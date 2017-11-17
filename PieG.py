'''
Created on Nov 16, 2017

@author: Cody
'''
import pygame
from pygame.locals import *
from Tile import *
from Game import *
import textwrap
"""textrect Module provided by David Clark (da_clark at shaw.ca), used for textbox management. http://www.pygame.org/pcr/text_rect/index.php"""
import textrect


imageTile = pygame.image.load('blank.png')
imageHouse = pygame.image.load('house.png')
imageTileP = pygame.image.load('blankP.png')
imageHouseP = pygame.image.load('houseP.png')

class gameGui:
    
    def __init__(self):
        self.__game = Game()
        
    
    def createScreen(self):
        self.__screen = pygame.display.set_mode((1200, 800));
        self.__screen.fill((255, 255, 255))
        z = 0;
        t = 0;
        for x in self.__game.getMap().getGrid():
            for y in x:
                if isinstance(y, House):
                    self.__screen.blit(imageHouse, (t, z))
                    t = t + 155
                else:
                    self.__screen.blit(imageTile, (t, z))
                    t = t + 155
            z = z + 155
            t = 0
        
        self.__posX = 0
        self.__posY = 0
        self.__textBox = pygame.draw.rect(self.__screen, (255, 255, 255), (500, 10, 600, 400), 2)
        if isinstance(self.__game.getLoc(), House):
            self.__screen.blit(imageHouseP, (self.__posX, self.__posY))
        else:
            self.__screen.blit(imageTileP, (self.__posX, self.__posY))
            
    def reDraw(self):
        self.__screen.fill((255, 255, 255))
        z = 0;
        t = 0;
        for x in self.__game.getMap().getGrid():
            for y in x:
                if(self.__game.getLoc()==y):
                    if isinstance(y, House):
                        self.__screen.blit(imageHouseP, (t, z))
                        t = t + 155
                    else:
                        self.__screen.blit(imageTileP, (t, z))
                        t = t + 155
                else:
                    if isinstance(y, House):
                        self.__screen.blit(imageHouse, (t, z))
                        t = t + 155
                    else:
                        self.__screen.blit(imageTile, (t, z))
                        t = t + 155
            z = z + 155
            t = 0
            
    def runGame(self):
        self.createScreen()
        pygame.init()
        self.__font = pygame.font.Font(None, 24)
        clock = pygame.time.Clock()
        pygame.display.flip()
        pygame.event.clear()
        self.__endText = "Game Over"
        self.__helpText = """Use arrows to move, B for Bag, S for Stats, Z for Hershey's Kisses, X For Nerds, C for Sour Straws, and V for Chocolate Bars. Press H to see this again, Q to quit, W to see where you are, and M for a list of monsters."""
        rendered_text = textrect.render_textrect(self.__helpText, self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
        if rendered_text:
            self.__screen.blit(rendered_text, self.__textBox.topleft)
        while pygame.event.wait().type != pygame.locals.QUIT:
            clock.tick(60)
            key = pygame.key.get_pressed()
            self.getInput(key)
            pygame.display.flip()
            pygame.event.clear()
            clock.tick(60)
            if(self.__game.deadGuy() or self.__game.gameOver()):
                if(self.__game.deadGuy()):
                    self.__endText = "You've been defeated, bad luck mate, press Q to quit"
                    rendered_text = textrect.render_textrect(self.__endText, self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
                    if rendered_text:
                        self.__screen.blit(rendered_text, self.__textBox.topleft)
                    
                if(self.__game.gameOver()):
                    self.__endText = "You've killed all the monsters, good job. Press Q to quit"
                    rendered_text = textrect.render_textrect(self.__endText, self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
                    if rendered_text:
                        self.__screen.blit(rendered_text, self.__textBox.topleft)
        
     
    def getInput(self, key):
        oldLoc = self.__game.getLoc()
        if key[pygame.K_UP]:
            valid = self.__game.playerMove("North")
            self.__game.getMsg()
            self.reDraw()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
            
                 
        if key[pygame.K_DOWN]:
            valid = self.__game.playerMove("South")
            self.__game.getMsg()
            self.reDraw()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
 
                    
        if key[pygame.K_LEFT]:
            valid = self.__game.playerMove("West")
            self.__game.getMsg()
            self.reDraw()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
                
        if key[pygame.K_RIGHT]:
            valid = self.__game.playerMove("East")
            self.__game.getMsg()
            self.reDraw()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
                    
                
        if key[pygame.K_s]:
            self.__game.command("Stats")
            self.__game.getMsg()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
        if key[pygame.K_b]:
            self.__game.command("Bag")
            self.__game.getMsg()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
        if key[pygame.K_z]:
            self.__game.command("Attack Kisses")
            self.__game.getMsg()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
        if key[pygame.K_x]:
            self.__game.command("Attack Sour")
            self.__game.getMsg()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
        if key[pygame.K_c]:
            self.__game.command("Attack Chocolate")
            self.__game.getMsg()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
        if key[pygame.K_v]:
            self.__game.command("Attack Nerd")
            self.__game.getMsg()
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
        if key[pygame.K_h]:
            rendered_text = textrect.render_textrect(self.__helpText, self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
        if key[pygame.K_w]:
            rendered_text = textrect.render_textrect(self.__game.getLoc().getDesc(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
        if key[pygame.K_m]:
            self.__game.command("List")
            rendered_text = textrect.render_textrect(self.__game.retMsg(), self.__font, self.__textBox, (255, 255, 255), (0, 0, 0), 0)
            if rendered_text:
                self.__screen.blit(rendered_text, self.__textBox.topleft)
                
        if key[pygame.K_q]:
            pygame.display.quit()
            pygame.quit()
            quit()
        




    # CODE THAT IS NOT MINE
    
if __name__ == '__main__':
    newGame = gameGui()
    newGame.runGame()
