# An asteroid is heading towards the Earth, and we need the brightest minds to prevent that. Are you qualified to solve the first challenge?

# Each letter stands for a different digit between 0 and 9. What's the value of the EARTH? When you find the answer, go to http://bit.ly/36Ok2Vr

#       E A R T H 
#  +    V E N U S 
#     U R A N U S
#     ------------
#     S A T U R N 

import numpy as np
import random

def getPlanetValue(planet,letters, letterValue):

    value = ""
    for s in planet:
        value+=str(letterValue[letters.index(s)])
        
    return int(value)

def calculateError(letters, letterValue):
    earth=getPlanetValue("EARTH",letters, letterValue)
    venus=getPlanetValue("VENUS",letters, letterValue)
    uranus=getPlanetValue("URANUS",letters, letterValue)
    saturn=getPlanetValue("SATURN",letters, letterValue)

    saturnResult = earth+venus+uranus

    return abs(saturnResult-saturn)

def generateRandomPopulation(n):
    population = []

    for i in range(n):
        population.append(random.sample(range(0, 9), 9))

    return population

def getBetterAsParents(population, error, n):
    
    error, population = zip(*sorted(zip(error, population)))
    return population[:n]

def getErrorArray(population, letters):
    
    error = []
    for element in population:
        error.append(calculateError(letters, population))
    return error

letters = ['A','E','H','N','R','S','T','U','V']

