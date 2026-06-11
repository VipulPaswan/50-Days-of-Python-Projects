import pygame
import random
import sys

pygame.init()

# ---------------- Settings ---------------- #

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 12

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont("Arial", 25)
big_font = pygame.font.SysFont("Arial", 40)

# ---------------- Functions ---------------- #

def draw_score(score):
    value = font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, (10, 10))


def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            [block[0], block[1], snake_block, snake_block]
        )


def start_screen():

    while True:

        screen.fill(BLACK)

        title = big_font.render("🐍 Snake Game", True, GREEN)
        msg = font.render("Press SPACE to Start", True, WHITE)
        msg2 = font.render("Arrow Keys to Move", True, YELLOW)

        screen.blit(title, (170, 120))
        screen.blit(msg, (180, 190))
        screen.blit(msg2, (180, 230))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    return


def game_loop():

    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    food_x = round(random.randrange(
        0, WIDTH - snake_block) / 20.0) * 20

    food_y = round(random.randrange(
        0, HEIGHT - snake_block) / 20.0) * 20

    game_over = False
    game_close = False

    while not game_over:

        while game_close:

            screen.fill(BLACK)

            over = big_font.render("Game Over", True, RED)
            msg = font.render(
                "Press C to Play Again or Q to Quit",
                True,
                WHITE
            )

            screen.blit(over, (180, 130))
            screen.blit(msg, (90, 200))

            draw_score(snake_length - 1)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0

                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block

                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change

        screen.fill(BLACK)

        pygame.draw.rect(
            screen,
            RED,
            [food_x, food_y, snake_block, snake_block]
        )

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)

        snake.append(snake_head)

        if len(snake) > snake_length:
            del snake[0]

        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake)

        draw_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:

            food_x = round(random.randrange(
                0, WIDTH - snake_block) / 20.0) * 20

            food_y = round(random.randrange(
                0, HEIGHT - snake_block) / 20.0) * 20

            snake_length += 1

        clock.tick(snake_speed)


# ---------------- Run ---------------- #

start_screen()
game_loop()