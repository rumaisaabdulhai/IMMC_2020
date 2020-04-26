'''
IMMC 2020

This program contains the basic formulas
used in calculating the damage score.
'''

###########
# IMPORTS #
###########
import numpy as np

def people_per_product_metric(pop_density, prod_density, max_ratio):
    return pop_density / (prod_density * max_ratio)

def population_density(num_people, pop_perc, free_dept_area):
    return (num_people * pop_perc) / free_dept_area

def product_density(num_products, display_area):
    return num_products / display_area

def obstruction(cashier_pos, dep_pos, pop_per, max_dist = (2*(480**2))**0.5):
    '''
    A Gaussian function with average change in decrease as a function of the popularity percentage.
    '''

    dist = ((cashier_pos.distance(dep_pos))/(max_dist))
    # return np.e ** (-1 * (pop_per) * (dist ** 2))
    return dist
    

def model_obstructions(obstructions, sub_constant = 0.1):
  '''
  Calculates the final obstruction score based on the
  individual obstruction scores for each cashier.
  '''
  if len(obstructions) == 1:
    return obstructions[0]
  else:
    avg = sum(obstructions)/len(obstructions)
    obstructions.remove(max(obstructions))

    sub = 0
    for o in obstructions:
      sub += sub_constant * o
    
    return avg - sub

#########
# POINT #
#########
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point2):
        return ((self.y - point2.y) ** 2 + (self.x - point2.x) ** 2) ** 0.5
