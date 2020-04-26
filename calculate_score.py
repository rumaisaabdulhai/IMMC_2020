'''
IMMC 2020

This program calculates the damage score.
'''

###########
# IMPORTS #
###########
import information as i
from Department import Department
import utils
from utils import Point

def get_score():
  
  scores = []

  for dep in i.departments:
    # print("DEPARTMENT: " + str(dep.get_dept()))

    dept_score = total_score(dep)
    scores.append((dept_score/3) * i.max_damages)

    # print("TOTAL SCORE (0-3): " + str(dept_score))
    # print("PERCENT PRODUCTS DAMAGED: " + str((dept_score/3)*i.max_damages))
    # print("\n\n")

  sum_damaged = 0
  for j, score in enumerate(scores):
    products_damaged = i.departments[j].get_quantity() * score
    sum_damaged += products_damaged

    # print("DEPARTMENT: " + str(dep.get_dept()))
    # print("PRODUCTS DAMAGED: " + str(products_damaged) + "\n")

  print("TOTAL PRODUCTS DAMAGED: " + str(sum_damaged))

# GIVENS:: population density and product density
def total_score(dep):

    dropping = dep.dropping()
    rough_handling = dep.rough_handling()
    open_packages = dep.open_packaging()

    # print("--------------------------")
    # print("DROPPING SCORE:: ", dropping)
    # print("ROUGH HANDLING SCORE:: ", rough_handling)
    # print("OPENING PACKAGING SCORE:: ", open_packages)
    # print("--------------------------")

    # damage score
    return i.w_1_T * dropping + i.w_2_T * rough_handling + i.w_3_T * open_packages
