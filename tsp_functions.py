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


def incertion_rand_k ( rand_k_city, tour ) :

    print("incertion_rand_k()...")

    if not tour or len(tour) == 1 :
        print('incertion_rand_k for the 1-st or 2-nd city...')

        tour.append(rand_k_city)
        print("tour: %s" % tour)

        return (tour)

          
    return (tour)