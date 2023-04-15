with open('dec10-input.txt') as f:
    data = f.read().splitlines()

data = [x.split(' ') for x in data]

x = 1
cycle_x = []
for i, row in enumerate(data):
    operation = data[i][0]
    if operation == 'noop':
        cycle_x.append(x)
        # takes one cycle to finish
    elif operation == 'addx':
        number = int(data[i][1])
        cycle_x.append(x)
        # takes 2 cycles to finish
        cycle_x.append(x)
        # x change after 2 cycles
        x += number

#print(cycle_x)

find = [20, 60, 100, 140, 180, 220]

s = 0
for c in find:
    #print(cycle_x[c-1])
    s += cycle_x[c-1] * c

print('A result:', s)


## B
img_row = ''
row = 0
for i in range(240):
    if cycle_x[i]-1 <= i-row and i-row <= cycle_x[i]+1:
        img_row += '#'
    else:
        img_row += '.'
    if i-row == 39:
        print(img_row)
        img_row = ''
        row += 40
print(img_row)

####. ###.. .##.. ###.. ####. ###.. .##.. ..##. .
####. ###.. .##.. ###.. ####. ###.. .##.. ..##