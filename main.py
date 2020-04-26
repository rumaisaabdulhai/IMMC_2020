'''
IMMC 2020

This program runs the simulation and calculates
the number of products damaged.
'''

###########
# IMPORTS #
###########
import pygame as pg
import information as i
from Department import Department
from calculate_score import get_score

def main():

    # initializes pygame
    pg.init()
    Screen = pg.display.set_mode(i.DIM)
    pg.display.set_caption("IMMC Simulator")
    clock = pg.time.Clock()
    running = True

    # add cashier to departments
    deps = i.departments.copy()

    for r in i.cashiers:
      deps.append(r)
    get_score()

    # while the program is running
    while running:

        # Events
        for event in pg.event.get():

            # if the program is quit, stop loop
            if event.type == pg.QUIT:
                running = False

            # if the mouse is down
            elif event.type == pg.MOUSEBUTTONDOWN: # [1]
                if event.button == 1:
                    for dep in deps:     
                        if dep.get_rect().collidepoint(event.pos):
                            dep.set_clicked(True)
                            offset_x = dep.get_rect().x - event.pos[0]
                            offset_y = dep.get_rect().y - event.pos[1]

            # if the mouse is not down
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    for dep in deps:      
                        dep.set_clicked(False)

            # if the mouse is moving and clicked is true, move dept
            elif event.type == pg.MOUSEMOTION:
                for dep in deps:
                    if dep.get_clicked():
                        dep.get_rect().x = event.pos[0] + offset_x
                        dep.get_rect().y = event.pos[1] + offset_y
                        dep.set_pos(dep.get_rect().center)

                        # makes sure depts do not go out of bounds
                        if dep.get_rect().right > i.SCREEN_WIDTH:
                            dep.get_rect().right = i.SCREEN_WIDTH
                        if  dep.get_rect().left < 0:
                                dep.get_rect().left = 0
                        if  dep.get_rect().bottom > i.SCREEN_HEIGHT:
                                dep.get_rect().bottom = i.SCREEN_HEIGHT
                        if  dep.get_rect().top < 0:
                                dep.get_rect().top = 0
                        
                        # gets the damage score
                        get_score()
                        print(dep.get_rect().center)

            # update the screen
            Screen.fill(i.WHITE)
            for dep in deps:
                pg.draw.rect(Screen, dep.get_color(), dep.get_rect())
            pg.display.flip()
            clock.tick(i.FPS)

    pg.quit()

if __name__ == "__main__":
    main()

##############
# REFERENCES #
##############
'''
1. How to drag an object with Pygame: https://blog.furas.pl/python-pygame-drag-object-on-screen-using-mouse-gb.html 
'''
