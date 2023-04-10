import numpy as np

with open('dec9-input.txt') as f:
    data = f.readlines()

data = [x.strip().split(' ') for x in data]


test_data = True
# testa data
if test_data:
    data = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20'
    ]
    data = [x.split(' ') for x in data]
    print(data[:3])


def vizulize(rope, grid_size):
    grid = np.zeros((grid_size,grid_size), dtype=int)
    for i in range(len(rope)):
        grid[rope[i]] = i+10
    print(grid)

move_def = np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ])
def check_t(pos_h, pos_t):
    #x, y = pos_t
    x = pos_h[0]-pos_t[0]
    y = pos_h[1]-pos_t[1]
    #a = np.zeros((3,3), dtype=int)
    move_def[x+1,y+1] = 1  # tail is 1,1
    print(move_def)
    return
    #print('check_t', pos_h, pos_t)
    if (x-1)<=pos_t[0] and pos_t[0]<=(x+1) and (y-1)<=pos_t[1] and pos_t[1]<=(y+1):
        return 'F' # no move
    # upper left corner
    elif (x-1)>pos_t[0] and (y-1)>pos_t[1]:
        return 'UL'
    # upper right corner
    elif (x-1)>pos_t[0] and (y+1)<pos_t[1]:
        return 'UR'
    # lower left corner
    elif (x+1)<pos_t[0] and (y-1)>pos_t[1]:
        return 'LL'
    # lower right corner
    elif (x+1)<pos_t[0] and (y+1)<pos_t[1]:
        return 'LR'
    else:
        return 'T' # just follow the prev rope

#def move_tail(pos_h, old_h, pos_t):


def move(rope, dir):
    pos_h = rope[0]
    #pos_t = rope[1]
    old_rope = rope.copy()
    if dir=='U':
        pos_h = (pos_h[0]-1, pos_h[1])
    elif dir=='D':
        pos_h = (pos_h[0]+1, pos_h[1])
    elif dir=='L':
        pos_h = (pos_h[0], pos_h[1]-1)
    elif dir=='R':
        pos_h = (pos_h[0], pos_h[1]+1)
    rope[0] = pos_h

    for i in range(len(rope))[1:]:
        #print('rope', i)
        pos_h = rope[i-1]
        pos_t = rope[i]
        #print(pos_h, pos_t)
        #print(check_t(pos_h, pos_t))
        check = check_t(pos_h, pos_t)
        if check=='T': # Follow the old rope.
            rope[i] = old_rope[i-1]
        elif check =='UL':
            rope[i] = (pos_t[0]-1, pos_t[1]-1)
        elif check =='UR':
            rope[i] = (pos_t[0]-1, pos_t[1]+1)
        elif check =='LL':
            rope[i] = (pos_t[0]+1, pos_t[1]-1)
        elif check =='LR':
            rope[i] = (pos_t[0]+1, pos_t[1]+1)


    # Update final tail history
    d_t_hist[rope[-1]] = 1

    return rope

grid_size = 30
start = (int(grid_size/2), int(grid_size/2))
rope_length = 10
rope = [start for _ in range(rope_length)]
#pos_h = start
#pos_t = starts
d_t_hist = {}

check_t((2,3), (2,2))
exit()
j = 0
for dir, nr in data:
    print(dir, nr)
    for i in range(int(nr)):
        rope = move(rope, dir)
    print(rope)
    vizulize(rope, grid_size)
    
    if j==1:
        break
    j += 1
    
    
#print(rope)
print('---')
print('Nr pos for t:', len(d_t_hist))
print(d_t_hist)
