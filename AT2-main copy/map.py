import random
import pygame
import os
from character import Character
from mage import Mage
from warrior import Warrior
from rogue import Rogue
from assets import GAME_ASSETS
from enemy import Enemy
from Combat import Combat
class Map:
       

    def __init__(self, window):
        """
        Initialize the Map class.

        Args:
            window (pygame.Surface): The game window surface.
        """
        self.window = window
        self.map_image = pygame.image.load(GAME_ASSETS["dungeon_map"]).convert_alpha()
        self.map_image = pygame.transform.scale(self.map_image, (self.window.get_width(), self.window.get_height()))
        self.player_images = {
            'Warrior': pygame.image.load(GAME_ASSETS['warrior']).convert_alpha(),
            'Mage': pygame.image.load(GAME_ASSETS['mage']).convert_alpha(),
            'Rogue': pygame.image.load(GAME_ASSETS["rogue"]).convert_alpha()
        }
        self.player_type = None
        self.player_position = [self.window.get_width() / 2, self.window.get_height() / 2]
        self.enemies = [
            Enemy(GAME_ASSETS["goblin"], [50, 50], self.window, name="goblin"),
            Enemy(GAME_ASSETS["orc"], [self.window.get_width() - 120, 50], self.window, name="orc"),
            Enemy(GAME_ASSETS["skeleton"], [50, self.window.get_height() - 120], self.window, name="skeleton"),
            Enemy(GAME_ASSETS["skeleton"], [self.window.get_width() - 120, self.window.get_height() - 120], self.window, name="skeleton")
        ]
        self.in_combat = False  # Ensure this attribute is defined in the constructor
        self.current_enemy = None
        self.blue_orb = None
        self.game_over = False
        self.player_death = False
        self.move_speed = 2
        self.has_chosen_attack = False
        self.player_turn = True
        self.enemy_turn = False
        self.heath_bar = None

    
    def load_player(self, character_type):
        """
        Load the player character.

        Args:
            character_type (str): The type of character to load.
        """
        self.player_type = character_type
        self.player_image = self.player_images[character_type]
        self.player_image = pygame.transform.scale(self.player_image, (int(self.player_image.get_width() * 0.15), int(self.player_image.get_height() * 0.15)))
        

        if character_type == "Mage":
            self.player = Mage("Player", max_hp=100)
            
        elif character_type == "Rogue":
            self.player = Rogue("Player", max_hp=100)

        elif character_type == "Warrior":
            self.player = Warrior("Player", max_hp=100)

    def check_for_combat(self):
        """
        Check if the player is in combat with any enemy.

        Returns:
            bool: True if the player is in combat, False otherwise.
        """
        for enemy in self.enemies:
            if pygame.math.Vector2(enemy.position).distance_to(self.player_position) < 50:
                self.in_combat = True
                self.current_enemy = enemy
                return True
        return False

    def handle_combat(self):
        enemy_damage = random.randint(15, 40)
        player_defeated = self.player.take_damage(enemy_damage)
        print(f"Enemy attacks back! Deals {enemy_damage} damage to the player.")
        if player_defeated:
            print("PLAYER DIED")
            self.in_combat = False
            self.player_death = True
            return 'Enemy Turn End'
        self.enemy_turn = False
        self.player_turn = True
        return 'Enemy Turn End'
            
            
                
                

    def spawn_blue_orb(self):
        """
        Spawn the blue orb in the center of the map.
        """
        self.blue_orb = pygame.image.load(GAME_ASSETS["blue_orb"]).convert_alpha()
        self.blue_orb = pygame.transform.scale(self.blue_orb, (50, 50))
        self.orb_position = [self.window.get_width() / 2 - 25, self.window.get_height() / 2 - 25]

    def check_orb_collision(self):
        """
        Check if the player has collided with the blue orb.

        Returns:
            bool: True if the player has collided with the blue orb, False otherwise.
        """
        if self.blue_orb and pygame.math.Vector2(self.orb_position).distance_to(self.player_position) < 25:
            self.game_over = True
            print("YOU WIN")  # This can be modified to a more visual display if needed.
            return True
        return False
    

    def inCombat(self):
        self.combat = Combat(self.window, self.player, self.current_enemy)
        self.combat.load_player(self.player_type)
        self.combat.Turnbased(self.combat)
        self.combat.draw()
        
    def handle_events(self):
        """
        Handle user input events.
        
        Returns:
            str: 'quit' if the game is over and should be exited, None otherwise.
        """
        if self.game_over:
            return 'quit'  # Stop processing events if game is over
        
        if self.player_death:
            return 'lose'

        keys = pygame.key.get_pressed()

        if not self.in_combat:
            if keys[pygame.K_ESCAPE]:  
                pygame.quit()
            if keys[pygame.K_LEFT]:
                self.player_position[0] -= self.move_speed
                if self.player_position[0] <= 0:
                    self.player_position[0] = 0
            if keys[pygame.K_RIGHT]:
                self.player_position[0] += self.move_speed
                if self.player_position[0] >= 1498:
                    self.player_position[0] = 1498
            if keys[pygame.K_UP]:
                self.player_position[1] -= self.move_speed
                if self.player_position[1] <= 0:
                    self.player_position[1] = 0
            if keys[pygame.K_DOWN]:
                self.player_position[1] += self.move_speed
                if self.player_position[1] >= 956:
                    self.player_position[1] = 956
        if self.check_for_combat():
            self.in_combat = True
            
        if self.blue_orb and self.check_orb_collision():
            return 'quit'


    def draw(self):
        """
        Draw the game objects on the window.
        """
        self.window.fill((0, 0, 0)) 
        self.window.blit(self.map_image, (0, 0))
        self.window.blit(self.player_image, (self.player_position[0], self.player_position[1]))
        for enemy in self.enemies:
            enemy.draw()
        if self.blue_orb:
            self.window.blit(self.blue_orb, self.orb_position)
        pygame.display.flip()

    def gameState(self):
        if self.in_combat == True:
            return "Combat"

        else:
            return "Regular"
        
    def getPlayer(self):
        return self.player

    def getCurrentEnemy(self):
        return self.current_enemy