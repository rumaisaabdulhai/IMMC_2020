'''
IMMC 2020

This Program models a store Department 
using the Excel spreadsheet and Pygame.
'''

###########
# IMPORTS #
###########
import pygame as pg
import information as i
import utils
from utils import Point

class Department():
    '''
    A Store Department that is modeled by a rectangle.
    '''

    def __init__(self, pos, dim, color, dept, quantity, dept_area, disp_area, pop_per):
        '''
        Constructor for the Department class.

        Parameters:
        -----------
        self: The Department object.\n
        pos (tuple): The coordinates of the center of the Department.\n
        dim (tuple): The dimensions of the Department in pixels.\n
        color (tuple): The RGB color of the Department.\n
        dept (str): The name of the Department.\n
        quantity (int): The total quantity of products in the Department.\n
        dept_area (float): The total area of the Department (m^2)\n
        disp_area (float): The display area of the Department (m^2)\n
        pop_per (float): The popularity percentage of the Department.
        '''

        self._pos = pos
        self._dim = dim
        self._color = color
        self._rect = self.make_rect()
        
        self._dept = dept
        self._quantity = quantity
        self._dept_area = dept_area
        self._disp_area = disp_area
        self._pop_per = pop_per

        self._clicked = False
    
    def make_rect(self):
        '''
        Makes the rectangle.

        Parameters:
        -----------
        self: The Department object.
        '''

        # x coordinate of the left side of the rect; x - (l/2)
        left = self._pos[0] - (self._dim[0]/2)

        # y coordinate of the top side of the rect; y + (w/2)
        top = i.SCREEN_HEIGHT - ( self._pos[1] + (self._dim[1]/2) )

        rect = (left, top, self._dim[0], self._dim[1])

        return pg.Rect(rect)

    def get_pos(self):
        '''
        Returns the center position of the Department depect.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._pos
    
    def set_pos(self, new_pos):
        '''
        Sets the pos.

        Parameters:
        -----------
        self: The Department object.
        '''
        self._pos = new_pos

    def get_dim(self):
        '''
        Returns the dimensions of the Department depect.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._dim

    def get_color(self):
        '''
        Returns the color of the Department object.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._color
    
    def get_rect(self):
        '''
        Returns the rectangle of the Department object.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._rect
    
    def get_dept(self):
        '''
        Returns the name of the Department object.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._dept
    
    def get_quantity(self):
        '''
        Returns the quantity of the Department object.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._quantity
    
    def get_dept_area(self):
        '''
        Returns the total area of the Department object.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._dept_area
    
    def get_disp_area(self):
        '''
        Returns the display area of the Department object.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._disp_area
    
    def get_pop_per(self):
        '''
        Returns the popularity percentage of the Department object.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._pop_per

    def get_clicked(self):
        '''
        Returns if the Department object has been clicked.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._clicked
    
    def get_num_people(self):
        '''
        Returns the number of people at the Department.

        Parameters:
        -----------
        self: The Department object.
        '''
        return self._pop_per * i.NUM_PEOPLE

    def set_clicked(self, clicked):
        '''
        Sets whether the Department object has been clicked.

        Parameters:
        -----------
        self: The Department object.
        '''
        self._clicked = clicked

    def get_pop_density(self):
        '''
        Calculates the population density.

        Parameters:
        -----------
        self: The Department object.
        '''
        return utils.population_density(i.NUM_PEOPLE, self._pop_per, self._dept_area - self._disp_area)

    def get_prod_density(self):
        '''
        Calculates the product density.

        Parameters:
        -----------
        self: The Department object.
        '''
        return utils.product_density(self._quantity, self._disp_area)

    def dropping(self):
        '''
        Calculates the dropping score from the people to product ratio.

        Parameters:
        -----------
        self: The Department object.
        '''
        return utils.people_per_product_metric(self.get_pop_density(), self.get_prod_density(), i.max_people_per_product)

    def rough_handling(self):
        '''
        Calculates the rough handling score as a function of 
        obstruction of the department and the people to product
        ratio in the department.

        Parameters:
        -----------
        self: The Department object.
        '''
        ppp = utils.people_per_product_metric(self.get_pop_density(), self.get_prod_density(), i.max_people_per_product)

        vises = []
        for c in i.cashiers: 
          vis = utils.obstruction(Point(c.get_pos()[0], c.get_pos()[1]), Point(self._pos[0], self._pos[1]), self._pop_per)

          vises.append(vis)

        vis_ = utils.model_obstructions(vises)

        return i.w_1_RH * ppp + i.w_2_RH * vis_

    def open_packaging(self):
        '''
        Calculates the open packaging score as a function of obstruction of the department, 
        the popularity score, and the people to product ratio in the department.

        Parameters:
        -----------
        self: The Department object.
        '''
        ppp = utils.people_per_product_metric(self.get_pop_density(), self.get_prod_density(), i.max_people_per_product)

        vises = []
        for c in i.cashiers: 
          vis = utils.obstruction(Point(c.get_pos()[0], c.get_pos()[1]), Point(self._pos[0], self._pos[1]), self._pop_per)

          vises.append(vis)
        vis_ = utils.model_obstructions(vises)

        return i.w_1_OP * ppp + i.w_2_OP * self._pop_per + i.w_3_OP * vis_
