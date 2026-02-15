# Student performance analyzer
registrationNumber = int(input("Enter your registration number: "))
activityScores = []
n = int(input("Enter number of activities: "))
print("Enter activities: ")
for i in range(n):
    x = int(input())
    activityScores += [x]
print('activity Scores :',activityScores)

low_risk = []
medium_risk = []
high_risk = []
critical_risk = []



for scores in activityScores:
    if scores>100:
        critical_risk += [scores]
    elif scores>60:
        high_risk += [scores]
    elif scores>30:
        medium_risk += [scores]
    elif scores>0:
        low_risk += [scores]
    else:


print("\nlow risk :",low_risk)
print("medium risk :",medium_risk)
print("high risk :",high_risk)
print("critical risk :",critical_risk)


if(registrationNumber%3 == 0):
    personalization = len(low_risk)
    low_risk = []
else:
    personalization = len(critical_risk)
    critical_risk = []

print("\n After personalization :")
print("low risk :",low_risk)
print("medium risk :",medium_risk)
print("high risk :",high_risk)
print("critical risk :",critical_risk)
