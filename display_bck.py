import colors
import pygame
import math
import time

""" This module draws the radar screen """

def draw_bck(radarDisplay, fontRenderer, screen_width, screen_height):
     # draw initial screen
    #radarDisplay.fill(colors.black)

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

# update the screen
    pygame.display.update()
    
