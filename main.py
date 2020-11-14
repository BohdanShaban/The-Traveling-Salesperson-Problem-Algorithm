print ("Shaban Bohdan TSP: Nearest Incertion of Arbitrary City")
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

# print("list_of_lists: %s" % init_txt_lists)
# print("distances: %s" % distances)
# print("cities: %s" % cities)

# !!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!
print("!!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!")

unvisit_cities = copy.deepcopy(cities)
init_tour = []

rand_k_city, unvisited, tour = select_rand_k( unvisit_cities, init_tour )

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

# ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR

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








