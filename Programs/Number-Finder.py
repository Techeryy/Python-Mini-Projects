# A simple algorithm to find a target within a large 
# number even if the number is seperated by values
# not included within the target number.
# part of Techeryy/Python-Mini-Projects
# Programmed By: Stephen Adams

number = 29834790827659846598324509687326459832745982740972195862
target = 4567

def findTarget(number,target,initial=[]):
    if not str(number).isdigit(): return False
    target = list(str(target))
    for num in str(number):
        if num in target:
            if target[len(initial)] == num:
                initial.append(num)
                if initial == target: return True
            else: initial = []
    return False

print(findTarget(number,target))