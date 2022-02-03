# The base to selection sort is finding the lowest number in list and put it as fist, then look for the second lowest
# And put it on the second place, and so on


# Number list
numList = [5, 9, 6, 7, 12, 11, 4, 2, 3, 8, 9, 1, 10, 13, 15]


# function
def selection(list):
    # Creating an index, and variable to control the inner loop
    index2 = range(len(list) - 1)
    contr = 0
    # this loop will pass through the entire list, one by one to define the minumum number
    for i in range(len(list) - 1):
        # this loop will just compare the positions are not completely defined yet
        for item in index2[contr:len(list)]:
            # comparing numbers them changing then
            if list[i] > list[item]:
                list[i], list[item] = list[item], list[i]
        contr = contr + 1

    return list


ordenList = selection(numList)

print(ordenList)
