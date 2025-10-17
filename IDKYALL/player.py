import pygame
from bullet import Shottype_1, Shottype_2
import constants as c

class Player(pygame.sprite.Sprite):
    def __init__(self, hitbox):
        super(Player, self).__init__()
        self.image = pygame.image.load("assets/pixil-frame-0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.speed = c.set_speed
        self.bullets = pygame.sprite.Group()
        self.rect.x=280
        self.rect.y=600
        self.hitbox = hitbox
        self.lives = c.set_life
        self.timer = 8
        self.hits = 0
        self.cooldown = False
        self.cooldown_timer = 0
        self.max_cooldown = c.fps * 2
       
    
    
    def shoot(self):
        new_bullet1 = Shottype_1()
        new_bullet2 = Shottype_2()
        new_bullet1.rect.x = self.rect.x + 5
        new_bullet1.rect.y = self.rect.y
        new_bullet2.rect.x = self.rect.x + 50
        new_bullet2.rect.y = self.rect.y 
        self.bullets.add(new_bullet1, new_bullet2)

   
   
   
   

    def update(self):

        if self.lives > 0:
            self.timer-=1
        
        if self.timer == 0:
            self.shoot()
            self.timer = 8

        self.bullets.update()
        self.hitbox.follow(self.rect)
        
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.screen_width - self.rect.width:
            self.rect.x = c.screen_width - self.rect.width 
    
        if self.rect.y <= 0:
            self.rect.y = 0 
        elif self.rect.y >= c.screen_height - self.rect.height:
            self.rect.y = c.screen_height - self.rect.height
        
        if self.cooldown_timer >= 0:
            self.cooldown_timer -= 1 
        else:
            self.cooldown = False

class HB(pygame.sprite.Sprite):
    def __init__(self):
        super(HB, self).__init__()
        self.width = 10
        self.height = 10
        self.size = (self.width,self.height)
        self.image = pygame.Surface(self.size)
        self.color = (c.white)
        self.image.fill(c.blue)
        pygame.draw.circle(self.image, self.color, (self.width//2, self.height//2), 5)
        self.rect = self.image.get_rect()
        self.rect.x = 311.5
        self.rect.y = 640
        self.lives = c.set_life
        self.is_alive = True
        self.timer = 0

    
    def get_hit(self):
        if self.timer == 0:
            self.timer =  c.fps * 2
            self.image = pygame.Surface(self.size)
            self.color = (c.red)
            self.image.fill(c.blue)
            pygame.draw.circle(self.image, self.color, (self.width//2, self.height//2), 5)
            self.rect = self.image.get_rect()


    

    
    def follow(self, player_rect):
        self.rect.centerx = player_rect.centerx + 2
        self.rect.centery = player_rect.centery + 10
    
    #def death(self):
        #if self.lives == 0:
            #self.is_alive = False
            #self.image = pygame.Surface((0,0))




    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else: 
            self.color = c.white
            self.image = pygame.Surface(self.size)
            self.image.fill(c.blue)
            pygame.draw.circle(self.image, self.color, (self.width//2, self.height//2), 5)
            self.timer = 0


        if self.rect.x <= 30:
            self.rect.x = 30
        elif self.rect.x >= c.screen_width - 35:
            self.rect.x = c.screen_width - 35 
    
        if self.rect.y <= 39:
            self.rect.y = 39
        elif self.rect.y >= c.screen_height - 35:
            self.rect.y = c.screen_height - 35







