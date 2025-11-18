print("---Student's Grade Checker Program---")
std_per = int(input("Enter your percentage to check your grade: "))
std_per = 10
if std_per >=80:
    print("Wonderfull!😁 You have got 'A+1' grade")
elif std_per >=70 and std_per <80:
    print("Excellent!😄 You have got 'A' grade")
elif std_per >=60 and std_per < 70:
    print("Good!🙂 You have got 'B' Grade")
elif std_per >=50 and std_per < 60:
    print("Nice!😊 You have got 'C' Grade")
elif std_per >=40 and std_per < 50:
    print("Required's Effort!😔 Your Grade is D")
elif std_per < 40:
    print("You are Failed😢")
else:
    print("Your entered percentage is wrong❌ please enter your percentage in number")                           