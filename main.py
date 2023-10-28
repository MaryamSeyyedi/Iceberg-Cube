import csv
import copy


def create_cuboids():
    cuboids = {}

    vocab = [
        ['a', '!a'],
        ['b', '!b'],
        ['c', '!c'],
        ['d', '!d'],
        ['e', '!e'],
    ]

    def recursion(current, cuboid, position, dim):
        if len(current) == dim:
            if cuboid in cuboids:
                cuboids[cuboid].append(current)
            else:
                cuboids[cuboid] = [current]

            return
        for pos in range(position, 5):
            temp1 = copy.deepcopy(current)
            temp2 = copy.deepcopy(current)
            temp1.append(vocab[pos][0])
            recursion(temp1, cuboid + vocab[pos][0], pos + 1, dim)
            temp2.append(vocab[pos][1])
            recursion(temp2, cuboid + vocab[pos][0], pos + 1, dim)

    for dim in range(1, 6):
        recursion([], '', 0, dim)

    return cuboids


min_sup = 10000  # Minimum support
output = {}  # Output result


def load_data(file_name):
    data_output = []
    with open(file_name, "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data_output.append(row)

    return data_output


def contain(a, b):
    flag = True
    for item in b:
        if item not in a:
            flag = False
            break

    return flag


def get_count(cell, data_set):
    count = 0
    for data in data_set:
        if contain(data, cell):
            count = count + 1

    return count


def buc():
    print("Apex")
    print([], ": ", len(buc_data_set))
    cuboids = create_cuboids()
    for cuboid, cells in cuboids.items():
        print(cuboid)
        for cell in cells:
            count = get_count(cell, buc_data_set)
            if count > min_sup:
                print(cell, ": ", count)


buc_data_set = load_data("output.csv")

buc_output = buc()
