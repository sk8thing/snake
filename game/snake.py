import pygame
from pygame.math import Vector2


class SNAKE:
    CELL_SIZE = 30
    CELL_COUNT = 20
    DIRECTIONS = {
        "up": Vector2(0, -1),
        "down": Vector2(0, 1),
        "right": Vector2(1, 0),
        "left": Vector2(-1, 0)
    }

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = self.DIRECTIONS["right"]
        self.is_growing = False
        self.head_up = pygame.image.load('game/assets/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('game/assets/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('game/assets/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('game/assets/head_left.png').convert_alpha()
        self.head = self.head_right

    def draw(self, surface):
        self.update_head()
        for index, part in enumerate(self.body):
            x = part.x * self.CELL_SIZE
            y = part.y * self.CELL_SIZE
            hitbox = pygame.Rect(x, y, self.CELL_SIZE, self.CELL_SIZE)

            if index == 0:
                surface.blit(self.head, hitbox)
            else:
                pygame.draw.rect(surface, (64, 64, 64), hitbox)

    def move(self):
        if self.is_growing:
            self.is_growing = False
            vbody = self.body
            vbody.insert(0, vbody[0] + self.direction)
            self.body = vbody
            return
        vbody = self.body[:-1]
        vbody.insert(0, vbody[0] + self.direction)
        self.body = vbody

    def grow(self):
        self.is_growing = True

    def update_head(self):
        head_direction = self.body[1] - self.body[0]
        if head_direction == self.DIRECTIONS["up"]:
            self.head = self.head_down
        elif head_direction == self.DIRECTIONS["down"]:
            self.head = self.head_up
        elif head_direction == self.DIRECTIONS["right"]:
            self.head = self.head_left
        elif head_direction == self.DIRECTIONS["left"]:
            self.head = self.head_right
