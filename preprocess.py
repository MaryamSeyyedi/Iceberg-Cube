
file = open('Dataset.txt', 'r')
output = open('output.csv', 'w')
while True:
    cell = ['!a', '!b', '!c', '!d', '!e']
    line = file.readline()
    if not line:
        break
    items = line.split()
    if '0' in items or '1' in items or '2' in items or '3' in items:
        cell[0] = 'a'
    if '4' in items or '5' in items or '6' in items or '7' in items:
        cell[1] = 'b'
    if '8' in items or '9' in items or '10' in items or '11' in items:
        cell[2] = 'c'
    if '12' in items or '13' in items or '14' in items or '15' in items:
        cell[3] = 'd'
    if '16' in items or '17' in items or '18' in items or '19' in items:
        cell[4] = 'e'
    output.write(','.join(cell) + '\n')

file.close()
output.close()
