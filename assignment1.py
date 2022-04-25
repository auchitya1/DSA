# QUESTION 1
print("AVERAGE OF THREE NUMBERS")

a=float(input("Enter the 1st number:- "))
b=float(input("Enter the 2nd number:- "))
c=float(input("Enter the 3rd number:- "))
AVERAGE=(a + b + c) / 3

print("The Average of three given numbers is: " , AVERAGE)

print("-*-")

#QUESTION 2
print("Income tax (GROSS INCOME>$25000)")
GI=int(input("Please Enter the Gross Income:$ "))
NOD=int(input("Please Enter the number of dependents: "))
#deduction1=Standard Deduction
deduction1=10000
#deduction2=Dependent Deduction
deduction2=int(3000*NOD)
Taxable_income=int(GI)-int(deduction1)-int(deduction2)
Tax=.20*Taxable_income
 
print("The total income tax of a person in $: " , Tax)


print("-*-")



#QUESTION 3

Student = []
print("Enter the SID: ")
SID = int(input())
print("Enter the name of the student: ")
Name = input()
print("Enter the gender of the student:")
Gender = input()
print("Enter your Course Name:")
Course = input()
print("Enter the CGPA of the student:")
CGPA = float(input())
Student.append(SID)
Student.append(Name)
Student.append(Gender)
Student.append(Course)
Student.append(CGPA)
print(Student)



print("-*-")


#QUESTION 4
print("Enter marks of 5 students")
list=[]
a=int(input("Marks of First Student:"))
b=int(input("Marks of Second Student: "))
c=int(input("Marks of Third Student: "))
d=int(input("Marks of Fourth Student: "))
e=int(input("Marks of Fifth Student: "))
list.append(a)
list.append(c)
list.append(d)
list.append(b)
list.append(e)
print("The List of marks of five student is as follows: " ,list)


print("-*-")

#QUESTION 5
print("This python program can print a list in an specified manner")
LIST=['Red','Green','White','Black','Pink','Yellow']
LIST.remove('Black')
print(LIST)
LIST[3]=('Purple')
print(LIST)


