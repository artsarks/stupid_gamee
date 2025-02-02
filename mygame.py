import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_velocity_y = 0
player_speed = 5
gravity = 0.8
jump_strength = -15

platforms = [
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),
    pygame.Rect(200, 400, 150, 20),
    pygame.Rect(500, 300, 150, 20),
    pygame.Rect(100, 200, 150, 20),
]

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if player_velocity_y == 0:
            player_velocity_y = jump_strength

    player_velocity_y += gravity
    player_y += player_velocity_y

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for platform in platforms:
        if player_rect.colliderect(platform) and player_velocity_y >= 0:
            player_y = platform.y - player_size
            player_velocity_y = 0

    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()