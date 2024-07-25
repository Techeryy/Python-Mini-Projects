# A python implementation of a bubble sort algorithm,
# that works by repeatedly swapping adjacent items
# if they are in the wrong order, over the course of
# a series of passes, part of 
# Techeryy/Python-Mini-Projects
# Programmed By: Stephen Adams

def bubbleSort(list):
    for p in range(len(list)-1):
        swapped = False
        for i in range((len(list)-1)-p):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swapped = True
        if not swapped: break
    return list

print(bubbleSort([9,8,7,6,5,4,3,2,1]))