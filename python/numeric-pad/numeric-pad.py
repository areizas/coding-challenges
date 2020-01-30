from itertools import permutations
array=[0,1,2,3,4,5,6,7]
permutations = list(permutations(array))

def rules_ok(a):
    for x in range(7):
        for y in range(x+1,8):
            if abs(x-y)==abs(a[x]-a[y]):
                return False

    return True


possiblePermutations = []

for each in permutations:
    if rules_ok(each):
        possiblePermutations.append(each)

for i in possiblePermutations:
    print(i)