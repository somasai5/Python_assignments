# Student performance analyzer
n = int(input("Enter the no. of students: "))
studentMarks = []
studentRegistrationNumbers = []
for i in range(n):
    regNo = input(f"Enter registration number of student {i+1}: ").strip()
    marks = float(input(f"Enter marks of student {i+1}: "))
    studentMarks += [marks]
    studentRegistrationNumbers += [regNo]

totalValid = 0
totalFailed = 0

print("\nReg No : Marks : Category")
print("--------------------------")

for i in range(n):
    if(int(studentRegistrationNumbers[i][-1])>5):
        if(studentMarks[i]<=39 and studentMarks[i]>=0):
            studentMarks[i]+=10
        elif(studentMarks[i]<=59 and studentMarks[i]>=40):
            studentMarks[i]+=5
        elif(studentMarks[i]<=74 and studentMarks[i]>=60):
            studentMarks[i]+=3
    if studentMarks[i]>100 or studentMarks[i]<0:
        print(f"{studentRegistrationNumbers[i]} : {studentMarks[i]} : invalid marks ")
    elif studentMarks[i] >= 90:
        print(f"{studentRegistrationNumbers[i]} : {studentMarks[i]} : Excellent ")
        totalValid += 1
    elif studentMarks[i]>=75:
        print(f"{studentRegistrationNumbers[i]} : {studentMarks[i]} : Very Good ")
        totalValid += 1
    elif studentMarks[i]>=60:
        print(f"{studentRegistrationNumbers[i]} : {studentMarks[i]} : Good ")
        totalValid += 1
    elif studentMarks[i]>=40:
        print(f"{studentRegistrationNumbers[i]} : {studentMarks[i]} : Average ")
        totalValid += 1
    else :
        print(f"{studentRegistrationNumbers[i]} : {studentMarks[i]} : Fail ")
        totalValid += 1
        totalFailed += 1
print("total valid students: ", totalValid)
print("total failed students: ", totalFailed)