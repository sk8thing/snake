from .snake import SNAKE
from .food import FOOD
import pygame
from pygame.math import Vector2

pygame.init()


class GAME:
    CELL_SIZE = 30
    CELL_COUNT = 20

    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()
        self.score = 0

    def update(self):
        self.snake.move()
        self.check_collision()
        self.is_ended()

    def draw(self, screen):
        self.snake.draw(screen)
        self.food.draw(screen)
        self.draw_score(screen)
        if self.is_ended():
            self.draw_lose(screen)

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.regen()
            self.snake.grow()

        for part in self.snake.body[1:]:
            if part == self.food.pos:
                self.food.regen()

    def draw_score(self, surface):
        score_text = str(len(self.snake.body) - 3)
        score_surface = pygame.font.Font(None, 30).render(score_text, True, (0, 0, 0))
        surface.blit(score_surface, (570, 570))

    def draw_lose(self, surface):
        lose_text = "YOU LOST"
        lose_surface = pygame.font.Font(None, 30).render(lose_text, True, (0, 0, 0))
        surface.blit(lose_surface, (250, 300))

    def is_ended(self):
        if not 0 <= self.snake.body[0].x < self.CELL_COUNT or not 0 <= self.snake.body[0].y < self.CELL_COUNT:
            return True

        for part in self.snake.body[1:]:
            if part == self.snake.body[0]:
                return True

    def reset(self):
        self.snake.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.snake.direction = self.snake.DIRECTIONS["right"]
        self.food.regen()
