import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

def mouse_pos(k,x=768,y=576):
    pg.init()
    screen = pg.display.set_mode((x, y))
    clicks = []
    done=False 
    i=0
    while not done:
        for event in pg.event.get():
            #if event.type == pg.QUIT:
            if i==k:
                done=True
            elif event.type == pg.MOUSEBUTTONDOWN:
                i+=1
                clicks.append([i,event.pos])
                
        screen.fill((30, 30, 30))
        pg.display.flip()
    pg.quit()
    return clicks

