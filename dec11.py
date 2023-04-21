import numpy as np

with open('dec11-input.txt') as f:
    data = f.readlines()

#data = [list(x.strip()) for x in data]
monkeys = []
monkey = []
for row in data:
    if row=='\n':
        monkeys.append(monkey)
        monkey = []
    else:
        monkey.append(row.strip())
#print(monkeys[0])
names = []
items = []
opers = []
numbers = []
divers = []
true_throws = []
false_throws = []
for monkey in monkeys:
    names.append(monkey[0])
    items.append(monkey[1].split(':')[1].replace(' ', '').split(','))
    [oper, number] = monkey[2].split(':')[1].split('old ')[1].split(' ')
    opers.append(oper)
    numbers.append(number)
    divers.append(monkey[3].split(' ')[-1])
    true_throws.append(monkey[4].split(' ')[-1])
    false_throws.append(monkey[5].split(' ')[-1])


nr_monkeys = len(monkeys)
for i in range(nr_monkeys):
    for j in range(len(items[i])):
        print(f'{names[i]} has {items[i][j]}')
        # inpection, perfrom oper
        item = items[i].pop(0)
        if opers[i]=='+':
            item = int(item) + int(numbers[i])
        elif opers[i]=='*':
            item = int(item) * int(numbers[i])
        else:
            print('Unknown operator')
        # devide by 3
        item = int( item / 3 )
        # check diversible by divers
        if item % int(divers[i]) == 0:
            # do true throw
            print('throw to (true)', true_throws[i])
            to = true_throws[i]
            items[to].append(item)
            print('items', items[to])
        else:
            # do false throw
            print('throw to', false_throws[i])


    break

print(items)