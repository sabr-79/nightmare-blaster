import pygame
import math
import random
import constants as c

class Shottype_1(pygame.sprite.Sprite):
    def __init__(self):
        super(Shottype_1, self).__init__()
        self.image = pygame.image.load("assets/arrowhead.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = -8
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Shottype_2(pygame.sprite.Sprite):
    def __init__(self):
        super(Shottype_2, self).__init__()
        self.image = pygame.image.load("assets/arrowhead.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = -8
    def update(self):
        self.rect.x += self.vel_x 
        self.rect.y += self.vel_y

    
class Butterfly(pygame.sprite.Sprite):
    def __init__(self, parent, start_angle, orbit_radius, speed):
        super(Butterfly, self).__init__()
        self.parent = parent
        self.angle = start_angle
        self.orbit_radius = orbit_radius
        self.speed = speed
        self.state = 'orbit'
        self.image = pygame.image.load("assets/butterfly.png").convert_alpha()
        self.rect = self.image.get_rect(center=self._orbit_pos())

    def _orbit_pos(self):
        rad = math.radians(self.angle)
        cx, cy = self.parent.rect.center
        return (cx + math.cos(rad)*self.orbit_radius,
                cy + math.sin(rad)*self.orbit_radius)
    
    def launch(self):
        if self.state == 'orbit':
            self.state = 'burst'
            rad = math.radians(self.angle)
            self.dx = math.cos(rad) * self.speed
            self.dy = math.sin(rad) * self.speed

    def update(self):
        if self.state == 'orbit':
            self.rect.center = self._orbit_pos()
        elif self.state == 'burst':
            self.rect.x += self.dx
            self.rect.y += self.dy


class Amulet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed):
        super(Amulet, self).__init__()
        self.image = pygame.image.load("assets/amulet.png").convert_alpha()
        self.original_pos = pygame.math.Vector2(x, y)
        self.angle = angle
        self.speed = speed
        self.radius = 0
        self.rect = self.image.get_rect(center=(x, y))
       
   
    def update(self):
        rad = math.radians(self.angle)
        self.radius += self.speed
        self.angle -= 0.5
        x = self.original_pos.x + math.cos(rad) * self.radius 
        y = self.original_pos.y + math.sin(rad) * self.radius 
        x += 1
        y -= 1
        self.rect.center =(x, y)

class Rose(pygame.sprite.Sprite):
    def __init__(self, x, y, fall_speed, launch_delay):
        super(Rose, self).__init__()
        self.image = pygame.image.load("assets/rose.png").convert_alpha()
        self.rect =self.image.get_rect(center=(x,y))
        self.fall_speed = fall_speed
        self.launch_delay = launch_delay
        self.timer = 0
        self.small_bullets = pygame.sprite.Group()

        num_small = 8
        for i in range(num_small):
            angle = i * (360/num_small)
            b = Butterfly(self, angle, orbit_radius = 50, speed = 6)
            self.small_bullets.add(b)

    def update(self):
        self.rect.y += self.fall_speed
        self.timer += 1
        if self.timer >= self.launch_delay:
            for b in self.small_bullets:
                b.launch()
        self.small_bullets.update()

class Bubble(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super(Bubble, self).__init__()
        self.image = pygame.image.load("assets/bubble.png").convert_alpha()
        self.rect = self.image.get_rect(center= (x,y))
        self.speed = speed
    
    def update(self):
        self.rect.y -= self.speed

class Heart(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, player_coord, float_height = 250, speed= 4):
        super(Heart, self).__init__()
        self.image = pygame.image.load("assets/heart.png").convert_alpha()
        self.rect = self.image.get_rect(center=(start_x, start_y))

        self.phase = 'float'  
        self.float_target = start_y - float_height
        self.float_speed = 2

        self.player_coord = player_coord
        self.speed = speed

        self.dx = 0
        self.dy = -self.float_speed

    def update(self):
        if self.phase == 'float':
            self.rect.y += self.dy
            if self.rect.y <= self.float_target:
                px, py = self.player_coord.rect.center
                sx, sy = self.rect.center

                angle = math.atan2(py-sy, px - sx)
                self.dx = math.cos(angle) * self.speed
                self.dy = math.sin(angle) * self.speed
                self.phase = 'chase'

        elif self.phase == 'chase':
            self.rect.x += self.dx
            self.rect.y += self.dy

 
    

