import random
import copy
import itertools

from data_reading import read_data 
from data_reading import write_to_file 
from tsp_functions import select_rand_k
from tsp_functions import nearest_dist
from tsp_functions import incertion_rand_k
from tsp_functions import tour_length


# !!!!! DATA READING && PREPARE !!!!!
print("!!!!! DATA READING && PREPARE !!!!!")

inputFile = 'input.txt'
outputFile = 'output.txt'

init_txt_lists, distances, cities = read_data(inputFile)

max_dist_in_txt = max(distances)

# !!!!! MAIN LOOP !!!!! 

tour = []
total_length = 0
unvisit_cities = copy.deepcopy(cities)

for index, city in enumerate(cities):

    if index == 1 :

        nearest_city = nearest_dist( max_dist_in_txt , init_txt_lists, rand_k_city, tour )
        tour = incertion_rand_k( nearest_city, tour, init_txt_lists, max_dist_in_txt )
        continue


    rand_k_city, unvisited, tour = select_rand_k( unvisit_cities, tour )
    tour = incertion_rand_k( rand_k_city, tour, init_txt_lists, max_dist_in_txt )


total_length = tour_length( tour, init_txt_lists )
print("total_length: %s" % total_length)

write_to_file( outputFile, total_length, tour)