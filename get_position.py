import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg


def mouse_pos(x=768,y=576):
    x=768
    y=576
    
    back_color = (255, 255, 255)
    red = (255, 0, 0)
    
    pg.init()
    screen = pg.display.set_mode((x, y))
    
    pg.event.pump()
    screen.fill(back_color)
    pg.display.update()
    
    positions = []
   
    i=0
    while True:        
        event = pg.event.wait()
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            i+=1
            positions.append([i,event.pos])
            pg.draw.circle(screen, red, event.pos, 5)
            pg.display.update()
            pg.time.delay(200)
            
        if event.type == pg.KEYDOWN:
            pg.display.quit()
            pg.quit()
            break
     
    return positions


     



                