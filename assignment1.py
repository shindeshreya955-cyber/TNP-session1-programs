# Q1. Find Maximum and Minimum Element in Array

class ArrayMax:
    def inputArray(self, arr):
        self.arr = arr
    def findMax(self):
        maximum = self.arr[0]
        for i in self.arr:
            if i > maximum:
                maximum = i
        return maximum
    def findMin(self):
        minimum = self.arr[0]
        for i in self.arr:
            if i < minimum:
                minimum = i
        return minimum
obj = ArrayMax()
obj.inputArray([10, 20, 5, 40, 15])
print("Maximum Element:", obj.findMax())
print("Minimum Element:", obj.findMin())

# Q2. Calculate Sum of Array Elements

class ArraySum:
    def inputArray(self, arr):
        self.arr = arr
    def calculateSum(self):
        total = 0
        for i in self.arr:
            total += i
        return total
obj = ArraySum()
obj.inputArray([1, 2, 3, 4, 5])
print("Sum:", obj.calculateSum())

# Q3. Calculate Average of Array Elements

class ArrayAverage:
    def inputArray(self, arr):
        self.arr = arr
    def findAverage(self):
        total = sum(self.arr)
        average = total / len(self.arr)
        return average
obj = ArrayAverage()
obj.inputArray([10, 20, 30, 40])
print("Average:", obj.findAverage())

# Q4. Search an Element in Array

class ArraySearch:
    def inputArray(self, arr):
        self.arr = arr
    def searchElement(self, key):
        for i in self.arr:
            if i == key:
                return True
        return False
obj = ArraySearch()
obj.inputArray([5, 10, 15, 20])
print(obj.searchElement(15))


# Q5. Count Even and Odd Numbers

class ArrayEvenOdd:
    def inputArray(self, arr):
        self.arr = arr
    def countEven(self):
        even = 0
        for i in self.arr:
            if i % 2 == 0:
                even += 1
        return even
    def countOdd(self):
        odd = 0
        for i in self.arr:
            if i % 2 != 0:
                odd += 1
        return odd
obj = ArrayEvenOdd()
obj.inputArray([1, 2, 3, 4, 5, 6])
print("Even Count:", obj.countEven())
print("Odd Count:", obj.countOdd())


# Q6. Reverse the Array

class ArrayReverse:
    def inputArray(self, arr):
        self.arr = arr
    def reverseArray(self):
        reversed_array = self.arr[::-1]
        print("Reversed Array:", reversed_array)
obj = ArrayReverse()
obj.inputArray([1, 2, 3, 4, 5])
obj.reverseArray()

# Q7. Sort Array in Ascending Order

class ArraySort:
    def inputArray(self, arr):
        self.arr = arr
    def sortArray(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        print("Sorted Array:", self.arr)
obj = ArraySort()
obj.inputArray([5, 2, 8, 1, 3])
obj.sortArray()


# Q8. Copy Array Elements into Another Array

class ArrayCopy:
    def inputArray(self, arr):
        self.arr = arr
    def copyArray(self):
        new_array = []
        for i in self.arr:
            new_array.append(i)
        return new_array
obj = ArrayCopy()
obj.inputArray([1, 2, 3, 4])
print("Copied Array:", obj.copyArray())

# Q9. Merge Two Arrays

class ArrayMerge:
    def inputArray(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
    def mergeArrays(self):
        merged = self.arr1 + self.arr2
        return merged
obj = ArrayMerge()
obj.inputArray([1, 2, 3], [4, 5, 6])
print("Merged Array:", obj.mergeArrays())

# Q10. Count Frequency of Each Element

class ArrayFrequency:
    def inputArray(self, arr):
        self.arr = arr
    def countFrequency(self):
        visited = []
        for i in self.arr:
            if i not in visited:
                count = 0
                for j in self.arr:
                    if i == j:
                        count += 1
                print(i, "appears", count, "times")
                visited.append(i)
obj = ArrayFrequency()
obj.inputArray([1, 2, 2, 3, 1, 4, 2])
obj.countFrequency()

# Q11. Find Second Largest Element

class ArraySecondLargest:
    def inputArray(self, arr):
        self.arr = arr
    def findSecondLargest(self):
        largest = second = -999999
        for i in self.arr:
            if i > largest:
                second = largest
                largest = i
            elif i > second and i != largest:
                second = i
        return second
obj = ArraySecondLargest()
obj.inputArray([10, 20, 40, 30, 50])
print("Second Largest:", obj.findSecondLargest())

# Q12. Check Array is Palindrome or Not

class ArrayPalindrome:
    def inputArray(self, arr):
        self.arr = arr
    def isPalindrome(self):
        n = len(self.arr)
        for i in range(n // 2):
            if self.arr[i] != self.arr[n - i - 1]:
                return False
        return True
obj = ArrayPalindrome()
obj.inputArray([1, 2, 3, 2, 1])
print("Palindrome:", obj.isPalindrome())



