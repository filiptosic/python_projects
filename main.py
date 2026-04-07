import sys
import pygame
import time

class Sprite():
    def __init__(self, size, reduced_size):
        self.size = size
        self.reduced_size = reduced_size


#initializa pygame and set window size and title
pygame.init()
pygame.display.set_caption("Air Brake Game")
screen = pygame.display.set_mode((900, 720))
clock = pygame.time.Clock()

#load in images
gas = pygame.image.load('gas.png')
brake = pygame.image.load('brake.png')
maxi = pygame.image.load('maxi.png')
air1 = pygame.image.load('air1real.png')
air2 = pygame.image.load('air2real.png')
needle = pygame.image.load('needle.png')

#define new image sizes
brake_size = [125,150]
gas_size = [125, 150]
maxi_size = [100, 100]
air1_size = [200, 200]
air2_size = [200, 200]
needle_size =[100, 100]

#define image locations
brake_location = [30, 550]
gas_location = [155, 550]
maxi_location = [500, 200]
air1_location = [0, 0]
air2_location = [210, 0]
needle_location = [25, 70]

#resize images in pygame using transform.smoothscale() method
resize_maxi = pygame.transform.smoothscale(maxi, maxi_size)
resize_brake = pygame.transform.smoothscale(brake, brake_size)
resize_gas = pygame.transform.smoothscale(gas, gas_size)
resize_air1 = pygame.transform.smoothscale(air1, air1_size)
resize_air2 = pygame.transform.smoothscale(air2, air2_size)
resize_needle = pygame.transform.smoothscale(needle, needle_size)

#initialize font
global font
font=pygame.font.Font(None,30)

#base text color of white
text_color = (220, 220, 220)

#warning color of red
warning_color=(255, 0, 0)

#used to reset color back to white
color = (220, 220, 220)

#default timer increment. Used to determine base rate at which pressure builds
time_timer = 1000
pressure1 = 120
pressure2 = 120

#used only for displaying truck on or off. Air pressure starts and stops building based off of key_on variable. This could be removed in later iterations
truck_on = True

#write function used to display text on screen
def write(text,location,color=(240,240,240)):
    screen.blit(font.render(text,True,color),location)

while True:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        screen.fill((0, 0, 0))
        
        #list of truck controls
        write("Press 0 to start truck", (550,15))
        write("Press 1 to shut off", (550,35))
        write("Press B to brake", (550, 55))
        write("Press G to increase RPM", (550,75))
        #initializes key_on variable which is used to increment pressure every x milliseconds as determined by time_timer variable
        key_on = pygame.USEREVENT
        pygame.time.set_timer(key_on, time_timer)

        #resized brake, gas, and maxi variables. These have to be done within this loop otherwise they will not reset properly.
        resize_brake = pygame.transform.smoothscale(brake, brake_size)
        resize_gas = pygame.transform.smoothscale(gas, gas_size)
        resize_maxi = pygame.transform.smoothscale(maxi, maxi_size)

        #builds pressure up to maximum of 120 if key is on
        if event.type == key_on and pressure1 < 120:
            pressure1 += 1
        if event.type == key_on and pressure2 < 120:
            pressure2 += 1

        #displays all sprites and images onto screen
        screen.blit(resize_air1, air1_location)
        screen.blit(resize_air2, air2_location)
        screen.blit(resize_needle, needle_location)
        screen.blit(resize_brake, brake_location)
        screen.blit(resize_gas, gas_location)
        screen.blit(resize_maxi, maxi_location)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # turns truck on and sets timer (pressure build up rate) to base speed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                key_on = pygame.USEREVENT
                time_timer = 1000
                truck_on = True
        # turns truck off and shuts off timer thus stopping air pressure build up
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key_on = False
                truck_on = False
                time_timer = 0

        # handles displaying truck on/off
        if truck_on:
            write("Truck ON", (450, 460), color=('green'))
        else:
            write("Truck OFF", (450, 460), color=('yellow'))
        
        # increases build speed up by changing timer interval if acclerator pedal is held down. This will be converted to clickable button later.
        # meant to represent increased idle speed/RPM
        if pressed[pygame.K_g] and truck_on == True:
                key_on = True
                if pressure1 < 120:
                    pressure1 += 1
                if pressure2 < 120:
                    pressure2 += 1
                time_timer = 800
                gas_size[0] = 95
                gas_size[1] = 120
                gas_location[0] = 170
                gas_location[1] = 565

        # returns variables and locations to normal when button is no longer being held down
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_g:
                gas_location = [155, 550]
                time_timer = 1000
                gas_size[0] = 125
                gas_size[1] = 150

        # used to decrement air pressure by 2 and reduce brake size and location with every press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                brake_size[0] -= 30
                brake_size[1] -= 30
                brake_location[0] += 15
                brake_location[1] += 15
                if 2 <= pressure1:
                    pressure1 -= 2
                if 2 <= pressure2:
                    pressure2 -= 2
                print(pressure1)
    
    # brings brake size and location back to normal after presses
    brake_location = [30, 550]
    brake_size = [125, 150]
    press1_to_string = str(pressure1)
    press2_to_string = str(pressure2)

    # displays air pressure
    write(press1_to_string, (90, 200), text_color)
    write(press2_to_string, (300, 200), text_color)
    if pressure1 <= 60:
        text_color = warning_color
        write("LOW AIR", (45, 220), text_color)
    else:
        text_color = color
    if pressure1 < 38:
        maxi_size = [200, 200]

    pygame.display.update()
    # print(event)
    clock.tick(60)
    