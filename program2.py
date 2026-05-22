''' #Q1. Write a Java program to reverse a number without using loop.
Input a number: 123 Reverse number: 321
no=int(input("enter number:"))
a=no//100
b=(no//10) %10
c=no%10
num=(c*100)+(b*10) +a
print("reversed number is:",num)'''

'''#Q2. Write a program to find first and last digit of a number without using loop in three digit.
num=int(input("enter number:"))
first=num//100
last=num%10
print("the first number is ",first)
print("the last number is ",last)'''


'''#Q3. Write a program to calculate sum of first and last digit of a number without using loop.
Input : 123
Output : 4

num=int(input("enter the number"))
first=num//100
last=num%10
sum=first+last
print("the first number is ",sum)'''

'''#Q4. Write a java program to check whether number is neon or not.
Input : 9
Output : Neon Number Explanation: square is 9*9 = 81 and sum of the digits of the square is 9.

num=int(input("enter the number"))
count=0
for i in range(1,num+1) :
    if num%i==0:
        count=count+1
if count==2:
    print("the number is prime")
else:
    print("the number is not prime")'''

'''#Q5. Write a java program to check whether number is palindrome or not.

num=int(input("enter the number"))
rev=0
temp=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print("number is palidrome")
else:
    print("number is not palidrome")'''

'''#Q.6Write a Java program to check whether character is alphabetic or not.'''


'''#Q.8 Write a java program to input any alphabet and check whether it is vowel or consonant.
ch=input("enter the char:")
if ch in ('a','e','i','o','u'):
    print("vowel")
else:
    print("consonant")'''

'''Q7. Write a Java program to input cost price and selling price of a product and check profit or loss.

cp=int(input("enter the cp"))
sp=int(input("enter the sp"))
if sp>cp:
    print("profit")
else:
    print("loss")'''

'''Q.9Write a java program to find maximum between three numbers.

first=int(input("enter the first number :"))
sec=int(input("enter the sec number:"))
third=int(input("enter the third number:"))
if first>sec or first>third:
    print("the first number is maximum")
elif sec>third:
    print("the sec number is max")
else:
    print("the third number is max")'''

'''Q.10 Write a java program to find a minimum between three numbers.
first=int(input("enter the first number :"))
sec=int(input("enter the sec number:"))
third=int(input("enter the third number:"))
if first<sec and first<third:
    print("the first number is min")
elif sec<third:
    print("the sec number is min")
else:
    print("the third number is min")'''

'''Q.11 Print a grade using ternary operators:
90+: A
80–89: B
70–79: C 
<70: F

marks=int(input("enter the marks:"))
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
else:
    print("F")'''


'''Q12.Write a java program to find the total number of notes in a given amount.  
                    	
Enter the amount: 2528
Expected output :
500=5 ,100=0 , 50=0 , 20=1 , 10=0 , 5=1 , 2=1 , 1=1

amount=int(input("enter the amount:"))
print("500=",amount//500)
amount=amount%500
print("100=",amount//100)
amount=amount%100
print("50=",amount//50)
amount=amount%50
print("20=",amount//20)
amount=amount%20
print("10=",amount//10)
amount=amount%10
print("5=",amount//5)
amount=amount%5
print("2=",amount//2)
amount=amount%2
print("1=",amount//1)
amount=amount%1'''

'''Q.13 Check whether a given employee is eligible for bonus:
 Input: Years of service and salary.
Logic: If service > 5 years, give 5% bonus.
Output: Display bonus amount or no bonus.

service=int(input("enter year of service:"))
salary=int(input("enter salary:"))
if(service>5):
    bonus=salary*5/100
    print("Bonus is",bonus)
else:
    print("No Bonus")'''

'''Q.14Calculate commission based on sales amount:
Input: Sales amount
Logic:
Sales < 5000 → 2% commission
Sales 5000–10000 → 5% commission
Sales > 10000 → 10% commission
Output: Display commission amount.

sales=int(input("enter the sales amount:"))
if(sales<5000):
    c=sales*2/100
elif(sales<=10000):
    c=sales*5/100
else:
    c=sales*10/100
print("Commission is",c )'''


'''Q16. Write a program that takes a grade (A, B, C, D, F) as input and displays the corresponding remark using switch:
A: Excellent
B: Good
C: Average
D: Poor
F: Fail
Explanation:
 Use a char or string in switch to match grades and print remarks.

grade=input("enter grade")
if (grade=='A'):
    print("Excellent")
elif (grade=='B'):
    print("Good")
elif (grade=='C'):
    print("Average")
elif (grade=='D'):
    print("Poor")
elif (grade=='E'):
    print("Fail")
else:
    print("Invalid grade")'''

'''Q.15Create a Java program to simulate a simple calculator using a switch case. It should take two numbers and an operator (+, -, *, /, %) as input and perform the corresponding operation.
Explanation:
 Use a switch on the operator to handle different arithmetic operations. Add default to handle invalid operators.

          
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
op=input("enter the value of op")
if op=='+':
    print("Result",a+b)
elif op=='-':
    print("Result",a-b)
elif op=='*':
    print("Result",a*b)
elif op=='/':
    print("Result",a/b)
elif op=='%':
    print("Result",a%b)
else:
    print("invalid")'''

'''Q17. Develop a Java program using switch to print the day type for an input day number (1-7):
1 for Monday, …, 7 for Sunday.
For 1-5, display “Weekday”; for 6-7, display “Weekend”.
Explanation:
 Use switch with multiple cases falling through for weekdays and weekends.

day=int(input("enter day number:"))
if(day>=1 and day<=5):
    print("weekday")
elif(day==6 or day==7):
    print("weekend")
else:
    print("invalid day")'''

'''Q19. Create a Java program using switch to convert a given number (1-5) to its word equivalent (One, Two, ..., Five). If the number is not between 1 and 5, display “Invalid number”.
Explanation:
 Switch with cases 1 to 5; default to handle invalid numbers.

num=int(input("enter the number:"))
if(num==1):
    print("one")
elif(num==2):
    print("two")
elif(num==3):
    print("three")
elif(num==4):
    print("four")
elif(num==5):
    print("five")
else:
    print("inavlid number")'''





