import RPi.GPIO as GPIO
import pygame
import math
import time
import colors
import sys
from Target import *
from display import draw
from grove.gpio import GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger

#radar display config
x = pygame.init()
pygame.font.init()
defaultFont = pygame.font.get_default_font()
fontRenderer = pygame.font.Font(defaultFont, 20)
radarDisplay = pygame.display.set_mode((1400, 800))
pygame.display.set_caption('Radar Screen')
#GPIO setup

RangerRead = GroveUltrasonicRanger(5)

# targets list
targets = {}

#radar read and write to dict
while True:
    for angle in range(0,180):
        distance = RangerRead.get_distance()
        distance = round(distance, 2)
        if distance != -1 and distance <= 10:
            targets[angle]=Target(angle, distance)
        
        draw(radarDisplay, targets, angle, distance, fontRenderer)
        time.sleep(0.001)
        
        
    for angle in range(180,0,-1):
        distance = RangerRead.get_distance()
        distance = round(distance, 2)
        if distance !=-1 and distance <=10:
            targets[angle]=Target(angle, distance)
            
        draw(radarDisplay, targets, angle, distance, fontRenderer)
        time.sleep(0.001)
    
    
        


        
