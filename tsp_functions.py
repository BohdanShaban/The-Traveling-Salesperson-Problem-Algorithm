import itertools
import random


def select_rand_k ( unvisited, tour ) :

    print("select_rand_k()...")

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
          
    return (rand_k_city, unvisited , tour)


def nearest_dist ( max_dist, init_txt_lists, rand_k_city, tour ) :

    print("nearest_dist()...")

    min_dist = max_dist
    nearest_city = 0

    if len(tour) == 1 :
        print('nearest_dist for the 2-nd city...')

        for item in init_txt_lists :
            if item[0] == rand_k_city:
                print(item[2])
                if item[2] < min_dist:
                    min_dist = item[2]
                    nearest_city = item[1]

        print("min_dist: %s" % min_dist)
        print("nearest_city: %s" % nearest_city)

        return (nearest_city)

    print('nearest_dist for the 3,4, ... ,n city...')
    


    return (nearest_city)


def incertion_rand_k ( rand_k_city, tour, init_txt_lists, max_dist_in_txt ) :

    print("incertion_rand_k()...")

    if not tour or len(tour) == 1 :
        print('incertion_rand_k for the 1-st or 2-nd city...')

        tour.append(rand_k_city)
        print("tour: %s" % tour)

        return (tour)

    if not tour or len(tour) == 2 :
        print('incertion_rand_k for the 3-d city...')

        tour.insert(1, rand_k_city)
        print("tour: %s" % tour)

        return (tour)

    print('incertion_rand_k for the 4,5, ... , n city...')

    city_pairs = []
    list_cycle = itertools.cycle(tour)
    next(list_cycle)

    for city in tour:
        next_element = next(list_cycle)
        pair = []
        pair.append( city )
        pair.append( next_element )
        city_pairs.append( pair )

    city_pairs = city_pairs[:-1] # removes the last element
    print("city_pairs: %s" % city_pairs)

    # C[i,k] + C[k,j] - C[i,j] = MIN
    c_i_j = 0
    c_i_k = 0
    c_k_j = 0
    min_pair_dist = max_dist_in_txt
    min_pair_idx = None

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

    pair = city_pairs[min_pair_idx]
    print("pair: %s" % pair)

    pair.insert(1, rand_k_city)
    print("pair: %s" % pair)
    print("city_pairs: %s" % city_pairs)

    tour = list(itertools.chain(*city_pairs))
    tour = list(dict.fromkeys(tour))
    print("tour: %s" % tour)

          
    return (tour)


def tour_length ( tour, init_txt_lists ) :

    print("tour_length()...")
    length = 0

    list_cycle = itertools.cycle(tour)
    next(list_cycle)

    for city in tour:
        next_city = next(list_cycle)

        for item in init_txt_lists :

            if item[0] == city and item[1] == next_city :
                
                print("length: %s" % item[2])
                length = length + item[2]
        
   
          
    return (length)