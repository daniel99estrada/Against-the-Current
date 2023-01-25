from pickle import FALSE, TRUE
import pygame
import time
from settings import *
import random
from pygame.locals import *
import sys

# Set global variables
class CarGame:
    def __init__(self):
        self.currentMove = 1
        self.lanes = {0:left_lane, 1:middle_lane, 2:right_lane}
game = CarGame()

# Initialize all Pygame modules.
pygame.init()
running = True
pygame.display.set_caption("Against the Current")
screen = pygame.display.set_mode(SIZE)

# Fill Screen with color
screen.fill(colorGREEN)

# draw the road.
def draw_road():

    # drraw  the Asphalt
    pygame.draw.rect(
        screen,
        colorGRAY,
        (WIDTH/2 - road_w/2, 0, road_w, HEIGHT))
    
    # draw outer yellow lanes
    pygame.draw.rect(
        screen,
        colorYELLOW,
        (WIDTH/2 - road_w/2 + roadMark_w*2, 0, roadMark_w, HEIGHT))

    pygame.draw.rect(
        screen,
        colorYELLOW,
        (WIDTH/2 + road_w/2 - roadMark_w* 3, 0, roadMark_w, HEIGHT))
    
    # draw middle white lanes
    pygame.draw.rect(
        screen,
        colorWHITE,
        (WIDTH/3 + roadMark_w*3, 0, roadMark_w, HEIGHT))  
        
    pygame.draw.rect(
        screen,
        colorWHITE,
        (WIDTH - WIDTH/3 - roadMark_w*4, 0, roadMark_w, HEIGHT))

def draw_options_screen():

    # main frame
    pygame.draw.rect(
        screen,
        colorWHITE,
        (screen_x, screen_y, screen_w, screen_h))
    
    # frame borders
    pygame.draw.rect(
        screen,
        colorBLACK,
        (screen_x, screen_y, border_w, screen_h))   
    pygame.draw.rect(
        screen,
        colorBLACK,
        (WIDTH*0.9, screen_y, border_w, screen_h))
    pygame.draw.rect(
        screen,
        colorBLACK,
        (screen_x, screen_y, screen_w, border_w))
    pygame.draw.rect(
        screen,
        colorBLACK,
        (screen_x, screen_y + screen_h - border_w, screen_w, border_w))   

# pause game
def optionScreen(mainMessage, counter = 0):
    paused = TRUE
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    paused = False  
        
        # draw current game status
        draw_road()
        screen.blit(car, car_loc)
        screen.blit(carA, carA_loc)
        screen.blit(carB, carB_loc)

        # draw options screen
        draw_options_screen()  
        message_to_screen(screen,"AGAINST THE CURRENT",size =45, x = WIDTH/2 , y = screen_h * 0.2 + screen_y)
        message_to_screen(screen,"by Moon Moon Games™",size =25, x = WIDTH/2 , y = screen_h * 0.35  + screen_y)
        message_to_screen(screen, mainMessage, size=40, x = WIDTH/2 , y = screen_h * 0.55 + screen_y)

        # Motion text
        if counter < 80:
            message_to_screen(screen,"- - - Press spacebar to continue - - -", size=25, x = WIDTH/2 , y = screen_h * 0.8 + screen_y)              
        if counter == 160:
            counter = 0
        counter += 1

        pygame.display.update()        

# load car image
car = pygame.image.load("assets/yellow_car.png")
car = pygame.transform.scale(car, (250, 250))
car_loc = car.get_rect()
car_loc.center = car_position

# load enemy car A image
carA = pygame.image.load("assets/white_car.png")
carA = pygame.transform.scale(carA, (250, 250))
carA_loc = car.get_rect()
carA_loc.center = carA_position

# load enemy car B image
carB = pygame.image.load("assets/white_car.png")
carB = pygame.transform.scale(carB, (250, 250))
carB_loc = car.get_rect()
carB_loc.center = carB_position

speed = 2
counter = 0
level = 1
collision = False

optionScreen("Welcome")
pygame.display.update()
while TRUE:

    # check for ongoing events in the game
    for event in pygame.event.get():

        # clicking the X button quits the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # pressing the ESC key quits the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # spacebar pauses the game
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print("Player Car location: " + str(car_loc.center[1]))
                print("White Car location: " + str(carA_loc.center[1]))
                print("Blue Car location: " + str(carB_loc.center[1]))               
                optionScreen("Paused")
                
        # switch lanes
        if event.type == KEYDOWN:
            if event.key in [K_a,K_LEFT] and game.currentMove != 0:
                game.currentMove -= 1
                car_loc.center = game.lanes[game.currentMove], HEIGHT * 0.8

        if event.type == KEYDOWN:
            if event.key in [K_d,K_RIGHT] and game.currentMove != 2:
                game.currentMove += 1
                car_loc.center = game.lanes[game.currentMove], HEIGHT * 0.8      

    # check if cars collide
    if (car_loc[0] == carA_loc[0]):
        if carA_loc.center[1] < car_loc.center[1] + 250 and carA_loc.center[1] > car_loc.center[1] - 250:
            collision = True

    if (car_loc[0] == carB_loc[0]):
        if carB_loc.center[1] < car_loc.center[1] + 250 and carB_loc.center[1] > car_loc.center[1] - 250:
            collision = True

    if collision:
        optionScreen("GAME OVER")
        optionScreen("Welcome")
        car_loc.center = car_position
        carA_loc.center = carA_position
        carB_loc.center = carB_position
        game.currentMove = 1  
        speed = 2
        level = 1
        collision = False

    # update screen
    screen.fill(colorGREEN)
    draw_road()
    message_to_screen(screen,"LEVEL: " + str(level),size =22, x = WIDTH * 0.06 , y = HEIGHT  * 0.05)
    screen.blit(car, car_loc)
    screen.blit(carA, carA_loc)
    screen.blit(carB, carB_loc) 
    
    if counter == 400:
        speed += 0.5
        level += 1
        counter = 0  
    
    counter += 1         

    carA_loc[1] += speed
    carB_loc[1] += speed

    # move cars at the top of the screen once they reach the bottom.
    if carA_loc[1] > HEIGHT:
        A_lane = random.randint(0,2)
        carA_loc.center = game.lanes[A_lane], - HEIGHT 
        
    if carB_loc[1] > HEIGHT:
        B_lane = random.randint(0,2)
        carB_loc.center = game.lanes[B_lane], - HEIGHT * 1.7
    
    # change car B's location if it is in the same lane as car A and at a car's distance from it.
    if carA_loc.center[0] == carB_loc.center[0]:
        if abs(carA_loc.center[1] - carB_loc.center[1]) < 300:
            carB_loc.center = (carB_loc.center[0],carB_loc.center[1] - 250)

    pygame.display.update()
