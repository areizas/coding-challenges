# 'R', 'E', 'G', 'U', 'L', 'A', 'T', 'I', 'O', 'N'
# a = [ 0   ,1   ,2   ,3   ,4   ,5   ,6   ,7   ,8   ,9]
# a = ['R', 'E', 'G', 'U', 'L', 'A', 'T', 'I', 'O', 'N']

from itertools import permutations
import math

array=[0,1,2,3,4,5,6,7,8,9]
permutations = list(permutations(array))

def get_values(a):
    regulation = int(''.join([str(elem) for elem in a]))
    rule = int(str(a[0])+str(a[3])+str(a[4])+str(a[1]))
    ignoreall = int(str(a[7])+str(a[2])+str(a[9])+str(a[8])+str(a[0])+str(a[1])+str(a[5])+str(a[4])+str(a[4]))

    return [regulation, rule, ignoreall]

def validation(ar):
    if math.sqrt(ar[0]).is_integer() and math.sqrt(ar[1]).is_integer():
        return True
    else:
        return False

def to_array(a):
    b = []
    for i in a:
        b.append(i)
    return b

for n in permutations:
    ar = to_array(n)
    ar = get_values(n)

    if validation(ar):
        print(ar)