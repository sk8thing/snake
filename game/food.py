import pygame
from pygame.math import Vector2
from random import randint


class FOOD:
    CELL_SIZE = 30
    CELL_COUNT = 20

    def __init__(self):
        self.pos = None
        self.regen()
        self.food_surface = pygame.image.load('game/assets/food.png').convert_alpha()

    def draw(self, surface):
        hitbox = pygame.Rect(self.pos.x * self.CELL_SIZE, self.pos.y * self.CELL_SIZE, self.CELL_SIZE,
                             self.CELL_SIZE)
        surface.blit(self.food_surface, hitbox)

    def regen(self):
        self.pos = Vector2(randint(0, self.CELL_COUNT - 1), randint(0, self.CELL_COUNT - 1))
