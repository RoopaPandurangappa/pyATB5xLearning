score=int(input("Enter your score to find Grade"))
if score<=100 and score>=90 :
    print("Your Grade is A")
elif score <=89 and score>=70 :
    print("Your Grade is B")
elif score <=69 and score >=50 :
     print("Your Grade is C")
else:
     print("You need to study again")