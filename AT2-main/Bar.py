
import pygame
class Bar:
    def __init__(self,barLength, maxValue, currentValue, x, y, surface, colour1, colour2):
        self.x = x
        self.surface = surface
        self.colour1 = colour1
        self.colour2 = colour2
        self.y = y
        self.bar_length = barLength
        self.current_Value = currentValue
        self.max_Value = maxValue
        self.healthbar_length = 400
        self.Ratio = self.max_Value/self.bar_length 

    def draw(self):
        pygame.draw.rect(self.surface, self.colour2, (self.x, self.y, self.current_Value/self.Ratio , 25))
        pygame.draw.rect(self.surface, self.colour1, (self.x, self.y, self.bar_length, 25), 4)

    def update(self):
        self.draw()

 