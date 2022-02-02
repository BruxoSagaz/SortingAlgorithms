# pick an element in list (Pivot)
# pass through the right of the Pivot every element bigger then it
# pass through the left of the Pivot every element smaller then it

# Number list (Size can be changeble)
numD = [4, 7, 2, 6, 4, 1, 8, 3]

# function
def ordenate(list, begin=0, end=None):
    # Defining an index to the end of the list
    if end is None:
        end = len(list) - 1
    # Doing the partiticion an calling the ordenate function again
    if begin < end:
        posi = partiticion(list, begin, end)
        ordenate(list, begin, posi - 1)
        ordenate(list, posi + 1, end)

# doing the partiticion and moving the numbers
def partiticion(list, begin, end):
    # Determing the Pivot
    pivot = list[end]
    # Defining the control Varieble
    i = begin
    # exchanging the numbers
    for j in range(begin, end):
        if list[j] <= pivot:
            list[j], list[i] = list[i], list[j]
            i = i + 1
    list[i], list[end] = list[end], list[i]

    return i


print(numD)
ordenate(numD)
print(numD)

