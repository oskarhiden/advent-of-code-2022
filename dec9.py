import numpy as np

with open('dec9-input.txt') as f:
    data = f.readlines()

data = [x.strip().split(' ') for x in data]
#print(data[:3])


# testa data
"""
data = [
'R 4',
'U 4',
'L 3',
'D 1',
'R 4',
'D 1',
'L 5',
'R 2'
]
data = [x.split(' ') for x in data]
#print(data[:3])
"""

def vizulize(pos_h, pos_t, grid_size):
    grid = np.zeros((grid_size,grid_size), dtype=int)
    grid[pos_t[0], pos_t[1]] = 2
    grid[pos_h[0], pos_h[1]] = 1
    print(grid)

 
grid_size = 20
start = (5,5)
pos_h = start
pos_t = start
d_t_hist = {}


def check_t(pos_h, pos_t):
    x, y = pos_h
    if (x-1)<=pos_t[0] and pos_t[0]<=(x+1) and (y-1)<=pos_t[1] and pos_t[1]<=(y+1):
        return False
    else:
        return True

def move(pos_h, pos_t, dir):
    old_h = pos_h
    if dir=='U':
        pos_h = (pos_h[0]-1, pos_h[1])
    elif dir=='D':
        pos_h = (pos_h[0]+1, pos_h[1])
    elif dir=='L':
        pos_h = (pos_h[0], pos_h[1]-1)
    elif dir=='R':
        pos_h = (pos_h[0], pos_h[1]+1)


    if check_t(pos_h, pos_t):
        pos_t = old_h

    # Update t hist
    d_t_hist[pos_t] = 1

    return pos_h, pos_t


for dir, nr in data:
    #print(dir, nr)
    for i in range(int(nr)):
        pos_h, pos_t = move(pos_h, pos_t, dir)
    

print('Nr pos for t:', len(d_t_hist))
