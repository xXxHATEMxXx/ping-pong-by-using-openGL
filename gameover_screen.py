import pygame 
import sys
from pygame import mixer 

global M
M=1
# initializing the constructor 
pygame.init() 

pygame.init() 
  
mixer.init()

mixer.music.load("WhatsApp Audio 2022-05-22 at 1.53.18 PM.mp3")

mixer.music.set_volume(0.7)

mixer.music.play()
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',100) 
  
# rendering a text written in 
# this font 
text_start = smallfont.render('GameOver' , True , color)

while M==1: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
        #checks if a mouse is clicked 


                

                
                  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
      
    # superimposing the text onto our button 

    screen.blit(text_start , (width/5,height/3))

      
    # updates the frames of the game 
    pygame.display.update() 