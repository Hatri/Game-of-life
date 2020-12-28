import pygame
import sys

WIDTH = 800
ROWS = 20
WIN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("Game of Life")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Node:
    def _init_(self, row, col, width):
        self.row = row
