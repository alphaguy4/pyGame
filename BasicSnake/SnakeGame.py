#lets get Started
import pygame
import os, sys
from pygame.locals import *
from helpers import *
if not pygame.font: print 'Warning, font disabled'
if not pygame.mixer: print 'Warning,sound disabled'

class PyManMain:
    """The Main PyMan Class-This class handles the main initialization 
        and 
        creating of the Game."""
    def __init__(self,width=640,height=480):
        # Initialize
        # Initialize PyGame
        pygame.init();
        """Set Window size"""
        self.width = width
        self.height = height
        """Create screen """
        self.screen = pygame.display.set_mode((self.width,self.height))

    def LoadSprites(self):
        """Load the sprites that we need"""
        self.snake = Snake()
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
        """figure out how many pellets we can display """
        nNumHorizontal = int(self.width/64)
        nNumVertical = int(self.height/64)
        """create pellet groups"""
        self.pellet_sprites = pygame.sprite.Group()
        """Create all of the pellets and add them to the pellet_sprites group"""
        for x in range(nNumHorizontal):
            for y in range(nNumVertical):
                self.pellet_sprites.add(Pellet(pygame.Rect(x*64,y*64,64,64)))    

    def Mainloop(self):
        """This is main loop of the Game """
        """Load All of the sprites"""
        self.LoadSprites()
        pygame.key.set_repeat(500,30)
        
        """create the background """
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT) or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN)):
                        self.snake.move(event.key)
            self.snake_sprites.draw(self.screen)
            pygame.display.flip()
            """check for collion """
            lstCols = pygame.sprite.spritecollide(self.snake,self.pellet_sprites,True)
            """Update the amount of pellets eaten """
            self.snake.pellets = self.snake.pellets + len(lstCols)
            
            """Do Drawing """
            self.screen.blit(self.background, (0,0))
            if pygame.font:
                font = pygame.font.Font(None,36)
                text = font.render("Score : %s" %self.snake.pellets,1,(255,0,0))
                textpos = text.get_rect(centerx=self.background.get_width()/2)
                self.screen.blit(text,textpos)
            """Draw pellet """
            self.pellet_sprites.draw(self.screen)
            self.snake_sprites.draw(self.screen)
            pygame.display.flip()

            
class Snake(pygame.sprite.Sprite):
    """This is our snake that will move around the screen"""
    def __init__(self):
        self.x_dist = 2
        self.y_dist = 2
        pygame.sprite.Sprite.__init__(self)
        self.image,self.rect = load_image('snake.png',-1)
        self.pellets = 0  #initially score zero
    def move(self,key):
        """Move your self in one of the 4 directions according to the key """
        """key for pygame is define for either up,down,left or right key """
        """Adjusting direction by ourself"""
        xMove =0;
        yMove =0;
        
        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        self.rect.move_ip(xMove,yMove);

class Pellet(pygame.sprite.Sprite):
    
    def __init__(self,rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.image,self.rect = load_image('pellet.png',-1)
        if rect != None:
            self.rect = rect
if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.Mainloop()        
