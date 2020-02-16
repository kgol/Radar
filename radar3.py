import RPi.GPIO as GPIO
import pygame
import math
import time
import colors
import sys
from Target import *
from display import draw
from display_bck import draw_bck
from grove.gpio import GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

def radar (width, height, color):
#radar display config
    screen_width = width
    screen_height = height
    x = pygame.init()
    pygame.font.init()
    defaultFont = pygame.font.get_default_font()
    fontRenderer = pygame.font.Font(defaultFont, 20)
    #screen_width = 800
    #screen_height =500
    radarDisplay = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Radar Screen')
    #GPIO setup

    RangerRead = GroveUltrasonicRanger(5)

    # targets list
    targets = {}
    a=0
    #radar read and write to dict
    while True:
        for angle in range(0,180):
            distance = RangerRead.get_distance()
            distance = round(distance, 2)
            if distance != -1 and distance <= 50:
                targets[angle]=Target(angle, distance)
        
            draw(radarDisplay, targets, angle, distance, fontRenderer, screen_width, screen_height, color)
            time.sleep(0.0001)
            #draw_bck(radarDisplay, fontRenderer, screen_width, screen_height)
        targets={}
        
        
        for angle in range(180,0,-1):
            distance = RangerRead.get_distance()
            distance = round(distance, 2)
            if distance !=-1 and distance <=50:
                targets[angle]=Target(angle, distance)
            
            draw(radarDisplay, targets, angle, distance, fontRenderer, screen_width, screen_height, color)
            time.sleep(0.0001)
 
            #draw_bck(radarDisplay, fontRenderer, screen_width, screen_height)
        
        targets={}