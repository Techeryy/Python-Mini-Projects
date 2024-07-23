# A python implementation of a linear search,
# algorithm, where items are individually
# compared against an item being searched for.
# part of Techeryy/Python-Mini-Projects
# Programmed By: Stephen Adams

def linearSearch(x, list):
    for item in list:
        if x is item:
            return True
    return False

print(linearSearch('David',['James','Michael','Robert','John','David','William']))