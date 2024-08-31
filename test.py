from itertools import product
from decisionSytem import processData


def getAllProbsInSystem():
    activityRange = range(7)
    dateRange = range(2)
    climateRange = range(2)
    priceRange = range(3)

    allProbs = list(product(activityRange, dateRange, climateRange, priceRange))

    return [
        {"activity": comb[0], "date": comb[1], "climate": comb[2], "price": comb[3]}
        for comb in allProbs
    ]


allProbs = getAllProbsInSystem()

unMatch = 0
match = 0

for prob in allProbs:
    finalAnswer = processData(prob, False)
    if len(finalAnswer) == 0:
        unMatch += 1
    else:
        match += 1

print(f"MATCH: {match}")
print(f"UNMATCH: {unMatch}")
