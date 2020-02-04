import math
import os
import random
import re
import sys


def getHealth(genes, health, first, last, gen):
    genHealth = 0

    subHealth = health[first:last + 1]
    subGenes = genes[first:last + 1]

    subHealths = {}
    letterN = []

    for i in range(len(subHealth)):
        if not subGenes[i] in subHealths:
            subHealths[subGenes[i]] = subHealth[i]
        else:
            subHealths[subGenes[i]] += subHealth[i]

        letterN.append(len(subGenes[i]))

    letterN = set(letterN)

    genHealth = cropGen2(gen, subHealths, letterN)

    return genHealth


def cropGen2(gen, subHealths, letterN):
    genHealth = 0

    for nL in letterN:
        for i in range(0, len(gen) - nL + 1):
            if (gen[i:i + nL] in subHealths):
                genHealth += subHealths[gen[i:i + nL]]

    return genHealth

def main():
    n = int(input())
    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())

    healths = []

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]
        healths.append(getHealth(genes, health, first, last, d))

    print(min(healths), max(healths))

def test():

    genes = "a b c aa d b".rstrip().split()

    health = list(map(int, "1 2 3 4 5 6".rstrip().split()))

    s = 3

    healths = []

    s_values = ["1 5 caaab","0 4 xyz","2 4 bcdybc"]

    for s_itr in s_values:
        firstLastd = s_itr.split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]
        healths.append(getHealth(genes, health, first, last, d))

    print(min(healths), max(healths))

def generateDictionary(keys):

    genMap = {}

    for key in keys:
        chars = tuple(key)
        for i in range(len(key)):
            s = "['%s']"*(i+1)
            sp ="['%s']"*(i)
            s = 'genMap'+ (s % chars[0:i+1])
            sp = 'genMap'+ (sp % chars[0:i])
            exec("if not key[i:i+1] in %s: %s={} " % (sp,s))

            print(genMap)







if __name__ == '__main__':
    #main()
    #test()

    generateDictionary(['the', 'han', 'and', 'pork', 'port', 'pot', 'ha', 'e'])


"""
Input
6
a b c aa d b
1 2 3 4 5 6
3
1 5 caaab
0 4 xyz
2 4 bcdybc
"""