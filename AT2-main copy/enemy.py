import pygame
import random

class Enemy:
    def __init__(self, image_path, position, window, name):
        # Load the enemy image from the specified image path
        self.image = pygame.image.load(image_path).convert_alpha()

        self.name = name
        
        # Scale the enemy image to 0.75 times the original size
        self.combat_image = pygame.transform.scale(self.image, (int(self.image.get_width() * 2), int(self.image.get_height() * 2)))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.75), int(self.image.get_height() * 0.75)))        
        # Set the initial position of the enemy
        self.position = position
        
        # Set the window where the enemy will be drawn
        self.window = window
        
        # Set the initial health of the enemy to 100
        self.health = 100

    def take_damage(self, damage):
        # Reduce the enemy's health by the specified damage amount
        self.health -= damage
        
        # Return True if the enemy's health is less than or equal to 0, indicating that it is defeated
        return self.health <= 0
    
    def is_dead(self, damage):
        health_test = self.health

        health_test -= damage

        return health_test <= 0

    def draw(self):
        # Adjust the position to ensure the image does not overflow the window boundaries
        adjusted_position = [
            max(0, min(self.window.get_width() - self.image.get_width(), self.position[0])),
            max(0, min(self.window.get_height() - self.image.get_height(), self.position[1]))
        ]
        
        # Draw the enemy image on the window at the adjusted position
        self.window.blit(self.image, adjusted_position)

    def COMBATDRAW(self):
        # Adjust the position to ensure the image does not overflow the window boundaries
        # Draw the enemy image on the window at the adjusted position
        self.window.blit(self.combat_image, (1000, 100))

