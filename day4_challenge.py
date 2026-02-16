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

totalValid=0
totalIgnored=0


for scores in activityScores:
    if scores>100:
        critical_risk += [scores]
        totalValid = totalValid + 1
    elif scores>60:
        high_risk += [scores]
        totalValid = totalValid + 1
    elif scores>30:
        medium_risk += [scores]
        totalValid = totalValid + 1
    elif scores>0:
        low_risk += [scores]
        totalValid = totalValid + 1
    else:
        totalIgnored += 1

print("\nlow risk :",low_risk)
print("medium risk :",medium_risk)
print("high risk :",high_risk)
print("critical risk :",critical_risk)


print("\nTotal valid :",totalValid)
print("Total ignored :",totalIgnored)



