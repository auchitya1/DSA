#Question 1, Find the length of a input srting.
# let the string be "a"
a= "Pyhton is a case sensitive language"
c= len(a)
print(c)

# Question b, Reverse the order in one line code
print(a[::-1])


# Question c, use slice function to "a case sensitive" string
print(a[10:26])
# Question d, replacing 
replaced= a.replace("a case sensitive","object oriented")
print(replaced)
# Question e,
print(a.index("a"))
# Question f
print(a.replace(' ',''))


#question 2
B1="HEY,{ABC} HERE!".format(ABC="Auchitya Sharma")
B2="MY SID IS 2110{XXXX}".format(XXXX="2099")
B3="I AM FROM {XYZ} DEPARTMENT AND MY CGPA IS 9.6".format(XYZ="civil")
print(B1)
print(B2)
print(B3)
#####################################
#QUESTION 3
a=56
b=10
#part a
c=a&b
print("parta:",c)
#part b
d=a|b
print("partb:",d)
#part c
e=a^b
print("partc :",e)
#part d
X=a<<2
print("partd,a:",X)
Y=b<<2
print("partd,b:",Y)
#part e
p=a>>2
print("parte,a:",p)
q=b>>4
print("print,b:",q)
###################################
#QUESTION 4
def iswordpresent (sentence,word):
    s=sentence.split(" ")
    for i in s:
        if (i == word):
            return True
        return False

s="My name is Auchitya Sharma"
word="name"
name="name"
if name==word:
    print("yes")
else:
    print("No")

########################
#question 5

side1 = int(input("ENTER SIDE LENGTH : "))
side2 = int(input("ENTER SIDE LENGTH : "))
side3 = int(input("ENTER SIDE LENGTH : "))
if side1+side2<=side3 or side2+side3<=side1 or side1+side3<=side2:
    print("false")
else:
    print("true")
#############################
#question 6
a = int(input("enter a number : "))
b = int(input("enter another number : "))
count =0
while (a>0 or b>0):
    temp1 = a&1
    temp2 = b&1
    if temp1!=temp2:
        count+=1
    a=a>>1
    b=b>>1
print(count)