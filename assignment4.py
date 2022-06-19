marks = int(input("Enter your marks"))     #for marks entry

if marks<25:
    print("F")                             #for F grade
elif marks>=25 and marks<45:
    print("E")                             #for E grade
elif marks>=45 and marks<50:
    print("D")                             #for D grade
elif marks>=50 and marks<60:
    print("C")                             #for C grade
elif marks>=60 and marks<80:
    print("B")                             #for B grade
else :
    print("A")                             #for A grade

#QUESTION2

year = int(input("Enter your year"))           #year entry for leap year    

if year%4==0 :                                 #main condition for leap year 
    if year%100!=0 or year%400==0 :            #for leap year
       print (year,"is a leap year")           
    else :
        print(year,"is not a leap year")       #for not leap year
else :
    print (year, "is not a leap year")         #second condition for not leap year
    
#QUESTION3
from random import randint                     #import of randint function from random module
n=0 
while n<10:                                    #while loop
    x=randint(0,9)
    y=randint(0,9)

    print("What is ",x,"times",y)
    guess=int(input("Enter your answer:"))    #answer entrty

    if guess==x*y:                            #if condition for guess of answer
        print("Correct")
    else:
        print("That is incorrect"," The correct answer is :",x*y) #for incorrect answer
    n=n+1
else :
    print("Thank you for playing")            #thanks for playing salutation 

#QUESTION4

for candies in range(200) :
    if candies%5 == 2 and candies%6 == 3 and candies%7 ==2 :  #condition for finding number of candies
      print("Number of candy are :",candies)                  #printing number of candies
