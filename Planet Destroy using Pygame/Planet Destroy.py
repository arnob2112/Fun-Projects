import pygame
import time

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load("assets/background.png")
planet = pygame.image.load("assets/planet.png")
bullet = pygame.image.load("assets/bullet.png")
spaceship = pygame.image.load("assets/spaceship.png")
destroy1 = pygame.image.load("assets/destroy 1.png")
destroy2 = pygame.image.load("assets/destroy 2.png")
pygame.font.init()
myfont = pygame.font.SysFont("Arial", 30)
text = myfont.render("Winner!", False, "white", (0, 0, 0))
planet_x = 140
bullet_y = 500
move_direction = "right"
fire = False
clock = pygame.time.Clock()

keep_alive = 0
while keep_alive < 2:
    pygame.event.get()
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        fire = True

    if move_direction == "right":
        planet_x += 5
        if planet_x == 300:
            move_direction = "left"
    else:
        planet_x -= 5
        if planet_x == 0:
            move_direction = "right"

    if fire:
        bullet_y -= 5
        if bullet_y == 50:
            fire = False
            bullet_y = 500

    screen.blit(background, [0, 0])
    screen.blit(bullet, [160, bullet_y])
    screen.blit(pygame.image.load
                ("assets/spaceship.png"), [140, 500])

    if bullet_y <= 80 and 120 <= planet_x <= 140:
        screen.blit(destroy1, [planet_x - 11, 50])
        time.sleep(1)
        screen.blit(text, [150, 250])
        time.sleep(1)
        keep_alive += 1
    else:
        screen.blit(planet, [planet_x, 50])

    pygame.display.update()
    clock.tick(60)
