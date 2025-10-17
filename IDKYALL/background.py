import pygame
import random
import constants as c

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(1,4)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color =(c.yellow)
        self.image.fill(c.yellow)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.screen_width)
        self.vel_x=0
        self.vel_y= random.randrange(4,16)
    
    def update (self):
        self.rect.x +=self.vel_x
        self.rect.y +=self.vel_y

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface(c.screen_size)
        self.color = (c.indigo)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = random.randrange(1,20)
    
    def update(self):
        self.stars.update()
        if self.timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.timer = random.randrange(1,20)
        for star in self.stars:
            if star.rect.y >= c.screen_height:
                self.stars.remove()
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1





