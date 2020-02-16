import colors
import pygame
import math
import time
from display_bck import draw_bck
from tkinter import *

""" This module draws the radar screen """

def draw(radarDisplay, targets, angle, distance, fontRenderer, screen_width, screen_height, color):
     # draw initial screen
    radarDisplay.fill(color)
    x1=(0.7*screen_width)
    x2=(0.95*screen_width)
    y1=(0.1*screen_height)
    y2=(0.15*screen_height)
    
    quit_button = pygame.draw.rect(radarDisplay,(244,0,0),(x1,y1,100,50));
    for evento in pygame.event.get():
        #print(evento);
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= x1 and pygame.mouse.get_pos()[1] >= y1:
                if pygame.mouse.get_pos()[0] <= x1+100 and pygame.mouse.get_pos()[1] <= y1+50:
                        sys.exit()
           

    pygame.draw.circle(radarDisplay, colors.green, ((round(screen_width/2)),(round(screen_height))), (round(screen_width/2)), 1)

    pygame.draw.circle(radarDisplay, colors.green, ((round(screen_width/2)),(round(screen_height))), (round((screen_width/2)-100)), 1)

    pygame.draw.circle(radarDisplay, colors.green, ((round(screen_width/2)),(round(screen_height))), (round((screen_width/2)-200)), 1)

    pygame.draw.circle(radarDisplay, colors.green, ((round(screen_width/2)),(round(screen_height))), (round((screen_width/2)-300)), 1)

    pygame.draw.circle(radarDisplay, colors.green, ((round(screen_width/2)),(round(screen_height))), (round((screen_width/2)-350)), 1)

    radarDisplay.fill(colors.white, [0, 785, 1400, 20])

    # horizental line
    pygame.draw.line(radarDisplay, colors.green, (0, (round(screen_height))), ((round(screen_width)), (round(screen_height))), 4)

    # 45 degree line
    pygame.draw.line(radarDisplay, colors.green, (0, 0),((round(screen_width/2)), (round(screen_height))), 1)

    # 90 degree line
    pygame.draw.line(radarDisplay, colors.green, (((round(screen_width/2))), 0), (((round(screen_width/2))), (round(screen_height))), 1)

    # 135 degree line
    pygame.draw.line(radarDisplay, colors.green, ((round(screen_width/2)), (round(screen_height))), ((round(screen_width)), 0), 1)

    # draw stastics board
    pygame.draw.rect(radarDisplay, colors.blue, [20, 20, 270, 100], 2)

    # write the 0 degree
    text = fontRenderer.render("0", 1, colors.green)
    radarDisplay.blit(text,(10,(0.95*(round(screen_height)))))

    # write the 45 degree
    text = fontRenderer.render("45", 1, colors.green)
    radarDisplay.blit(text,(15,10))

    # write the 90 degree
    text = fontRenderer.render("90", 1, colors.green)
    radarDisplay.blit(text,(((round(screen_width/2))+15),10))

    # write the 135 degree
    text = fontRenderer.render("135", 1, colors.green)
    radarDisplay.blit(text,(((round(screen_width)*0.9)),10))

    # write the 180 degree
    text = fontRenderer.render("180", 1, colors.green)
    radarDisplay.blit(text,(((round(screen_width)*0.9)),(0.95*(round(screen_height)))))

    # draw the moving line
    a = math.sin(math.radians(angle)) * (1.1*(round(screen_width/2)))
    b = math.cos(math.radians(angle)) * (1.1*(round(screen_width/2)))
    pygame.draw.line(radarDisplay, colors.green, (round((screen_width/2)), round((screen_height))), ((round(screen_width/2))-int(b), (round(screen_height)) - int(a)), 3)


    # write the current angle
    text = fontRenderer.render("Angle : " + str(angle), 1, colors.white)
    radarDisplay.blit(text,(40,40))

    # write the distance
    if distance == -1:
        text = fontRenderer.render("Distance : Out Of Range" , 1, colors.white)
    else:
        text = fontRenderer.render("Distance : " + str(distance) + " cm" , 1, colors.white)

    radarDisplay.blit(text,(40,80))

    # draw targets
    for angle in targets.keys():
        # calculate the coordinates and the remoteness of the target
        c = math.sin(math.radians(targets[angle].angle)) * (1.1*(round(screen_width/2)))
        d = math.cos(math.radians(targets[angle].angle)) * (1.1*(round(screen_width/2)))
    # change the scale if the range is changed
        e = math.sin(math.radians(targets[angle].angle)) * ((round(screen_width/2))/ 50) * targets[angle].distance
        f = math.cos(math.radians(targets[angle].angle)) * ((round(screen_width/2))/ 50) * targets[angle].distance

        # draw the line indicating the target
        pygame.draw.line(radarDisplay, targets[angle].color, ((round(screen_width/2))- int(f), (round(screen_height)) - int(e)), ((round(screen_width/2)) - int(d), (round(screen_height)) - int(c)), 3)
        
        # fading

        diffTime = time.time() - targets[angle].time
        
        if diffTime >= 0.0 and diffTime <= 0.2:
            targets[angle].color = colors.red1L
        elif diffTime > 0.2 and diffTime <= 0.6:
            targets[angle].color = colors.red2L
        elif diffTime > 0.6 and diffTime <= 1:
            targets[angle].color = colors.red3L
        elif diffTime > 1 and diffTime <= 2.0:
            """targets[angle].color = colors.red4L
        elif diffTime > 2.0 and diffTime <= 2.5:
            targets[angle].color = colors.red5L
        elif diffTime > 2.5 and diffTime <= 3.0:
            targets[angle].color = colors.red6L
        elif diffTime > 3.0:"""
           # targets[angle].color = colors.black
            
    draw_bck(radarDisplay, fontRenderer, screen_width, screen_height)    



# update the screen
    pygame.display.update()
    
