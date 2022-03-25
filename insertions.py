import random

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
              
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key

data = []
for i in  100:
    data.append(random.randrange(1,1000))
#data = [9, 5, 45, 1, 333, 4, 3, 56, 34, 67, 89, 34, 23]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

