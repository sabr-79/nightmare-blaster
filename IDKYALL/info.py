import pygame
import constants as c
import random

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        pygame.font.init()
        self.value = 0
        self.font_size = 30
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render(str(f'Score: {self.value}'), False, c.white, None)

        self.rect = self.image.get_rect()
        self.rect.x = c.screen_width - self.rect.width - 20
        self.rect.y = c.screen_height - self.rect.height - 20

    def update(self):
        pass

    def update_score(self, chara_lives):
        value = 4 * (chara_lives) 
        self.value += value
        self.image = self.font.render(str(f'Score: {self.value}'), False, c.white, None)

        self.rect = self.image.get_rect()
        self.rect.x = c.screen_width - self.rect.width - 20
        self.rect.y = c.screen_height - self.rect.height - 20

    def final_score(self, chara_lives):
        if chara_lives == c.set_life:
            value = 2500 * c.set_life
        elif chara_lives > 0:
            value = (chara_lives * 250) 
        if chara_lives == 0:
            value = 0

        self.value += value
        self.image = self.font.render(str(f'Score: {self.value}'), False, c.white, None)

        self.rect = self.image.get_rect()
        self.rect.x = c.screen_width - self.rect.width - 20
        self.rect.y = c.screen_height - self.rect.height - 20



class Lives(pygame.sprite.Sprite):
    def __init__(self, player_lives):
        super(Lives, self).__init__()
        pygame.font.init()
        self.life = c.set_life
        self.font_size = 30
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render(str(f'Lives: {self.life}'), False, c.white, None)
        self.player_lives = player_lives

        self.rect = self.image.get_rect()
        self.rect.x = c.screen_width - self.rect.width - 20
        self.rect.y = c.screen_height - self.rect.height - 50

    def update(self):
        pass

    def update_count(self, player_lives):
        self.image = self.font.render(str(f'Lives: {player_lives}'), False, c.white, None)

        self.rect = self.image.get_rect()
        self.rect.x = c.screen_width - self.rect.width - 20
        self.rect.y = c.screen_height - self.rect.height - 50


class Game_over(pygame.sprite.Sprite):
    def __init__(self, player_lives):
        super(Game_over, self).__init__()
        pygame.font.init()
        self.font_size = 50
        self.font = pygame.font.Font(None, self.font_size)
        self.image = self.font.render("GAME OVER, YOU DIED.", False, c.white, None)

        self.rect = self.image.get_rect()
        self.rect.x = c.screen_width - self.rect.width - 120
        self.rect.y = self.rect.height
        self.player_lives = player_lives

    def update_screen(self, player_lives):
        if player_lives > 0:
            self.image = self.font.render("GAME OVER, YOU WON!", False, c.white, None)
        else:
            self.image = self.font.render("GAME OVER, YOU DIED.", False, c.white, None)
        
        self.rect = self.image.get_rect()
        self.rect.x = c.screen_width - self.rect.width - 120
        self.rect.y = self.rect.height

      

    def update():
        pass



