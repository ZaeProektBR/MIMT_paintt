width, height = 11, 11
a, b = 5, 5
r = 5
EPSILON = 2.2

map_ = [[' ' for x in range(width)] for y in range(height)]

for y in range(height):
    for x in range(width):
        if abs((x-a)**2 + (y-b)**2 - r**2) < EPSILON**2:
            map_[y][x] = '#'

# print the map
for line in map_:
    print (' '.join(line))
