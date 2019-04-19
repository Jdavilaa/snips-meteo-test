import random

BUFFER_SIZE = 64 * 1024 * 1024
all_cities = []
with open('../resources/sorted_cities.txt', 'rb', BUFFER_SIZE) as orig:
    for line in orig:
        all_cities.append( line.strip() )
with open('../resources/filtered_cities.txt', 'wb', BUFFER_SIZE) as filt:
    n = 0
    while n < 49999:
        sel = random.choice(all_cities)
        filt.write('{}\n'.format(sel))
        n += 1
