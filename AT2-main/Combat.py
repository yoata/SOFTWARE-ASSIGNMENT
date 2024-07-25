import random
import pygame
from Text_writer import TextRenderer
from assets import GAME_ASSETS
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
        self.width = int(self.window.get_width())
        self.height = int(self.window.get_height())
        self.map_image = pygame.image.load("Turnbased image.jpg").convert_alpha()
        self.map_image = pygame.transform.scale(self.map_image, (self.window.get_width(), 700))
        self.test_box = pygame.image.load("testBox.png").convert_alpha()
        self.test_box = pygame.transform.scale(self.test_box, (self.width, self.height - 700))
        self.player_images = {
            'Warrior': pygame.image.load(GAME_ASSETS['warrior']).convert_alpha(),
            'Mage': pygame.image.load(GAME_ASSETS['mage']).convert_alpha(),
            'Rogue': pygame.image.load(GAME_ASSETS["rogue"]).convert_alpha()
        }
        self.player_death = False
        self.has_chosen_attack = False
        self.player_turn = True
        self.enemy_turn = False
        self.textmaker = TextRenderer(self.window, pygame.rect.Rect(0, 700, self.width, (self.height - 700)), 5)
        pygame.font.init()
        self.font = pygame.font.Font(None, 50)
        self.attacks_font = pygame.font.Font(None, 25)
        
    
    def load_player(self, character_type):
        self.player_type = character_type
        self.player_image = self.player_images[character_type]
        self.player_image = pygame.transform.scale(self.player_image, (int(self.player_image.get_width() * 1.5), int(self.player_image.get_height() * 1.5)))

    def load_bars(self):
        self.heath_bar_player = Bar((self.player_image.get_width()), (self.player.getMax_Hit_points()), (self.player.getHit_points()), 200, (int(self.player_image.get_height()) + 350), self.window, (255,0,0), (0,255,0))
        self.heath_bar_enemy = Bar((self.enemy.combat_image.get_width()), (self.enemy.getMaxHP()), (self.enemy.getHP()), 1000, (int(self.enemy.combat_image.get_height()) +300), self.window, (255,0,0), (0,255,0))
        self.stamina_bar = Bar((self.player_image.get_width()), (self.player.getMaxStamina()), (self.player.getStamina()), 200, (int(self.player_image.get_height()) + 375), self.window, (255, 255, 255), (0,0,255))
    
    def handle_combat(self):
        enemy_damage = random.randint(15, 40)
        player_defeated = self.player.take_damage(enemy_damage)
        if player_defeated:
            print("PLAYER DIED")
            return 'PLAYER DIED'
        return str(f"{self.enemy.name} attacks back! Deals {enemy_damage} damage to the player.")
    

    def pause(self):
        hit_key = None
        while not hit_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:    
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        hit_key = 1   
        return hit_key
    
    def playerTurn(self):
        chosen_attack = None
        attacks = self.player.getAttacks()
        line1 = "Choose attack by hitting corresponding key"
        line2 = attacks[0]
        line3 = attacks[1]
        line4 = attacks[2]
        line5 = attacks[3]
        line6 = attacks[4]
        
        line1_text = self.attacks_font.render(line1, False, (255, 255, 255))
        line2_text = self.attacks_font.render(line2, False, (255, 255, 255))
        line3_text = self.attacks_font.render(line3, False, (255, 255, 255))
        line4_text = self.attacks_font.render(line4, False, (255, 255, 255))
        line5_text = self.attacks_font.render(line5, False, (255, 255, 255))
        line6_text = self.attacks_font.render(line6, False, (255, 255, 255))

        self.window.blit(line1_text, (100, 750))
        self.window.blit(line2_text, (100, 775))
        self.window.blit(line3_text, (100, 800))
        self.window.blit(line4_text, (100, 825))
        self.window.blit(line5_text, (100, 850))
        self.window.blit(line6_text, (100, 875))

        pygame.display.flip()

        line1_text = self.attacks_font.render(line1, False, (0, 0, 0))
        line2_text = self.attacks_font.render(line2, False, (0, 0, 0))
        line3_text = self.attacks_font.render(line3, False, (0, 0, 0))
        line4_text = self.attacks_font.render(line4, False, (0, 0, 0))
        line5_text = self.attacks_font.render(line5, False, (0, 0, 0))
        line6_text = self.attacks_font.render(line6, False, (0, 0, 0))

        self.window.blit(line1_text, (100, 750))
        self.window.blit(line2_text, (100, 775))
        self.window.blit(line3_text, (100, 800))
        self.window.blit(line4_text, (100, 825))
        self.window.blit(line5_text, (100, 850))
        self.window.blit(line6_text, (100, 875))

        while not chosen_attack: # Repeats a loop checking for key inputs until an attack is chosen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:    
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        chosen_attack = 1
                    elif event.key == pygame.K_2:
                        chosen_attack = 2
                    elif event.key == pygame.K_3:
                        chosen_attack = 3
                    elif event.key == pygame.K_4:
                        chosen_attack = 4
                    elif event.key == pygame.K_5:
                        chosen_attack = 5

        return chosen_attack
            


                

    def Turnbased(self):
        if self.player_turn == True:
               attack_choozer = self.playerTurn()
               player_deal_damage = self.player.choose_attack(self.enemy, attack_choozer)
               if player_deal_damage == "Invalid attack":
                    player_message = self.font.render("Please Input A Valid Attack", False, (255, 255, 255))
                    self.window.blit(player_message, (100, 750))
                    pygame.display.flip()
                    self.pause()
                    pass
                   
               elif player_deal_damage == "no stam":
                    player_message = self.font.render("Not Enough Stamina For Chosen Attack", False, (255, 255, 255))
                    self.window.blit(player_message, (100, 750))
                    pygame.display.flip()
                    self.pause()
                    pass

               elif player_deal_damage == "attack complete":
                      self.stamina_bar.update()
                      attack_message = self.player.get_current_attack_message()
                      player_message = self.font.render(attack_message, False, (255, 255, 255))
                      self.window.blit(player_message, (100, 750))
                      self.heath_bar_enemy.update()
                      pygame.display.flip()        
                      self.pause()
                      player_message = self.font.render(attack_message, False, (0, 0, 0))
                      self.window.blit(player_message, (100, 750))
                      pygame.display.flip()
                      enemy_alive = self.enemy.is_alive()
                      if enemy_alive == "dead":
                        self.player.healthRegen()
                        return "Enemy Death"
                      self.player_turn = False
                      self.enemy_turn = True
                   
                       
                
        
        if self.enemy_turn == True:
            turn_result = self.handle_combat()
            self.heath_bar_player.update()
            self.player.regenerate_stamina()
            if turn_result == "PLAYER DIED":
                return "player death"
            
            else:
                enemy_message = self.font.render(turn_result, False, (255, 255, 255))
                self.window.blit(enemy_message, (100, 750))
                pygame.display.flip()
                self.pause()
                self.enemy_turn = False
                self.player_turn = True

        

        
              

    def draw(self):
        self.window.fill((0, 0, 0)) 
        self.window.blit(self.map_image, (0, 0))
        self.window.blit(self.player_image, (200, 350))
        self.enemy.COMBATDRAW(1000, 300)
        pygame.draw.rect(self.window, (0,0,0), (0, 700, self.window.get_width(), int(self.window.get_height()) - 700))
        pygame.draw.rect(self.window, (255,255,255), (0, 700, self.window.get_width(), int(self.window.get_height()) - 700), 4)
        self.stamina_bar.draw()
        self.heath_bar_enemy.draw()
        self.heath_bar_player.draw()
        pygame.display.flip()

    def getPlayer(self):
        return self.player
    
                        