import random
import pygame

from mage import Mage
from warrior import Warrior
from rogue import Rogue
from assets import GAME_ASSETS
from enemy import Enemy
from Bar import Bar

class Combat:
    def __init__(self, window, player, enemy):
        """
        Initialize the Map class.

        Args:
            window (pygame.Surface): The game window surface.
        """
        self.window = window
        self.player = player
        self.enemy = enemy
        self.map_image = pygame.image.load(GAME_ASSETS["dungeon_map"]).convert_alpha()
        self.map_image = pygame.transform.scale(self.map_image, (self.window.get_width(), self.window.get_height()))
        self.player_images = {
            'Warrior': pygame.image.load(GAME_ASSETS['warrior']).convert_alpha(),
            'Mage': pygame.image.load(GAME_ASSETS['mage']).convert_alpha(),
            'Rogue': pygame.image.load(GAME_ASSETS["rogue"]).convert_alpha()
        }
        self.player_death = False
        self.has_chosen_attack = False
        self.player_turn = True
        self.enemy_turn = False
        self.heath_bar_player = Bar(self.player.current_hp, self.player.max_hp, 500, 500)
        self.heath_bar_enemy = Bar(self.enemy.health, 100, 700, 700)
    
    def load_player(self, character_type):
        self.player_type = character_type
        self.player_image = self.player_images[character_type]
        self.player_image = pygame.transform.scale(self.player_image, (int(self.player_image.get_width() * 2), int(self.player_image.get_height() * 2)))


    def handle_combat(self):
        enemy_damage = random.randint(15, 40)
        player_defeated = self.player.take_damage(enemy_damage)
        print(f"Enemy attacks back! Deals {enemy_damage} damage to the player.")
        if player_defeated:
            print("PLAYER DIED")
            self.in_combat = False
            self.player_death = True
            return 'Enemy Turn End'
        return 'Enemy Turn End'
            
            
    
    def Player_deal_damage(self, attack):
        self.player.choose_attack(self.current_enemy, attack)
        damage = self.player.Get_current_damage()
        enemy_defeated = self.current_enemy.is_dead(damage)
        print(f"Player attacks! Deals {damage} damage to the enemy.")
        if enemy_defeated:
            print("Enemy defeated!")
            self.enemies.remove(self.current_enemy)
            self.in_combat = False
            self.current_enemy = None
            if not self.enemies:
                self.spawn_blue_orb()   
        self.Attack_number = None
        self.has_chosen_attack = False

    def playerTurn(self):
                for event in pygame.event.get():
                    if event.type == pygame.K_ESCAPE:
                        pygame.quit()

                    if event.type == pygame.QUIT:
                        break
                    
                    if event.type == pygame.KEYDOWN:
                            
                        if event.type == pygame.K_1:  
                            self.Attack_number = 1
                            self.has_chosen_attack == True
                            break

            
                        if event.type == pygame.K_2:  
                            self.Attack_number = 2
                            self.has_chosen_attack == True
                            break


                        if event.type == pygame.K_3:  
                            self.Attack_number = 3
                            self.has_chosen_attack == True
                            break
                            

                        if event.type == pygame.K_4:  
                            self.Attack_number = 4
                            self.has_chosen_attack == True
                            break


                        if event.type == pygame.K_5:  
                            self.Attack_number = 5
                            self.has_chosen_attack == True
                            break
                

    def Turnbased(self, comabt):
        if self.player_turn == True:
               print("player turn")
               comabt.playerTurn()
               if self.has_chosen_attack == True:
                    print("here")
                    self.Player_deal_damage(self.Attack_number)
                    self.has_chosen_attack = False
                    self.player_turn = False
                    self.enemy_turn = True
        
        if self.enemy_turn == True:
            print("enemy turn")
            turn_result = comabt.handle_combat()
            if turn_result == "Enemy Turn End":
                self.enemy_turn = False
                self.player_turn = True

        
              

    def draw(self):
        self.window.fill((0, 0, 0)) 
        self.window.blit(self.map_image, (0, 0))
        self.window.blit(self.player_image, (200, 100))
        self.enemy.COMBATDRAW()
        self.heath_bar_player.draw(self.window, (255,0,0))
        self.heath_bar_enemy.draw(self.window, (0,0,255))
        pygame.display.flip()