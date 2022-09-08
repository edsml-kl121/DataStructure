# Find the smallest number through traversing
# Then swap the first number in the array with that smallest number.
# Repeat

# time O(n^2), space O(1)

def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        for j in range(i, len(array)):
            min = array[i]
            if array[j] < min:
                array = swap(array, i, j)
    return array
                
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array
    