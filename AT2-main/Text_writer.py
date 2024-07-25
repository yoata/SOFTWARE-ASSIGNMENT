import pygame


class TextRenderer:
   def __init__(self, window, text_area, font_size):
       self.__window = window
       self.__text_area = text_area
       pygame.font.init()
       self.__font = pygame.font.Font(None, font_size)
       self.__first_space, self.__first_line = self.__text_area.topleft
       self.__current_line = 0
       self.__line_spacing = self.__font.get_height() + 5  # Adjust the line spacing as needed


   # Accessors
   def getWindow(self):
       return self.__window


   def getTextArea(self):
       return self.__text_area


   def getFont(self):
       return self.__font


   def getCurrentLine(self):
       return self.__current_line


   def getFirstSpace(self):
       return self.__first_space
   
   def getFirstLine(self):
       return self.__first_line


   # Mutators
   def setWindow(self, newWindow):
       self.__window = newWindow


   def setTextArea(self, newTextArea):
       self.__text_area = newTextArea
       self.__first_space, self.__first_line = newTextArea.topleft


   def setFont(self, newFont):
       self.__font = newFont


   def setCurrentLine(self, newCurrentLine):
       self.__current_line = newCurrentLine


   def setFirstSpace(self, newFirstSpace):
       self.__first_space = newFirstSpace
   
   def setFirstLine(self, newFirstLine):
       self.__first_line = newFirstLine


   # Behaviors
   def write_text(self, text):
       words = text.split(' ')


       x = self.getFirstSpace()  # x-coordinate of the current space to write on
       y = self.getFirstLine() + self.getCurrentLine() * self.__line_spacing  # y-coordinate of the current line


       space_width, space_height = self.__font.size(' ')
       max_width, max_height = self.__text_area.size


       for word in words:
           word_surface = self.__font.render(word, True, (255, 255, 255))
           word_width, word_height = word_surface.get_size()


           if x + word_width >= self.__text_area.right:
               x = self.getFirstSpace()
               self.__current_line += 1
               y = self.getFirstLine() + self.getCurrentLine() * self.__line_spacing


           if y + word_height > self.__text_area.bottom:
               break  # Stop rendering text if it exceeds the text area height
               
           self.__window.blit(word_surface, (x, y))
           x += word_width + space_width


       self.__current_line += 2  # Move down 1 line for the next text


   def display_output(self, output):
       for event in output:
           self.write_text(event)


       self.__current_line = 0  # Reset the line that the writing begins to the first line

