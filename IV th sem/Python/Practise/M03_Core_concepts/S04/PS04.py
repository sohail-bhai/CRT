'''check for duplicates in traditional and optimal method 
input : [1,2,3,4,5,1]
output : True

input : [1,2,3,4,5]
output : False
def check_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False
    
def check_duplicates_optimal(lst):
    return len(lst) != len(set(lst))'''