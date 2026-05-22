
'''1. Write a Java program to input 5 elements in an array and print all elements.

arr=[]
for i in range (5):
    num=int(input("enter element:"))
    arr.append(num)
print(arr)'''


'''2.Write a Java program to find the sum of all elements of an array.nb7

arr=[1,2,3,4,5]
sum=0
for i in arr:
    sum=sum+i
print("sum is",sum)'''


'''3.Write a Java program to find the average of array elements

arr=[10,20,30,40,50]
sum=0
for i in arr:
    sum=sum+i
avg=sum/len(arr)
print("average is",avg)'''


'''4.Write a Java program to find the largest element in an array.

arr=[10,20,50,40,30]
largest=max(arr)
print("largest element is",largest)'''

'''5. Write a Java program to find the smallest element in an array.

arr=[10,20,50,40,30]
smallest=min(arr)
print("smallest element is",smallest)'''

'''6.Write a Java program to count even and odd numbers in an array

arr=[1,2,3,4,5,6]
even=0
odd=0
for i in arr:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("even numbers =",even)
print("odd numbers =",odd)'''

'''7. Write a Java program to search an element in an array.


arr=[10,20,30,40,50]
num=int(input("enter number"))
if(num in arr):
    print("Element Found")
else:
    print("Element Not Found")'''

'''8. Write a Java program to print array elements in reverse order.

arr=[1,2,3,4,5]
print(arr[::-1])'''


'''9.Write a Java program to copy all elements from one array to another array.

arr=[]
for i in range (5):
    arr.append (int(input("enter the element:")))
b=arr.copy()
print(b)'''


'''10.Find Second Largest Element Write a program to find the second largest element in an array.
Example: Input: [10, 20, 5, 8, 25] Output: 20


arr=[]
for i in range(5):
    arr.append(int(input("enter the element:")))
arr.sort()
print("second largest element is",arr[-2])'''

'''11. Write a program to find the second largest element in an array.
Example: Input: [10, 20, 5, 8, 25] Output: 20

arr=[]
for i in range(5):
    arr.append(int(input("enter the element:")))
largest=max(arr)
arr.remove(largest)
second=max(arr)
print("second largest element is",second)'''

'''12. Reverse an Array
13. Write a program to reverse the elements of an array without using another array.
       Example: Input: [1, 2, 3, 4] Output: [4, 3, 2, 1]

arr=[]
for i in range(4):
    arr.append(int(input("enter the element:")))
arr.reverse()
print(arr)'''


'''14. Find Duplicate Elements
15. Write a program to print duplicate elements in an array.
        Example: Input: [1, 2, 3, 2, 4, 1] Output: 1 2

arr=[]
for i in range(6):
    arr.append(int(input("enter the element:")))
for i in arr:
    if(arr.count(i)>1):
        print(i)'''

'''16. Rotate Array Left by One Position
17. Write a program to rotate array elements to the left by one position.

arr=[]
for i in range(5):
    arr.append(int(input("enter the element:")))
first=arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[-1]=first
print(arr)'''


'''18. Merge Two Arrays
19. Write a program to merge two arrays into a single array.
Example: Array1: [1, 2, 3] Array2: [4, 5, 6] Output: [1, 2, 3, 4, 5, 6]

arr1=[]
arr2=[]
for i in range(3):
    arr1.append(int(input("enter element in array1:")))
for i in range(3):
    arr2.append(int(input("enter element in array2:")))
arr3=arr1+arr2
print(arr3)'''

'''20. Find Missing Number
21. An array contains numbers from 1 to n with one number missing.
22. Find the missing number.Example: Input: [1, 2, 4, 5] Output: 3

arr=[]
for i in range(4):
    arr.append(int(input("enter element:")))
n=5
total=n*(n+1)//2
sum=0
for i in arr:
    sum=sum+i
missing=total-sum
print("missing number is",missing)'''


'''23. Check Array is Sorted or Not
24. Write a program to check whether the array is sorted in ascending order.
Example: Input: [1, 2, 3, 4] Output: Sorted

arr=[]
for i in range(4):
    arr.append(int(input("enter element:")))
if(arr==sorted(arr)):
    print("Sorted")
else:
    print("Not Sorted")'''



