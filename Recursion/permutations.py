def getPermutations(array):
    # Write your code here.
    permutations = []
    getPermutationsHelper(0, array, permutations)
    return permutations

def getPermutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            # print(array)
            print(i, j)
            getPermutationsHelper(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


getPermutations([1,2,3])
