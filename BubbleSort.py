# BubleSort Algorithim, mean comparing every number in a list, to the number ahead, if it's bigger change their
# posicioning

# number list
numList = [7, 15, 5, 2, 8, 12, 9, 4, 4, 2, 10, 3, 2, 1, 6, 13]


# function
def Bubble(list):
    # Defining the range of the list
    index = len(list)
    # Creating the control tie
    goon = True
    # Autorepeat while not ready
    while goon:
        # A counter to know if there are no changes to do, then close de loop
        c = 0
        for i in range(index - 1):
            # Properly changing the positioning
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
            else:
                # If there is no change to do, counter++ :)
                c = c + 1
        # A simple if/else to control de repetition
        if c < index - 1:
            goon = True
        else:
            goon = False
    # Returning the list
    return list


newList = Bubble(numList)

print(newList)
