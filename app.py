# from filters import
from helper import question_helper, allActivities

activities = allActivities()

print("Que atividade você tem mais interesse em fazer?")
for index, activitie in enumerate(activities):
    print(f"[{index}] {activitie}")
chooseActivity = question_helper("Atividade: ", len(activities) - 1)

print(
    """Você pretende viajar?
- [1] Antes de junho
- [2] Depois de junho"""
)
chooseDate = question_helper("Data: ", 2)

print(
    """Que tipo de clima você prefere?
- [1] Quente
- [2] Frio"""
)

chooseWeather = question_helper("Clima: ", 2)


print(
    """Quanto mais ou menos deseja gastar?
- [1] R$3500 e R$4100 (baixo)
- [2] R$4200 e R$4500 (médio)
- [3] Mais de R$4500 (alto)"""
)
choosePrice = question_helper("Preço: ", 3)
