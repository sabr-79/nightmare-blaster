# Files and needed libraries: 
import random
import pygame
from player import Player, HB
from enemy import Boss
import constants as c 
from background import Star, BG
from bullet import Shottype_1, Shottype_2, Rose, Butterfly
from info import Score, Lives, Game_over

# Start, screen, fps, etc
pygame.init()
hit_sound = pygame.mixer.Sound("assets/death.mp3")
hit_sound.set_volume(0.1)
ost = pygame.mixer.music.load("assets/Dream_shooter.mp3")
pygame.mixer.music.play()
screen = pygame.display.set_mode(c.screen_size)
clock=pygame.time.Clock()
pygame.display.set_caption("Nightmare Blaster")
screenmode=0
font = pygame.font.SysFont(None, 48)
health_lost = 0
score_timer = 0


# Classes
wallpaper = BG()
hitbox = HB()
chara=Player(hitbox)
ghost=Boss(chara)
score = Score()
lives = Lives(chara)
end = Game_over(chara)

damage = pygame.rect.Rect(195, 30, 250, 20)
health_remaining = pygame.rect.Rect(195, 30, 250, 20)


# Groups
sprite_group= pygame.sprite.Group()
bg_group = pygame.sprite.Group()
font_group1 = pygame.sprite.Group()
font_group2 = pygame.sprite.Group()

sprite_group.add(chara)
sprite_group.add(hitbox)
sprite_group.add(ghost)

font_group1.add(score)
font_group1.add(lives)

font_group2.add(end)

bg_group.add(wallpaper)



# Run event
running = True
while running:
    clock.tick(c.fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if screenmode == 0:
                if event.key == pygame.K_SPACE:
                    screenmode = 1

            elif screenmode == 2:
                if event.key == pygame.K_SPACE:
                    score.value = 0
                    chara.lives = c.set_life
                    lives.update_count(chara.lives)
                    score.update_score (chara.lives )
                    hitbox.lives = c.set_life
                    chara.hits = 0
                    ghost.health = 250
                    ghost.health_lost = 0
                    ghost.state = 'left'
                    ghost.is_alive = True
                    ghost.spellOne = True
                    ghost.spellThree = False
                    ghost.spellTwo = False
                    end = Game_over(chara)
                    ghost = Boss(chara)
                    ghost.is_alive = True
                    
                    font_group2.empty()
                    font_group2.add(end)

                    sprite_group.add(chara)
                    sprite_group.add(hitbox)
                    sprite_group.add(ghost)
                    ghost.Spell_Card_1
                    screenmode = 1

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                chara.vel_x = -chara.speed
            elif event.key== pygame.K_RIGHT:
                chara.vel_x=chara.speed
            elif event.key== pygame.K_UP:
                chara.vel_y=-chara.speed
            elif event.key== pygame.K_DOWN:
                chara.vel_y=chara.speed
            
            
        if event.type==pygame.KEYUP:
            if event.key ==pygame.K_UP:
                chara.vel_y = 0
             
            elif event.key== pygame.K_DOWN:
                chara.vel_y=0

            elif event.key ==pygame.K_LEFT:
                chara.vel_x = 0
    
            elif event.key== pygame.K_RIGHT:
                chara.vel_x=0


    if screenmode == 0:
        screen.fill(c.indigo)
        bg_group.update()
        bg_group.draw(screen)
        start_text = font.render("PRESS SPACE TO START", True, c.white)
        screen.blit(start_text, (c.screen_width // 2 - start_text.get_width() // 2, 300))
    
    elif screenmode == 1:
        score_timer += 1
        if score_timer == 90:
            score_timer = 0
            score.update_score(chara.lives)
            end.update_screen(chara.lives)


        hits = pygame.sprite.spritecollide(ghost, chara.bullets, True)
        attacks = pygame.sprite.spritecollide(chara.hitbox, ghost.bullets1, True)
        attack1 = pygame.sprite.spritecollide(chara.hitbox, ghost.rose, True)
        attack2 = []
        for rose in ghost.rose:
            hit = pygame.sprite.spritecollide(chara.hitbox, rose.small_bullets, True)
            attack2.extend(hit)
        attack3 =  pygame.sprite.spritecollide(chara.hitbox, ghost.bubbles, True)
        attack4 =  pygame.sprite.spritecollide(chara.hitbox, ghost.hearts, True)


        if hits:
            ghost.health -= c.damage
            ghost.health_lost += c.damage
            health_remaining = pygame.Rect(195, 30, 250 - ghost.health_lost, 20)
            ghost.death()
        
        for attack in [attacks, attack1, attack2, attack3, attack4]:
            if attack and not chara.cooldown:
                pygame.mixer.Sound.play(hit_sound)
                chara.lives -= 1
                hitbox.lives -= 1
                chara.hits += 1
                lives.update_count(chara.lives)
                chara.cooldown = True
                chara.cooldown_timer = chara.max_cooldown
                hitbox.get_hit()
        
        if chara.lives==0:
            score.value = 0
            chara.hits = 0
            end.update_screen(chara.lives)
            screenmode = 2
            
        elif not ghost.is_alive:
            end.update_screen(chara.lives)
            screenmode = 2

    
        
    
   # Update objects
    
        bg_group.update()
        font_group1.update()
        sprite_group.update()

    # Render game screen
    #if screenmode == 1:
        screen.fill(c.indigo) 
        bg_group.draw(screen)
        sprite_group.draw(screen)
        font_group1.draw(screen)
        chara.bullets.draw(screen)
        ghost.bullets1.update()
        ghost.bubbles.update()
        ghost.hearts.update()
        ghost.bullets1.draw(screen)
        ghost.rose.draw(screen)
        for rose in ghost.rose:
            rose.small_bullets.draw(screen)
            rose.small_bullets.update()
        ghost.bubbles.draw(screen)
        ghost.hearts.draw(screen)
        pygame.draw.rect(screen, c.red, damage)
        pygame.draw.rect(screen, c.green, health_remaining)


    elif screenmode == 2:
        pygame.mixer.Sound.stop(hit_sound)
        #end.update_screen()
        score.update_score(chara.lives)
        score.final_score(chara.lives)
        chara.lives = 0
        chara.hits = 0
        screen.fill(c.indigo)
        sprite_group.empty()
        bg_group.update()
        bg_group.draw(screen)
        restart_msg = font.render("Press SPACE to Restart", True, c.white)
        screen.blit(restart_msg, (c.screen_width // 2 - restart_msg.get_width() // 2, 300))

        font_group1.draw(screen)
        font_group2.draw(screen)
        

            
    
     








    pygame.display.update()




