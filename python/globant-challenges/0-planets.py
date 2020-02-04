# An asteroid is heading towards the Earth, and we need the brightest minds to prevent that. Are you qualified to solve the first challenge?

# Each letter stands for a different digit between 0 and 9. What's the value of the EARTH? When you find the answer, go to http://bit.ly/36Ok2Vr

#       E A R T H
#  +    V E N U S
#     U R A N U S
#     ------------
#     S A T U R N

import random
from itertools import permutations

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = list(permutations(array))


def getPlanetValue(planet, letters, letterValue):
    value = ""
    for s in planet:
        value += str(letterValue[letters.index(s)])

    return int(value)


def calculateError(letters, letterValue):
    earth = getPlanetValue("EARTH", letters, letterValue)
    venus = getPlanetValue("VENUS", letters, letterValue)
    uranus = getPlanetValue("URANUS", letters, letterValue)
    saturn = getPlanetValue("SATURN", letters, letterValue)

    saturnResult = earth + venus + uranus

    return abs(saturnResult - saturn)


letters = ['A', 'E', 'H', 'N', 'R', 'S', 'T', 'U', 'V']


def to_array(a):
    b = []
    for i in a:
        b.append(i)
    return b


correctValues = []

for n in permutations:
    ar = to_array(n)

    if calculateError(letters, ar[1::]) == 0:
        st = ""
        for i in range(1, len(ar)):
            st += "{}={} ".format(letters[i - 1], ar[i])
        correctValues.append(ar)
        print(st)

# Solutions
# A=2 E=7 H=4 N=0 R=5 S=8 T=1 U=6 V=9
# A=6 E=9 H=4 N=8 R=5 S=2 T=3 U=1 V=0
