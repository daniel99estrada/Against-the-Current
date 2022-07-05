import pygame
from pygame.locals import *


# main screen dimensions
SIZE = WIDTH,HEIGHT= (700, 600)

# road dimensions
road_w = int(WIDTH / 1.3)
roadMark_w = int(WIDTH /80)

# lane dimensions
right_lane = int(WIDTH/2 + road_w/3 - roadMark_w)
middle_lane = int(WIDTH/2)
left_lane = int(WIDTH/2 - road_w/3 + roadMark_w)

# Option screen dimensions
screen_w = WIDTH * 0.8
screen_h = HEIGHT * 0.25
screen_y = HEIGHT * 0.2
screen_x = WIDTH * 0.1
border_w = WIDTH // 80

# RGB color values
colorBLUE = (0,0,255)
colorGREEN = (0,200,100)
colorGRAY = (100,100,100)
colorRED = (255,0,0)
colorYELLOW = (255,240,60)
colorWHITE = (255,255,255)
colorBLACK = (0,0,0)

# cars' starting position
car_position = (middle_lane, HEIGHT * 0.8)
carA_position = (left_lane, HEIGHT * 0.2)
carB_position = (right_lane, HEIGHT * 0.1)

# Print message to screen function
def message_to_screen(screen, message= "", size=50, color=colorBLACK, x=20, y=20):

    font = pygame.font.SysFont(None, size)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(x,y))
    screen.blit(text, text_rect)

