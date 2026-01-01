"""
Name: Zackery Loy
Date: 12/31/2025
Description: Snake Game then moving into a 2D
loot finder maybe mobile swipe game
"""
import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720





def main():

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)




    # quit game functionality when click X in top right
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")

        # draw the snake
        pygame.draw.circle(screen, GREEN, player_pos, 40)
        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        pygame.display.flip()

        dt = clock.tick(60) / 1000



main()







pygame.quit()