FullName = input("enter your FullName: ")
EmailID = input("enter your EmailID: ")
MobileNumber = int(input("enter your MobileNumber: "))
Age = int(input("enter your Age: "))
if FullName.count(" ")<1 or FullName[0]==" " or FullName[-1]==" " :
    print("user profile invalid")
elif EmailID.find('@')==-1 or EmailID.find('.')or EmailID[0]=="@" :
    print("user profile invalid")
elif len(MobileNumber)!=10 or not MobileNumber.isdigit() or MobileNumber[0]=="0" :
    print("user profile invalid")
elif Age<18 or Age>60 :
    print("user profile invalid")
else :
    print("user profile is valid")