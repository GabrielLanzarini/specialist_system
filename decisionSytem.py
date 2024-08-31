from utils import getAllActivities, getClimate, checkPrice, generateAnswer
from json import load

file = open("./allDestiny.json", encoding="utf8")
data = load(file)


def filterByAct(index: int):
    filteredStates = []
    activities = getAllActivities()
    activity = activities[index]
    for states in data:
        if activity in states["activities"]:
            filteredStates.append(states["state"])
    return filteredStates


def filterByDateAndClimate(dateIndex: int, climateIndex: int):
    filteredDates = []
    climate = getClimate(climateIndex)

    if dateIndex == 0:
        date = "beforeJune"
    else:
        date = "afterJune"

    for states in data:
        if states["climate"][date] == climate:
            filteredDates.append(states["state"])

    return filteredDates


def filterByPrice(index: int):
    filteredStates = []

    for states in data:
        isMatchedPrice = checkPrice(index, states["mediumPrice"])
        if isMatchedPrice:
            filteredStates.append(states["state"])
    return filteredStates


def findMatchStates(act: list, dateClimate: list, price: list, showMessages: bool):
    dateInterception = [item for item in act if item in dateClimate]
    priceInterception = [item for item in dateInterception if item in price]

    if len(priceInterception) == 0 and len(dateInterception) == 0:
        return []

    if len(priceInterception) == 0:
        if showMessages:
            print("-" * 70)
            print(
                "Para melhores resultados foi necessário remover seu filtro de preço!"
            )
        return dateInterception[:3]

    return priceInterception[:3]


def processData(data: object, showMessages: bool):
    actStates = filterByAct(data["activity"])
    dateClimateStates = filterByDateAndClimate(data["date"], data["climate"])
    priceStates = filterByPrice(data["price"])

    matchAllStates = findMatchStates(
        actStates, dateClimateStates, priceStates, showMessages
    )
    return generateAnswer(matchAllStates)
