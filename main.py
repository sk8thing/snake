import pygame
import sys
from game import GAME


def main_game():
    update = pygame.USEREVENT
    pygame.time.set_timer(update, 150)
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("SNAKE")
    snake_game = GAME()
    clock = pygame.time.Clock()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == update and not snake_game.is_ended():
                snake_game.update()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w and not snake_game.snake.direction == snake_game.snake.DIRECTIONS["down"]:
                    snake_game.snake.direction = snake_game.snake.DIRECTIONS["up"]
                if e.key == pygame.K_s and not snake_game.snake.direction == snake_game.snake.DIRECTIONS["up"]:
                    snake_game.snake.direction = snake_game.snake.DIRECTIONS["down"]
                if e.key == pygame.K_a and not snake_game.snake.direction == snake_game.snake.DIRECTIONS["right"]:
                    snake_game.snake.direction = snake_game.snake.DIRECTIONS["left"]
                if e.key == pygame.K_d and not snake_game.snake.direction == snake_game.snake.DIRECTIONS["left"]:
                    snake_game.snake.direction = snake_game.snake.DIRECTIONS["right"]
                if e.key == pygame.K_r and snake_game.is_ended():
                    snake_game.reset()

        screen.fill((86, 125, 70))
        snake_game.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main_game()
