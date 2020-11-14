import random
import copy
import itertools

from data_reading import read_data 
from tsp_functions import select_rand_k
from tsp_functions import nearest_dist
from tsp_functions import incertion_rand_k


# !!!!! DATA READING && PREPARE !!!!!
print("!!!!! DATA READING && PREPARE !!!!!")

fileName = 'input.txt'

init_txt_lists, distances, cities = read_data(fileName)

max_dist_in_txt = max(distances)

# !!!!! MAIN FOR LOOP !!!!! 

tour = []
unvisit_cities = copy.deepcopy(cities)

for index, city in enumerate(cities):

    if index == 1 :

        nearest_city = nearest_dist( max_dist_in_txt , init_txt_lists, rand_k_city, tour )
        tour = incertion_rand_k( nearest_city, tour, init_txt_lists, max_dist_in_txt )
        continue


    rand_k_city, unvisited, tour = select_rand_k( unvisit_cities, tour )
    tour = incertion_rand_k( rand_k_city, tour, init_txt_lists, max_dist_in_txt )







# !!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!
print("!!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!")

rand_k_city, unvisited, tour = select_rand_k( unvisit_cities, tour )

# !!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!
print("!!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!")

tour = incertion_rand_k( rand_k_city, tour, init_txt_lists, max_dist_in_txt )

# !!!!! FIND THE NEAREST DISTANCE !!!!!
print("!!!!! FIND THE NEAREST DISTANCE !!!!!")

nearest_city = nearest_dist( max_dist_in_txt , init_txt_lists, rand_k_city, tour )

# !!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!
print("!!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!")

tour = incertion_rand_k( nearest_city, tour, init_txt_lists, max_dist_in_txt )

# !!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!
print("!!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!")

rand_k_city, unvisited, tour = select_rand_k( unvisit_cities, tour )

# !!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!
print("!!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!")

tour = incertion_rand_k( rand_k_city, tour, init_txt_lists, max_dist_in_txt )

# !!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!
print("!!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!")

rand_k_city, unvisited, tour = select_rand_k( unvisit_cities, tour )

# !!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!
print("!!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!")

tour = incertion_rand_k( rand_k_city, tour, init_txt_lists, max_dist_in_txt )

# !!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!
print("!!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!")

rand_k_city, unvisited, tour = select_rand_k( unvisit_cities, tour )

# !!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!
print("!!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!")

tour = incertion_rand_k( rand_k_city, tour, init_txt_lists, max_dist_in_txt )

# !!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!
print("!!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!")

rand_k_city, unvisited, tour = select_rand_k( unvisit_cities, tour )

# !!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!
print("!!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!")

tour = incertion_rand_k( rand_k_city, tour, init_txt_lists, max_dist_in_txt )








