import json

file = open("./allDestiny.json")
data = json.load(file)


def question_helper(inputText: str, maxSelection: int):
    answer = -1
    while answer < 0 or answer > maxSelection:
        answer = int(input(inputText))
        if answer < 0 or answer > maxSelection:
            print("Por favor selecione um parametro dentro dos fornecidos!")
    return answer


def allActivities():
    allAct = []
    for dataIndex in data:
        for activity in dataIndex["activities"]:
            if activity not in allAct:
                allAct.append(activity)
    return allAct
