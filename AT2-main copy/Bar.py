
import pygame
class Bar:
    def __init__(self, maxValue, currentValue, x, y):
        self.x = x
        self.y = y
        self.current_Value = currentValue
        self.max_Value = maxValue

    def draw(self, surface, colour):
        pygame.draw.rect(surface, colour, (self.x, self.y, self.current_Value, 25))
        