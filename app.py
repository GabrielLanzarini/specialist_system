from utils import question_helper, getAllActivities
from decisionSytem import processData

activities = getAllActivities()

print("Que atividade você tem mais interesse em fazer?")
for index, activitie in enumerate(activities):
    print(f"- [{index}] {activitie}")
chooseActivity = question_helper("Atividade: ", len(activities) - 1)

print(
    """Você pretende viajar?
- [0] Antes de junho
- [1] Depois de junho"""
)
chooseDate = question_helper("Data: ", 2)

print(
    """Que tipo de clima você prefere?
- [0] Quente
- [1] Frio"""
)
chooseClimate = question_helper("Clima: ", 2)

print(
    """Quanto mais ou menos deseja gastar?
- [0] R$3500 e R$4100 (baixo)
- [1] R$4200 e R$4500 (médio)
- [2] Mais de R$4500 (alto)"""
)
choosePrice = question_helper("Preço: ", 3)

answerData = {
    "activity": chooseActivity,
    "date": chooseDate,
    "climate": chooseClimate,
    "price": choosePrice,
}


finalAnswer = processData(answerData)

if len(finalAnswer) == 0:
    print("Infelizmente não foram encontrados possíveis destinos com as suas escolhas!")
else:
    print("-" * 70)
    answerSize = len(finalAnswer)
    print(f"Foram encontrados {answerSize} possiveis destinos:")
    for answer in finalAnswer:
        print(answer)
    print("-" * 70)
