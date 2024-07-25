import pygame, sys
from assets import GAME_ASSETS
from button import Button

def makeFont(size):
    return pygame.font.Font("font.ttf", size)
    
class LoseScreen():
    def __init__(self, window):
        self.window = window
        self.font = makeFont(36)
        self.background_image = pygame.image.load('loseScreen_Background.png')
        self.scaled_background = pygame.transform.scale(self.background_image, (self.window.get_width(), self.window.get_height()))
        self.LOSE_TEXT = makeFont(100).render("YOU LOSE", True, "#37FF00")
        self.LOSE_TEXT_RECT = self.LOSE_TEXT.get_rect(center=(896, 80))
        self.BACK_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(896, 828), 
                                text_input="BACK", font=makeFont(75), base_color="#d7fcd4", hovering_color="White")
    
        
        

    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        running = True

        while running:
            self.window.blit(self.scaled_background, (0, 0))
            self.window.blit(self.LOSE_TEXT, self.LOSE_TEXT_RECT)
            for button in [self.BACK_BUTTON]:
                button.changeColor(mouse_pos)
                button.update(self.window)
            pygame.display.flip()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.BACK_BUTTON.checkForInput(event.pos):
                            return 'back'