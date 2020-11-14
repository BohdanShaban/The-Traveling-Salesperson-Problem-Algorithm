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

tour = incertion_rand_k( rand_k_city, tour )

# !!!!! FIND THE NEAREST DISTANCE !!!!!
print("!!!!! FIND THE NEAREST DISTANCE !!!!!")

max_dist_in_txt = max(distances)

nearest_city = nearest_dist( max_dist_in_txt , init_txt_lists, rand_k_city, tour )

# !!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!
print("!!!!! INCERTION OF RANDOM K TO THE TOUR !!!!!")

tour = incertion_rand_k( nearest_city, tour )

# !!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!
print("!!!!! SELECT rand_k_city && DELATE FORM unvisited !!!!!")

unvisit_cities = copy.deepcopy(cities)
init_tour = []

rand_k_city, unvisited, tour = select_rand_k( unvisit_cities, init_tour )








# INCERTION OF k TO THE TOUR (in the middle) && remove rand_k_city from unvisited
print("INCERTION OF k TO THE TOUR (in the middle) && remove rand_k_city from unvisited ...")

tour.insert(1, rand_k_city)
print("tour: %s" % tour)
unvisited.remove(rand_k_city)
print("unvisited after remove rand_k_city: %s" % unvisited )


# SELECT UNVISITED RAND K
print("SELECT UNVISITED RAND K...")

for i in unvisited :
    for j in tour :
        if i == j :
            unvisited.remove(i)

print("unvisited: %s" % unvisited)
print("tour: %s" % tour)
rand_k_city = random.choice(unvisited)
print("rand_k_city: %s" % rand_k_city)
unvisited.remove(rand_k_city)
print("unvisited after remove rand_k_city: %s" % unvisited )

city_pairs = []

# !!!!! INCERTION OF k TO THE TOUR (on unknown place) !!!!!
print("INCERTION OF k TO THE TOUR (on unknown place)...")

# FIND THE SMALLEST DISTANCE (for 3,4, ... , n city)
print("FIND THE SMALLEST DISTANCE (for 3,4, ... , n city)...")

# divide the tour on pairs
print("divide the tour on pairs...")

list_cycle = itertools.cycle(tour)
next(list_cycle)

for city in tour:
    next_element = next(list_cycle)

    pair = []
    # print("city: %s" % city)
    # print("next_element: %s" % next_element)

    pair.append( city )
    pair.append( next_element )
    # print("pair: %s" % pair)

    city_pairs.append( pair)
    # print("city_pairs: %s" % city_pairs)

city_pairs = city_pairs[:-1] # removes the last element
print("city_pairs: %s" % city_pairs)


# FIND THE SMALLEST DISTANCE (for 3,4, ... , n city)
print("FIND THE SMALLEST DISTANCE (for 3,4, ... , n city)...")

print("rand_k_city: %s" % rand_k_city)

# C[i,k] + C[k,j] - C[i,j] = MIN
c_i_j = 0
c_i_k = 0
c_k_j = 0
min_pair_dist = max_dist_in_txt
min_pair_idx = None

#for pair in city_pairs :
for index, pair in enumerate(city_pairs):

    print("pair: %s" % pair) # DEBUG !!!

    for item in init_txt_lists :

        #C[i,j]
        if item[0] == pair[0] and item[1] == pair[1] :
            c_i_j = item[2]
            print("c_i_j: %s" % c_i_j)

        #C[i,k]
        if item[0] == pair[0] and item[1] == rand_k_city :
            c_i_k = item[2]
            print("c_i_k: %s" % c_i_k)

        #C[k,j]
        if item[0] == rand_k_city and item[1] == pair[1] :
            c_k_j = item[2]
            print("c_k_j: %s" % c_k_j)

    sum_dist = c_i_k + c_k_j - c_i_j
    print("sum_dist of pair: %s" % sum_dist)

    if sum_dist < min_pair_dist : 
        min_pair_dist = sum_dist 
        min_pair_idx = index 
        print("min_pair_dist: %s" % min_pair_dist)
        print("min_pair_idx: %s" % min_pair_idx)


# INCERTION OF k TO THE TOUR (on unknown place)
print("INCERTION OF k TO THE TOUR (on unknown place)...")

# incertion of the rand_k_city to the pair with min_pair_idx
print("incertion of the rand_k_city to the pair with min_pair_idx...")  

pair = city_pairs[min_pair_idx]
print("pair: %s" % pair)

pair.insert(1, rand_k_city)
print("pair: %s" % pair)
print("city_pairs: %s" % city_pairs)

# transform the city_pairs into tour && upd the tour
print("transform the city_pairs into tour && upd the tour...")  

tour = list(itertools.chain(*city_pairs))
tour = list(dict.fromkeys(tour))
print("tour: %s" % tour)

# SELECT UNVISITED RAND K
print("SELECT UNVISITED RAND K...")

for i in unvisited :
    for j in tour :
        if i == j :
            unvisited.remove(i)

print("unvisited: %s" % unvisited)
print("tour: %s" % tour)
rand_k_city = random.choice(unvisited)
print("rand_k_city: %s" % rand_k_city)
unvisited.remove(rand_k_city)
print("unvisited after remove rand_k_city: %s" % unvisited )


