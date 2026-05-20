#Write  a python program to display message "This is first python program"
#print("This is my first python program ")
#to input all basic data types and print  its output
'''a=10
b=10.5
c='A'
d="Python"
e=True
print("Integer:",a)
print("Float:",b)
print("Char:",c)
print("String:",d)
print("Boolen:",e)
# enter 2 nos and perform arithmetic
a=int(input("Enter value a "))
b=int(input("Enter value b"))
print("Add :",a+b)
print("Sub:",a-b)
print("Mul:",a*b)
print("Div:",a/b)

# find 3rd angle 
a=int(input("Enter value a "))
b=int(input("Enter value b"))
c=180-(a+b)
print("The thrid angle is :",c)
 # 5 sub marks and percentage
a=int(input("Enter value a "))
b=int(input("Enter value b"))
c=int(input("Enter value c "))
d=int(input("Enter value d"))
e=int(input("Enter value e "))
total=a+b+c+d+e
per=total/5
print("The total marks are :",total)
print("The percentage is :",per)
#Find si
p=float(input("Enter value p "))
r=float(input("Enter value r"))
t=float(input("Enter value t"))
si=(p*r*t)/100
print ("The si is:",si)
# swap 2 nos into 3rd
a=int(input("Enter value a "))
b=int(input("Enter value b"))
temp=a
a=b
b=temp
print("After swap:",a)
print("After swap:",b)
# swap without 3rd variable
a=int(input("Enter value a "))
b=int(input("Enter value b"))
a=a+b
b=a-b
a=a-b
print("after swap a=",a)
print("after swap b=",b)
#ASCII values 
ch=input("Enter the char")
print("the ASCII value of char is :",ord(ch))'''
#10
sec=int(input("Enter the sec value "))
hours=sec//3600
minutes=(sec % 3600)//60
sec=sec%60
print("Hours =",hours,"Minutes=",minutes,"Seconds=",sec)
#Write a java program to check whether number is neon or not.
     Input : 9
     Output : Neon Number Explanation: square is 9*9 = 81 
	 and sum of the digits of the square is 9.
num=int(input ("Enter the value of num"))
square=num*num
sum=0
temp=square
while square >0:
    digit=square%10
    sum=sum+digit
    square=square//10
if sum==num:
    print("The number is neon is the  square is ",num,"*",num," =",temp,
              " and sum of the digits of the square is",sum)
else:
    print("The number is not neon")
#13
num= int(input("Enter the num"))
if num%2==0:
    print("The number is even")
else :
    print("The number is odd")
#16 positiv,neg,or zero
num=int(input("Enter the number"))
if num>0:
    print("The number is positive")
elif num<0:
    print("Neg")
else:
    print("Zero")
#Q14. Write a Java program to check whether a triangle is valid or not.
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))
if a+b+c==180:
    print("valid ")
else:
    print("not valid")
#Q17. Write a Java program to check whether a number is divisible by 5 and 11 or not.
num=int(input("Enter the number"))
if num%5==0 and num%11==0:
    print("the number is divisible by 5 and 11")
else:
    print("the number is not ")
#Q15. Write a Java program to check whether a triangle is equilateral , isoscale or scalene.
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))
if a==b==c:
    print("Equilateral ")
elif a==b or  b==c:
    print("Isoscale")
else:
    print("Scalene")














 
 

 
