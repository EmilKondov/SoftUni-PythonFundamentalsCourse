size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
coordinates = ((int(x) for x in c.split(",")) for c in input().split())


directions = (
    (-1, 0), #up
    (1, 0),  #down
    (0, -1), #left
    (0, 1),  #right
    (-1, 1),#top right
    (-1, -1),#top left
    (1, -1), # bottom left
    (1, 1), # bottom right
    (0, 0) #current
)


