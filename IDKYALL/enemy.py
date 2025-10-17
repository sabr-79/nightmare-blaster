import pygame
import random
import math
import constants as c
from bullet import Butterfly, Rose, Amulet, Bubble, Heart
from player import Player, HB

class Boss(pygame.sprite.Sprite):
    def __init__(self, player_coord):
        super(Boss, self).__init__()
        self.image = pygame.image.load("assets/pixil-frame-1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.bullets1 = pygame.sprite.Group()
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 2
        self.rect.x=210
        self.rect.y=70
        self.original_x = 210
        self.left_target = self.rect.x - 200
        self.right_target = self.rect.x + 200
        self.up_target = 55
        self.down_target = 85
        self.spell_angle1 = 0
        self.spell_angle2 = 0
        self.spell_timer = 0
        self.movement = True
        self.timer = 0
        self.state = 'left'
        self.pause = 120
        self.v_state = 'up'
        self.health = 250
        self.health_lost = 0
        self.is_alive = True
        self.spellOne=True
        self.spellTwo=False
        self.spellThree=False
        self.rose = pygame.sprite.Group()
        self.phase = "one"
        self.bubbles = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.hearts_timer = 0
        self.player_coord = player_coord


 

        


    def Spell_Card_1(self):
       if self.spellOne == True:
            num_bullets = random.randrange(6,8)
            for i in range(num_bullets):
                a1 = self.spell_angle1 + (i * (360/num_bullets))
                b1 = Amulet(self.rect.centerx, self.rect.centery, a1, random.randrange(1,3))
                self.bullets1.add(b1)
    
    def Spell_Card_2(self):
        if self.spellTwo == True:
            for i in range(2):
                x = random.randrange(0, c.screen_width)
                y = -50
                orb = Rose(x,y, fall_speed = random.randrange(3,8), launch_delay=random.randrange(15, 60))
                self.rose.add(orb)
    
    def Spell_Card_3(self):
        if self.spellThree == True:
            for i in range(2):
                x = random.randrange(0, c.screen_width)
                y = c.screen_height + 50
                bubble = Bubble(x, y, speed = random.randrange(2, 7))
                self.bubbles.add(bubble)

            self.hearts_timer += 1
            if self.hearts_timer == 2:

                heart1 = Heart(self.rect.centerx, self.rect.bottom, self.player_coord)
                self.hearts.add(heart1)
                self.hearts_timer = 0
    
        
            


        



    def death(self):
        if self.health < 0 and self.spellOne == True:
            self.health = 250
            self.phase = "two"
            self.health_lost = 0
            self.spellOne = False
            self.spellTwo = True
            self.spell_timer = 0
            self.bullets1.empty()
            self.Spell_Card_2

        if self.health < 0 and self.spellTwo == True:
            self.health = 250
            self.phase = "three"
            self.health_lost = 0
            self.spellTwo = False
            self.spellThree = True
            self.rose.empty()
            self.spell_timer = 0
            self.Spell_Card_3

        if self.health < 0 and self.spellThree == True:
            self.health = 0
            self.spellThree = False
            self.is_alive = False
            self.hearts.empty()
            self.bubbles.empty()


 
    



    def update(self):
        if self.is_alive == True:
            if self.state == "left":
                self.rect.x -= self.speed
                if self.rect.x <= self.left_target:
                    self.rect.x = self.left_target
                    self.state = "pause_left"
                    self.timer = 0

            elif self.state == "pause_left":
                self.timer += 1
                if self.timer >= self.pause:
                    self.state = "right"

            elif self.state == "right":
                self.rect.x += self.speed
                if self.rect.x >= self.right_target:
                    self.rect.x = self.right_target
                    self.state = "pause_right"
                    self.timer = 0

            elif self.state == "pause_right":
                self.timer += 1
                if self.timer >= self.pause:
                    self.state = "center"

            elif self.state == "center":
                if self.rect.x > self.original_x:
                    self.rect.x -= self.speed
                    if self.rect.x <= self.original_x:
                        self.rect.x = self.original_x
                        self.state = "pause_center"
                        self.timer = 0
            
            elif self.state == "pause_center":
                self.timer += 1 
                if self.timer >= self.pause:
                    self.state = "left"

            if self.v_state == 'up':
                if self.state == 'pause_left' or self.state == 'pause_right' or self.state == 'pause_center':
                    self.rect.y -= self.speed
                    if self.rect.y <= self.up_target:
                        self.rect.y = self.up_target
                        self.v_state = 'down'
            if self.v_state == 'down':
                if self.state == 'pause_left' or self.state == 'pause_right' or self.state == 'pause_center':
                    self.rect.y += self.speed
                    if self.rect.y >= self.down_target:
                        self.rect.y = self.down_target
                        self.v_state = 'up'
        

        if self.is_alive == True and self.phase == 'one':
            self.spell_timer += 1
            if self.spell_timer == 12:
                self.Spell_Card_1()
                self.spell_timer = 0

        if self.is_alive == True and self.phase == 'two':
            self.spell_timer += 1
            if self.spell_timer == 50:
                self.Spell_Card_2()
                self.spell_timer = 0
        
        if self.is_alive == True and self.phase == 'three':
            self.spell_timer += 1
            if self.spell_timer == 20:
                self.Spell_Card_3()
                self.spell_timer = 0

        
        for bullet in self.bullets1:
            if bullet.rect.y <= 0 or bullet.rect.y >= c.screen_height:
                self.bullets1.remove()
                

        for bullet in self.bullets1:
            if bullet.rect.x <= 0 or bullet.rect.x>= c.screen_width:
                self.bullets1.remove()
                
        for rose in self.rose.copy():
            if rose.rect.top > c.screen_height:
                rose.kill()
        
        for bubble in self.bubbles:
            if bubble.rect.y <= 0:
                self.bubbles.remove()
        for heart in self.hearts:
             if heart.rect.y >= c.screen_height:
                self.hearts.remove()


        self.bullets1.update()
        self.rose.update()
        self.bubbles.update()
        self.hearts.update()
        for rose in self.rose:
            rose.small_bullets.update()


            



        




