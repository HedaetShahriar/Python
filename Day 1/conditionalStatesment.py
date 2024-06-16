grade=int(input("Enter your number: "))
if grade>=90 :
    print("You got an A+")
elif grade<90 and grade>=85:
    print("you got an A")
elif grade<85 and grade>=80:
    print("You got B+" )
elif grade<80 and grade>=75:
    print("You got B")
elif grade<75 and grade>=70:
    print("You got C+")
elif grade<70 and grade>=65:
    print("You got C")
elif grade<65 and grade>=60:
    print("You got D+")
elif grade<60 and grade>=50:
    print("You got D")
else: 
    print("You Failed")