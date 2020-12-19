# write a Python program to check if year is a leap year or not
year = 2000
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


# write a Program to check if a number is prime or not
num = 407
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")


# write a Program to count the number of each vowels
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?'
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
   if char in count:
       count[char] += 1
print(count)


# write a Program to perform different set operations like in mathematics
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};
print("Union of E and N is",E | N)
print("Intersection of E and N is",E & N)
print("Difference of E and N is",E - N)
print("Symmetric difference of E and N is",E ^ N)


# write a Python program to find the factorial of a number provided by the user.
num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# write Multiplication table (from 1 to 10) in Python
num = 12
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# write a Python program to convert decimal into other number systems
dec = 344
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# write a Python function to find H.C.F of two numbers
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
num1 = 54 
num2 = 24
print("The H.C.F. is", compute_hcf(num1, num2))


# write Python function to find the L.C.M. of two input number
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
num1 = 54
num2 = 24
print("The L.C.M. is", compute_lcm(num1, num2))


# write a Program to find the ASCII value of the given character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


# write a Python program to display all the prime numbers within an interval
lower = 900
upper = 1000
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

  
# write a Python Program to Remove Punctuations From a String
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char
print(no_punct)


# write a Python program to check if the number is an Armstrong number or not
num = 663
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# write a Python program to swap two variables
x = 5
y = 10
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# write a python program to Display the powers of 2 using anonymous function
terms = 15
result = list(map(lambda x: 2 ** x, range(terms)))
print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])


# write a Python program to find the sum of natural using recursive function
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)
num = 16
if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))


# write anonymous  function to find all the numbers divisible by 13 in the list.
my_list = [12, 65, 54, 39, 102, 339, 221,]
result = list(filter(lambda x: (x % 13 == 0), my_list))
print("Numbers divisible by 13 are",result)


# write a Program to transpose a matrix using a nested loop
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for r in result:
   print(r)


# write a Program to multiply two matrices using nested loops

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
for r in result:
   print(r)


# write a Program to add two matrices using nested loop
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)


# write a Python Program to find the area of triangle
a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# write a python program to add two numbers
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# write a Program to sort alphabetically the words form a string provided by the user
my_str = "Hello this Is an Example With cased letters"
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
   print(word)


# write a Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')
dec = 34
convertToBinary(dec)
print()


# write a Python program to display the Fibonacci sequence
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# write a Python function to Split the list and add the first part to the end
def split(arr, n, k):  
    for i in range(0, k):  
        x = arr[0] 
        for j in range(0, n-1): 
            arr[j] = arr[j + 1] 
          
        arr[n-1] = x        
arr = [12, 10, 5, 6, 52, 36] 
n = len(arr) 
position = 2
split(arr, n, position)  
for i in range(0, n):  
    print(arr[i], end = ' ') 


# write a Python function for Sum of cubes of first n natural numbers
def sumOfSeries(n): 
    sum = 0
    for i in range(1, n+1): 
        sum +=i*i*i        
    return sum
n = 5
print(sumOfSeries(n)) 


#write a Python function for list rotation
def leftRotate(arr, d, n): 
    for i in range(d): 
        temp = arr[0] 
        for i in range(n-1): 
            arr[i] = arr[i+1] 
        arr[n-1] = temp 

arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
for i in range(7): 
    print ("%d"% arr[i],end=" ")  


# write a python program to Check if given list is Monotonic 
def isMonotonic(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
A = [6, 5, 4, 4] 
print(isMonotonic(A)) 


# write a Python Program to find largest element in a list
def largest(arr,n): 
    max = arr[0] 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
arr = [10, 324, 45, 90, 9808] 
n = len(arr) 
Ans = largest(arr,n) 
print ("Largest in given array is",Ans) 


#write a python program for tuple multiplication
test_tup1 = (10, 4, 5, 6) 
test_tup2 = (5, 6, 7, 5) 
print("The original tuple 1 : " + str(test_tup1)) 
print("The original tuple 2 : " + str(test_tup2)) 
res = tuple(ele1 * ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 
print("The multiplied tuple : " + str(res)) 


#write a python program for Tuple list cross multiplication
test_list1 = [(2, 4), (6, 7), (5, 1)] 
test_list2 = [(5, 4), (8, 10), (8, 14)] 
print("The original list 1 : " + str(test_list1)) 
print("The original list 2 : " + str(test_list2)) 
res = [(x[0] * y[0], x[1] * y[1]) for x, y in zip(test_list1, test_list2)] 
print("The multiplication across lists is : " + str(res)) 
