'''
IMMC 2020

This Program stores the constants for
the simulation and the mathematical model.
'''

###########
# IMPORTS #
###########
from Department import Department

####################
# PYGAME CONSTANTS #
####################
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
FPS = 60
DIM = (SCREEN_WIDTH,SCREEN_HEIGHT)
WHITE =      (255, 255, 255, 255.0)
BLACK =      ( 23,  23,  23, 255.0)
RED =        (255,   0,   0, 127.5)
GREEN =      ( 61, 255,   0, 127.5)
ORANGE =     (255, 109,   0, 127.5)
AQUAMARINE = (  0, 255, 212, 127.5)
INDIGO =     (  0,  92, 255, 127.5)
PURPLE =     (100,   0, 255, 127.5)

# number of people - CHANGING VARIABLE
NUM_PEOPLE = 1500

max_damages = 0.1 # [1]

#################
# MODEL WEIGHTS #
#################

# Opening Package
w_1_OP = 0.2
w_2_OP = 0.1
w_3_OP = 0.7
w_OP = [w_1_OP, w_2_OP, w_3_OP]

# Rough Handling
w_1_RH = 0.7
w_2_RH = 0.3
w_RH = [w_1_RH, w_2_RH]

# Total Damage Score
w_1_T = 0.425
w_2_T = 0.425
w_3_T = 0.150
w_T = [w_1_T, w_2_T, w_3_T]

#############
# POSITIONS #
#############

# LAYOUT 1 POSITIONS (ORIGINAL)
# pos_appliances = (90, 380)
# pos_cam_aud_phones = (300,140)
# pos_computers_tablets = (250, 280)
# pos_tvhometheater_1 = (300, 430)
# pos_tvhometheater_2 = (450, 240)
# pos_video_gaming = (90, 190)
# pos_large_cashier = (210, 50)

# LAYOUT 2 POSITIONS (MODIFIED)

pos_appliances = (230, 480-215)
pos_cam_aud_phones = (95,	480-135)
pos_computers_tablets = (95,	480-295)
pos_tvhometheater_1 = (375,	480-115)
pos_tvhometheater_2 = (250, 480-50)
pos_video_gaming = (365,	480-290)
pos_cashier_1 = (197, 480-119)
pos_cashier_2 = (269, 480-119)
pos_cashier_3 = (62, 480-195)
pos_cashier_4 = (130, 480-195)
pos_cashier_5 = (344, 480-201)
pos_cashier_6 = (200, 480-310)
pos_cashier_7 = (270, 480-310)
pos_cashier_8 = (237, 480-369)

##############
# DIMENSIONS #
##############

# LAYOUT 1 DIMENSIONS (ORIGINAL)
# dim_appliances =      (120, 120)
# dim_cam_aud_phones =  ( 80,  40)
# dim_computers_tablets =  (117,  117)
# dim_tvhome_theater_1 = (120,  60)
# dim_tvhome_theater_2 = ( 60, 260)
# dim_video_gaming =    (102, 102)
# dim_large_cashier = (245, 80)
# dim_small_cashier = (60, 50)

# LAYOUT 2 DIMENSIONS (MODIFIED)
dim_appliances =      (120, 120)
dim_cam_aud_phones =  ( 80,  40)
dim_computers_tablets =  (117,  117)
dim_tvhome_theater_1 = (120,  60)
dim_tvhome_theater_2 = ( 260, 60)
dim_video_gaming =    (102, 102)
dim_large_cashier = (245, 80)
dim_small_cashier = (60, 50)

#########
# AREAS #
#########

# Areas of each department
area_appliances = 360
area_cam_aud_phones = 192
area_computers_tablets = 456
area_tvhometheater_1 = 264 # split TV department in two areas due to large num of products
area_tvhometheater_2 = 288 
area_video_gaming = 324
area_cashier = 196

# Display Areas of each department
area_appliances_disp = 144
area_cam_aud_phones_disp = 32.5
area_computers_tablets_disp = 138
area_tvhometheater_1_disp = 72.75
area_tvhometheater_2_disp = 156
area_video_gaming_disp = 104.25
area_tvhometheater_disp = area_tvhometheater_1_disp + area_tvhometheater_2_disp

##############
# QUANTITIES #
##############
dept_to_quantity = { "Appliances": 257,
                     "Cameras": 165,
                     "Audio": 50,
                     "Cell Phones": 55,
                     "Computers&Tablets": 444,
                     "TV&Home Theater": 383, 
                     "Video Gaming": 181 }

# Total quantity of products in each department
quantity_appliances = dept_to_quantity["Appliances"]
quantity_cam_aud_phones =  dept_to_quantity["Cameras"] + dept_to_quantity["Audio"] + dept_to_quantity["Cell Phones"]
quantity_computers_tablets = dept_to_quantity["Computers&Tablets"]
quantity_tvhometheater_1 = round ( dept_to_quantity["TV&Home Theater"] * (area_tvhometheater_1_disp / area_tvhometheater_disp) )
quantity_tvhometheater_2 = round ( dept_to_quantity["TV&Home Theater"] * (area_tvhometheater_2_disp / area_tvhometheater_disp) )
quantity_video_gaming = dept_to_quantity["Video Gaming"]

