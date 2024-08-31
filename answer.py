from helper import allActivities
import json

file = open("./allDestiny.json")
data = json.load(file)


def getAllByAct(index: int):
    filteredStates = []
    activitie = allActivities()[index]
    for states in data:
        if activitie in states["activities"]:
            filteredStates.append(states)
    return filteredStates


def getAllByClimate(index: int):
    filteredStates = []
    climate = ""
    
    if index == 0:
        climate = "quente"
    else:
        climate = "fria"

    for states in data:
      print(states["climate"])
      

getAllByClimate(1)
