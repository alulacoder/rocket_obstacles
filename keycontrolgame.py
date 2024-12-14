import pygame
from pygame.locals import *
from time import sleep
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Scrolling Background with Obstacles")

# Load images
player = pygame.image.load("images/rocket.png")
background = pygame.image.load("images/starwarp.png")
obstacle_img = pygame.image.load("images/asteroid.png")  # Load obstacle image

# Scale images if necessary
player = pygame.transform.scale(player, (50, 50))
obstacle_img = pygame.transform.scale(obstacle_img, (50, 50))

# Variables for player
player_x = 225
player_y = 400
player_speed = 7
keys = [False, False, False, False]

# Background scrolling
bg_y1 = 0
bg_y2 = -500
bg_speed = 5

# Obstacles
obstacles = []
obstacle_speed = 5
spawn_timer = 0

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear the screen
    
    # Scroll background
    bg_y1 += bg_speed
    bg_y2 += bg_speed
    if bg_y1 >= 500:  # Reset position of the first background
        bg_y1 = -500
    if bg_y2 >= 500:  # Reset position of the second background
        bg_y2 = -500
    screen.blit(background, (0, bg_y1))
    screen.blit(background, (0, bg_y2))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_RIGHT:
                keys[3] = False
    
    # Move player
    if keys[0] and player_y > 0:
        player_y -= player_speed
    if keys[1] and player_x > 0:
        player_x -= player_speed
    if keys[2] and player_y < 450:  # Keep player within screen
        player_y += player_speed
    if keys[3] and player_x < 450:  # Keep player within screen
        player_x += player_speed

    # Spawn obstacles
    spawn_timer += 1
    if spawn_timer > 30:  # Spawn a new obstacle every 30 frames
        obstacle_x = random.randint(0, 450)
        obstacles.append([obstacle_x, -50])  # Start above the screen
        spawn_timer = 0
    
    # Move obstacles and check for collisions
    for obstacle in obstacles[:]:
        obstacle[1] += obstacle_speed  # Move obstacle down
        screen.blit(obstacle_img, (obstacle[0], obstacle[1]))  # Draw obstacle
        if obstacle[1] > 500:  # Remove obstacles that move off screen
            obstacles.remove(obstacle)
        # Collision detection
        player_rect = pygame.Rect(player_x, player_y, 50, 50)
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], 50, 50)
        if player_rect.colliderect(obstacle_rect):
            print("Game Over")
            running = False
    
    # Draw player
    screen.blit(player, (player_x, player_y))
    
    # Update display
    pygame.display.flip()
    sleep(0.05)

pygame.quit()
