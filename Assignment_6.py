# Question-1
num= int(input("enter the number:\n"))
i=1
sum=0
while(num>i):
    if num%i==0: 
        sum=sum+i
    i+=1
if sum==num:
    print("Perfect Number")
else :
    print("Not Perfect NUmber")

# Question-2

n=input()
n=n.replace(" ","")
a=n[::-1]
if a==n:
    print("YES")
else:
    print("NO")

#Q.3
#Print Pascal's Triangle in Python
from math import factorial
 
n = 5
for i in range(n):
    for j in range(n-i+1):
 
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    print()

#Q.4
import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
print ( ispangram('The quick brown fox jumps over the lazy dog'))


#Question-5
n=input().split("-")
n.sort()
sum=""
for i in n:
    if(sum==""): sum+=i
    else: sum=sum+"-"+i
print(sum)

#Q.6
def student(student_id, student_name, student_class):
    return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'
print(student('21102099', 'Auchitya Sharma', 'B.Tech_1st_year'))

#Q.7
class Student:
    pass 
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 

#Q.8
def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print(arr[i], arr[j], arr[k])
					found = True
	if found == False:
		print("No triplets exist")
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input())
	lst.append(ele) 
findTriplets(lst,n)

#Q.9
class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")
