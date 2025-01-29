
import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake and food
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
            random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Game over function
def game_over():
    font = pygame.font.SysFont('arial', 50)
    msg = font.render("Game Over!", True, RED)
    screen.blit(msg, [WIDTH // 4, HEIGHT // 3])
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= BLOCK_SIZE
    if direction == 'DOWN':
        snake_pos[1] += BLOCK_SIZE
    if direction == 'LEFT':
        snake_pos[0] -= BLOCK_SIZE
    if direction == 'RIGHT':
        snake_pos[0] += BLOCK_SIZE

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                    random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
    food_spawn = True

    if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    screen.fill(BLACK)
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    font = pygame.font.SysFont('arial', 20)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

    pygame.display.update()

    clock.tick(10)

