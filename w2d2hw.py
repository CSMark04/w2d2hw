# excercise 1

# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

def less(num):
    lten = []
    for n in num:
        if n < 10:
            lten.append(n)
    return lten
            
print(less(l_1))

# excercise 2

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge(list1, list2):
    merged = list1 + list2
    merged = set(merged)
    return merged
print(merge(l_1,l_2))