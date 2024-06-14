# Artin khodayari
# github.com/artin-khodayari
# artinkhodayari2010@gmail.com


import pygame
import sys
import random


while True :
    WIDTH, HEIGHT = 500, 500
    PLAYER_WIDTH, PLAYER_HEIGHT = 100, 5
    OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 40, 50
    PLAYER_SPEED = 9
    OBSTACLE_SPEED = 9
    WHITE = (255, 255, 255)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("nokia cars : Artin")
    player_x = WIDTH // 2
    player_y = HEIGHT - PLAYER_HEIGHT
    obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
    obstacle_y = 0
    score = 0

    pygame.font.init()
    font = pygame.font.SysFont(None, 36)

    colors = ['red', 'yellow', 'brown', 'lightbrown', 'lightblue', 'pink', 'purple', 'lightgreen']

    def change_obstacle_color():
        random_color = random.choice(colors)
        return random_color
        
    new_color = change_obstacle_color()

    def draw_player(x, y):
        pygame.draw.rect(screen, "BLUE", (x, y, PLAYER_WIDTH, PLAYER_HEIGHT))

    def draw_obstacle(x, y):
        pygame.draw.rect(screen, new_color, (x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED

        obstacle_y += OBSTACLE_SPEED
        if obstacle_y > HEIGHT:
            obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
            obstacle_y = 0
            score += 1

        if obstacle_y + OBSTACLE_HEIGHT > player_y and obstacle_x < player_x + PLAYER_WIDTH and obstacle_x + OBSTACLE_WIDTH > player_x:
            
            with open('colors_history.txt', 'a', encoding='utf-8') as file:
                file.write(new_color + '\n')

            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        draw_player(player_x, player_y)
        draw_obstacle(obstacle_x, obstacle_y)

        score_text = font.render(f"color : {new_color}"f" score : {score}", True, new_color)
        screen.blit(score_text, (8, 8))

        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED

        obstacle_y += OBSTACLE_SPEED
        if obstacle_y > HEIGHT:
            obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
            obstacle_y = 0
            score += 1

        if obstacle_y + OBSTACLE_HEIGHT > player_y and obstacle_x < player_x + PLAYER_WIDTH and obstacle_x + OBSTACLE_WIDTH > player_x:
            
            with open('colors_history.txt', 'a', encoding='utf-8') as file:
                file.write(new_color + '\n')

            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        draw_player(player_x, player_y)
        draw_obstacle(obstacle_x, obstacle_y)

        score_text = font.render(f"color : {new_color}"f" score : {score}", True, new_color)
        screen.blit(score_text, (8, 8))

        pygame.display.update()
        clock.tick(60)
