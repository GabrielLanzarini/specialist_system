from json import load

file = open("./allDestiny.json", encoding="utf8")
data = load(file)


def questionHelper(inputText: str, maxSelection: int):
    answer = -1
    while answer < 0 or answer > maxSelection:
        answer = int(input(inputText))
        if answer < 0 or answer > maxSelection:
            print("Por favor selecione um parâmetro dentro dos fornecidos!")
    return answer


def getAllActivities():
    allAct = []
    for dataIndex in data:
        for activity in dataIndex["activities"]:
            if activity not in allAct:
                allAct.append(activity)
    return allAct


def getClimate(index: int):
    if index == 0:
        return "quente"
    return "fria"


def checkPrice(index: int, price: int):
    if index == 0 and (price >= 3500 and price <= 4100):
        return True
    if index == 1 and (price > 4100 and price <= 4500):
        return True
    if index == 2 and price > 4500:
        return True

    return False


def generateAnswer(statesArr: list):
    allAnswers = []
    for states in data:
        if states["state"] in statesArr:
            answer = f"""
            Estado: {states["state"]}
            Clima antes de junho: {states["climate"]["beforeJune"]}
            Clima depois de junho: {states["climate"]["afterJune"]}
            Preço médio: {states["mediumPrice"]}
            Atividades: {', '.join(states["activities"])}"""
            allAnswers.append(answer)
    return allAnswers
