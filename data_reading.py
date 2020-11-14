import itertools


def read_data( filename) :

    print("read_data()...")

    init_txt_lists = []
    distances = []
    cities = []

    with open(filename) as f:
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split()]

            if inner_list[0] not in cities :
                cities.append(inner_list[0])

            distances.append(inner_list[2])

            init_txt_lists.append(inner_list)

    f.close()

    # print("list_of_lists: %s" % init_txt_lists)
    # print("distances: %s" % distances)
    # print("cities: %s" % cities)
          
    return (init_txt_lists, distances, cities)

def write_to_file( filename, length, tour ) :

    print("write_to_file()...")

    with open( filename, 'w') as f:

        f.write("%s\n" % length)
        
        for item in tour:
            f.write("%s," % item)