#################
# POPULARITY %s #
#################
# Dictionary that represents the percentage of people that will be at a department at a particular point in time.
# They are essentially normalized percentages based on popularity in each department.
p_norm = {  'Appliances': 10.87,
            'Audio': 18.29,
            'Cameras': 13.04,
            'Cell Phones': 15.38,
            'Computers&Tablets': 15.32,
            'TV&Home Theater': 11.13,
            'Video Gaming': 15.97 }

# Popularity percentages for each department/group
per_appliances = p_norm['Appliances'] / 100
per_cam_aud_phones = ( p_norm['Audio'] + p_norm['Cameras'] + p_norm['Cell Phones'] ) / 100
per_computers_tablets = p_norm['Computers&Tablets']  / 100
per_tv_home_theater_1 = p_norm['TV&Home Theater'] * (area_tvhometheater_1_disp / area_tvhometheater_disp) / 100
per_tv_home_theater_2 = p_norm['TV&Home Theater'] * (area_tvhometheater_2_disp / area_tvhometheater_disp)  / 100
per_video_gaming = p_norm['Video Gaming']  / 100

#############
# DEPT OBJS #
#############

appliances = Department(pos_appliances, dim_appliances, RED, "Appliances", quantity_appliances, area_appliances, area_appliances_disp, per_appliances)

cam_aud_phones = Department(pos_cam_aud_phones, dim_cam_aud_phones, INDIGO, "CamerasAudioPhones", quantity_cam_aud_phones, area_cam_aud_phones, area_cam_aud_phones_disp, per_cam_aud_phones)

computers_tablets = Department(pos_computers_tablets, dim_computers_tablets, AQUAMARINE, "Computers&Tablets", quantity_computers_tablets, area_computers_tablets, area_computers_tablets_disp, per_computers_tablets)

tvhome_theater_1 = Department(pos_tvhometheater_1, dim_tvhome_theater_1, ORANGE, "TV&Home Theater1", quantity_tvhometheater_1, area_tvhometheater_1, area_tvhometheater_1_disp, per_tv_home_theater_1)

tvhome_theater_2 = Department(pos_tvhometheater_2, dim_tvhome_theater_2, PURPLE, "TV&Home Theater2", quantity_tvhometheater_2, area_tvhometheater_2, area_tvhometheater_2_disp, per_tv_home_theater_2)

video_gaming = Department(pos_video_gaming, dim_video_gaming, GREEN, "Video Gaming", quantity_video_gaming, area_video_gaming, area_video_gaming_disp, per_video_gaming)

############
# CASHIERS #
############

# Cashiers, modeled by Department objects.

# CASHIERS FOR LAYOUT 1 (ORIGINAL)
# large_cashier = Department(pos_large_cashier, dim_large_cashier, BLACK, "Cashier", 0, area_cashier, 0, 0)
# cashiers = [large_cashier]

# CASHIERS FOR LAYOUT 2 (MODIFIED)
cashier1 = Department(pos_cashier_1, dim_small_cashier, BLACK, "Cashier", 0, area_cashier, 0, 0)

cashier2 = Department(pos_cashier_2, dim_small_cashier, BLACK, "Cashier", 0, area_cashier, 0, 0)

cashier3 = Department(pos_cashier_3, dim_small_cashier, BLACK, "Cashier", 0, area_cashier, 0, 0)

cashier4 = Department(pos_cashier_4, dim_small_cashier, BLACK, "Cashier", 0, area_cashier, 0, 0)

cashier5 = Department(pos_cashier_5, dim_small_cashier, BLACK, "Cashier", 0, area_cashier, 0, 0)

cashier6 = Department(pos_cashier_6, dim_small_cashier, BLACK, "Cashier", 0, area_cashier, 0, 0)

cashier7 = Department(pos_cashier_7, dim_small_cashier, BLACK, "Cashier", 0, area_cashier, 0, 0)

cashier8 = Department(pos_cashier_8, dim_small_cashier, BLACK, "Cashier", 0, area_cashier, 0, 0)

cashiers = [cashier1, cashier2, cashier3, cashier4, cashier5, cashier6, cashier7, cashier8]

# department objects stored in list for use in main file
departments = [appliances, cam_aud_phones, computers_tablets, tvhome_theater_1, tvhome_theater_2, video_gaming]

max_people_per_product = NUM_PEOPLE / sum(dept_to_quantity.values()) # [2]

##############
# References #
##############
'''
1. The inventory shrinkage for unkown damages to items is projected to be 7-10% by https://www.shopkeep.com/blog/what-causes-retail-shrinkage#step-1.
2. The maximum capacity of a large retail store such as Lowes is about 500 people, and the total number of objects is approximately 1500. Thus, the maximum people per product ratio is approximately 0.33. https://www.reddit.com/r/Lowes/comments/fv2184/what_is_the_maximum_occupancy_of_a_typical_lowes/
'''
