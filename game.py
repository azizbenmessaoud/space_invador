import pygame
import sys
import random
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP

from pygame.time import Clock

# initialize pygame
pygame.init()

# set up screen settings
WIDTH = HEIGHT = 500
CAPTION = 'Space Invador'
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

# lives : red hearts, black hearts
red_life = pygame.image.load("red_heart.png")
black_life = pygame.image.load("black_heart.jpg")
lifes_numbers_init = 4
lifes_numbers = lifes_numbers_init
top_left_life_x = 400
top_left_life_y = 25
life_width = 25
life_height = 25


# draw hearts function
def draw_hearts():
    for i in range(lifes_numbers):
        SCREEN.blit(pygame.transform.scale(red_life, (life_width, life_height)), [top_left_life_x + i * 20, top_left_life_y])
    for i in range(lifes_numbers, lifes_numbers_init):
        SCREEN.blit(pygame.transform.scale(black_life, (life_width, life_height)), [top_left_life_x + i * 20, top_left_life_y])


# aliens
aliens_list = []
alien_number = 10
alien_color_init = (39, 186, 6)
alien_color_hit = (151, 1, 1)
alien_width = 20
alien_height = 40
top_left_alien_x = 10
alien_y_init = 10

# create alien
def build_aliens():
    for i in  range(alien_number):
        aliens_list.append([pygame.Rect((top_left_alien_x + i * 40), alien_y_init, alien_width, alien_height), False, False])

# create aliens
build_aliens()

# move aliens automaticly
def move_aliens():
    for alien in aliens_list:
        random_alien_speed = random.randint(0, 1)
        alien[0].y += random_alien_speed



# ship
was_not_colliding_with_alien = True
ship_color = (161, 7, 185)
ship_width = 20
ship_height = 50
ship_x = (WIDTH // 2) - (ship_width // 2)
latest_ship_x = ship_x
ship_y = HEIGHT - ship_height - (ship_height // 2)
latest_ship_y = ship_y
ship_rect = pygame.Rect(ship_x, ship_y, ship_width, ship_height)

# check colid x coordinates
"""
def collidate_x():
    if ship_rect.x >= WIDTH or ship_rect.x <= 0:

        # changing the x coordinate to the latest value it had before overcoming the width borders
        
        return True
    else: return False

# check colid y coordinates
def collidate_y():
    if ship_rect.y >= ship_y + ship_height or ship_rect.y <= HEIGHT // 2:

        # changing the y coordinate to the latest value it had before overcoming the y borders
        
        return True
    else: return False
"""

# changing x and y coordinates when pressing on keyboard specific buttons
def move_ship():
    if up_key_down:
        latest_ship_y = ship_rect.y
        ship_rect.y -= speed_y
    if down_key_down:
        latest_ship_y = ship_rect.y
        ship_rect.y  += speed_y
    if right_key_down:
        latest_ship_x = ship_rect.x
        ship_rect.x  += speed_x
    if left_key_down:
        latest_ship_x = ship_rect.x
        ship_rect.x  -= speed_x

"""
# check collision between ship and aliens
def ship_collide_with_alien():
    for alien in aliens_list:
        if alien[0].colliderect(ship_rect) and was_not_colliding_with_alien:
            return True


    
    return False
"""
        
# bullets
bullet_counter_block_x = 400
bullet_counter_block_y = 5
none_bullet_color = (0, 0, 0)
bullets_counter_init = 10
bullets_counter = bullets_counter_init
bullet_rect = None
bullet_color = (239, 62, 8)
bullet_width = 5
bullet_height = 15
bullet_speed = 10

# build bullet
def build_bullet():
    return pygame.Rect(ship_rect.x + (ship_width // 2) - (bullet_width // 2), ship_rect.y, bullet_width, bullet_height)

# bullets counter display build
def build_b_counter_display():
    global bullets_counter_list
    bullets_counter_list = []
    for i in range(bullets_counter_init):
        bullets_counter_list.append(pygame.Rect((bullet_counter_block_x + i * bullets_counter_init), bullet_counter_block_y, bullet_width, bullet_height))

# update screen function 
def update_screen():
    clock.tick(fps)
    SCREEN.fill((255, 255, 255))

    # changing x & y coordinates when player moves the ship
    move_ship()

    # draw the ship on the screen
    pygame.draw.rect(SCREEN, ship_color, ship_rect)

    # draw bullet if exists
    if bullet_rect:
        pygame.draw.rect(SCREEN, bullet_color, bullet_rect)

    # draw aliens
    for alien in aliens_list:
        if not alien[2]:
            if not alien[1]:
                # if not hit, alien color will be green
                pygame.draw.rect(SCREEN, alien_color_init, alien[0])   
            else:
                # if hit, alien color will be red
                pygame.draw.rect(SCREEN, alien_color_hit, alien[0])

    # draw bullet counter pannel 
    # available bullets in orange color
    for i in range(bullets_counter):
        pygame.draw.rect(SCREEN, bullet_color, bullets_counter_list[i])
    # sent bullets in black color
    for i in range(bullets_counter, bullets_counter_init):
        pygame.draw.rect(SCREEN, none_bullet_color, bullets_counter_list[i])

    # draw lifes : hearts
    draw_hearts()
        
    pygame.display.update()

# global variables
up_key_down = False
down_key_down = False
right_key_down = False
left_key_down = False
clock = pygame.time.Clock()
speed_x = 7
speed_y = 7
fps = 60
is_running = True

# game loop
while is_running:

    # check for events
    for event in pygame.event.get():

        # close window when clicking on red x button
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
            sys.exit()

        # ship movement control (keydown conditions)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # and not collidate_y():
                up_key_down = True
            elif event.key == pygame.K_DOWN: # and not collidate_y():
                down_key_down = True
            elif event.key == pygame.K_RIGHT: # and not collidate_x():
                right_key_down = True 
            elif event.key == pygame.K_LEFT: # and not collidate_x():
                left_key_down = True 
            
            # send bullet
            elif event.key == pygame.K_SPACE and bullets_counter > 0:
                bullet_rect = build_bullet()
                bullets_counter -= 1


        # ship movement control (keyup conditions)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_key_down = False
            elif event.key == pygame.K_DOWN:
                down_key_down = False
            elif event.key == pygame.K_RIGHT: 
                right_key_down = False
            elif event.key == pygame.K_LEFT:
                left_key_down = False

    # bullet movement control
    if bullet_rect:
        bullet_rect.y -= bullet_speed

        # check for collision between bullets and aliens
        for alien in aliens_list:
            if bullet_rect:
                if alien[0].colliderect(bullet_rect):
                    # if not hit before, change its color to red
                    if alien[1] == False:
                        bullet_rect.y = -50
                        alien[1] = True
                    # if hit before, make it disappear
                    elif alien[2] == False:
                        # add another extra bullet when killing an alien
                        if bullets_counter < bullets_counter_init:
                            bullets_counter += 1
                        alien[2] = True
                    

    

    # alien movement control
    move_aliens()

    # call for building bullets counter display block function
    build_b_counter_display()

    # fill in the screen with a background color
    SCREEN.fill((111, 111, 111))

    # call update screen
    update_screen()