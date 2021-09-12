# 1. print hello world!
print('Hello world!')

# 2.add two no.
x=2
y=3
print(x+y)

# 3. Sqrt by predefined libraries
import math
x=5
print(math.sqrt(x))

# 3. Sqrt by logical approach
x=5
s=x**0.5
print(s)

# 4. Area of triangle
a=5
b=4
c=3
s=(a+b+c)/2
a=s*(s-a)*(s-b)*(s-c)
a=a**0.5
print(a)

# 5. Solve Quadratic equation
# coefficient of x^2
a=2
# coefficient of x
b=5
# constant
c=-3
r1=(b**2)-4*a*c
r1=r1**0.5
r1-=b
r1/=(2*a)
r2=(b**2)-4*a*c
r2=r2**0.5
r2+=b
r2/=(2*a)
print('roots of quadratic eq. are ',r1,', ',-r2)

# 6. Swap two variables
x=4
y=45
t=x
x=y
y=t
print('after swapping x is ',x,' and y is ',y)

# 7. generate a random no.
import random
print(random.randint(0,100))

# 8. converts km to miles
k=1000
print('after converting km to mile the value is ',k*0.621371192)

# 9. convert celsius to fahrenheit
c=100
c*=(9/5)
print('after converting C to F the value is ',c+32)

# 10. check no. is +ve -ve or zero
x=0
if x<0:
    print('-ve number')
elif x>0:
    print('+ve number')
else:
    print('number is zero')

# 11. check odd or even
x=42
if x%2==0:
    print('even number')
else:
    print('odd number')

# 12. check leap year
x=2000
if x%4==0:
    if x%100==0:
        if x%400==0:
            print(x,' is Leap year')
        else:
            print(x,' is not a Leap year')
    else:
        print(x,' is Leap year')
else:
    print(x,' is not a Leap year')

# 13. largest among three no.
x=15
y=16
z=20
if x>=y and x>=z:
    print(x,' is largest')
elif y>=x and y>=z:
    print(y,' is largest')
else:
    print(z,' is largest')

# 14. check prime no.
x=13
for i in range(2,x):
    if x%i==0:
        print(x,' is not a prime no.')
        break;
if i==x-1:
    print(x,' is prime no.')

# 15. print prime no.
x=100
for i in range(2,x):
    c=0
    for j in range(2,i):
        c+=1
        if i%j==0:
            break
    if c==i-2:
        print(i,end=', ')

# 16. factorial program
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
x=5
print(f(x))

# 17. multiplication table
x=3
for i in range(1,11):
    print(x,'*',i,'=',x*i)

# 18. fibonacci series
x=10
def f(n):
    if n==0 or n==1:
        return n
    else:
        return f(n-1)+f(n-2)
for i in range(x):
    print(f(i),end=' ')

# 19. check armstrong no.
x=153
a=x
s=0
while a>=1:
    c=a%10
    c=int(c)
    s+=(c**3)
    a//=10
if s==x:
    print(x,' is a armstrong number')
else:
    print(x,' is not a armstrong number')

# 20. find armstrong no.
x=410
for i in range(1,x+1):
    a=i
    s=0
    while(a>=1):
        c = a % 10
        c = int(c)
        s += (c ** 3)
        a //= 10
    if s==i:
        print(i,end=', ')

# 21. sum of natural no.
x=int(input("enter a no."))
def sum(x):
    s=0
    for i in range(1,x+1):
        s+=i
    return s
print(sum(x))

# 22. display powers of 2 using anonymous function
x=10
for i in range(x):
    print('2 raised to power ',i,' is ',2**i)

# 23. find numbers divisible by another no.
list=[12,25,222,50,54,550,225]
x=25
l=[]
for i in list:
    if i%x==0:
        l.append(i)
print(l)

# 24. convert decimal to binary,octal,hexadecimal
n=int(input("enter a decimal no."))
def DtB(n):
    r=0
    x=1
    while n>0:
        y=n%2
        y=int(y)
        r+=(x*y)
        x*=10
        n/=2
    return r
def DtO(n):
    r=0
    x=1
    while n>0:
        y=n%8
        y=int(y)
        r+=(x*y)
        x*=10
        n/=8
    return r
print('Conversion of Decimal to Binary is ',DtB(n))
print('Conversion of Decimal to Octal is ',DtO(n))

# 25. Find ASCII value of characters
c='p'
print('the ASCII value of ',c,' is ',ord(c))

# 26. Find HCF or GCD
def hcf(x,y):
    if x > y:
        s = y
    else:
        s = x
    for i in range(1, s+1):
        if((x % i == 0) and (y % i == 0)):
            h = i
    return h
x = int(input("enter first number: "))
y = int(input("enter second number: "))
print("The H.C.F. is", hcf(x, y))

# 27. Find LCM
def lcm(x, y):
   if x > y:
       g = x
   else:
       g = y
   while(True):
       if((g % x == 0) and (g % y == 0)):
           l = g
           break
       g += 1
   return l
x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
print("The L.C.M. is", lcm(x, y))

# 28. Find the Factors of a number
x=int(input("enter the no. to calculate the factor: "))
print('The factors of ',x,' are:')
l=[]
for i in range(1,x+1):
    if x%i==0:
        l.append(i)
print(l)

# 29. Make a simple calculator
x=float(input("enter first no."))
y=float(input("enter second no."))
print('enter 1 if u want to add the numbers')
print('enter 2 if u want to subtract the numbers')
print('enter 3 if u want to multiply the numbers')
print('enter 4 if u want to divide the numbers')
ch=input("enter ur choice")
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
if ch=='1':
    print('addition of the numbers: ',add(x,y))
elif ch=='2':
    print('subtraction of the numbers: ',sub(x,y))
elif ch=='3':
    print('multiplication of the numbers: ',mul(x,y))
elif ch=='4':
    print('division of the numbers: ',div(x,y))
else:
    print('wrong choice entered')

# 30. To shuffle deck of cards
import itertools, random
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])

# 31. Display Calendar
import calendar
yy = int(input("enter the year in yyyy format: "))
mm = int(input("enter the month in mm format: "))
print(calendar.month(yy, mm))

# 32. fibonacci series using recursion
x=int(input("enter a number: "))
def f(n):
    if n==0 or n==1:
        return n
    else:
        return f(n-1)+f(n-2)
for i in range(x):
    print(f(i),end=' ')

# 33. sum of natural no. using recursion
x=int(input("enter a number: "))
def sum(x):
    s=0
    for i in range(1,x+1):
        s+=i
    return s
print(sum(x))

# 34. factorial program using recursion
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
x=int(input("enter a number: "))
print(f(x))

# 35. Convert Decimal to Binary using recursion
n=int(input("enter a decimal number: "))
def DtB(n):
    r=0
    x=1
    while n>0:
        y=n%2
        y=int(y)
        r+=(x*y)
        x*=10
        n/=2
    return r
print('Conversion of Decimal to Binary is ',DtB(n))

# 36. Add two matrices
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[7,8,9],
     [4,5,6,],
     [1,2,3]]
r = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        r[i][j] = X[i][j] + Y[i][j]
for i in r:
    print(i)

# 37. Transpose of a matrix
x = [[12,7],
    [4 ,5],
    [3 ,8]]
r = [[0,0,0],
         [0,0,0]]
for i in range(len(x)):
   for j in range(len(x[0])):
       r[j][i] = x[i][j]

for i in r:
   print(i)

# 38. Multiply two matrices
A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
r = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            r[i][j] += A[i][k] * B[k][j]
for i in r:
    print(i)

# 39. Check Palindrome
def isPalindrome(s):
    return s == s[::-1]
s = "naman"
a = isPalindrome(s)
if a:
    print(a," is palindrome")
else:
    print(a," is not palindrome")

# 40. Remove punctuations from a string
punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
s = "Hello!!!, he said ---and went."
no_p = ""
for c in s:
   if c not in punct:
       no_p = no_p + c
print(no_p)

# 41. Sort words in alphabetic order
s = "Hello this Is an Example With cased letters"
w = [word.lower() for word in s.split()]
w.sort()
print("The sorted words are:")
for word in w:
   print(word)

# 42. Illustrate different set operations
x = {1,3,5,7,9}
y = {1, 2, 3, 4, 5,6,7,8}
print("Union of x and y is",x | y)
print("Intersection of x and y is",x & y)
print("Difference of x and y is",x - y)
print("Symmetric difference of x and y is",x ^ y)

# 43. Count the number of each vowel
v = 'aeiou'
s = 'Hello, have you tried our tutorial section yet?'
s = s.casefold()
c = {}.fromkeys(v,0)
for char in s:
   if char in c:
       c[char] += 1
print(c)

# 44. Merge two dictionaries
def m(d1, d2):
    return (d2.update(d1))
d1 = {'a': 5, 'b': 6}
d2 = {'c': 7, 'd': 8}
print(m(d1, d2))
print(d2)

# 45. Find the size(resolution) of a image
def res(f):
   with open(f,'rb') as img:
       img.seek(163)
       a = img.read(2)
       h = (a[0] << 8) + a[1]
       a = img.read(2)
       w = (a[0] << 8) + a[1]
   print("The resolution of the image is",w,"x",h)
res("1.jpg")

# 46. Find hash of file
import hashlib

def hash_file(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()
message = hash_file("track1.mp3")
print(message)

# 47. Create pyramid patterns
for i in range(6):
    for j in range(i,6):
        print(' ',end='')
    for k in range(i+1):
        print('* ',end='')
    print('')

# 48.Merge two dictionaries
def m(d1, d2):
    return (d2.update(d1))
d1 = {'a': 5, 'b': 6}
d2 = {'c': 7, 'd': 8}
print(m(d1, d2))
print(d2)

# 49. Safely create a nested directory

# 50. Access index of a list using for loop
l = [8, 9, 7, 6]
for i, v in enumerate(l):
    print(i, v)

# 51. Make a Flattened list from nested list
l = [[1], [2, 3], [4, 5, 6, 7]]

li = [n for sl in l for n in sl]
print(li)

# 52. Slice lists
l = [5,4,3,2,1]
print(l[1:4])

# 53. Iterate over dictionaries using for loop
d = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for k, v in d.items():
    print(k, v)

# 54. sort a dictionary by value
d = {5:4, 1:6, 6:3}
sorted_d = {key: value for key, value in sorted(d.items(), key=lambda item: item[1])}
print(sorted_d)

# 55. Check if a list is empty
def check(l):
    if len(l) == 0:
        return 0
    else:
        return 1
l = []
if check(l):
    print("The list is not empty")
else:
    print("Empty List")

# 56. Catch multiply exceptions in one line
string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)

# 57. Copy a File
from shutil import copyfile
copyfile("/root/a.txt", "/root/b.txt")

# 58. Concatenate two lists
l1 = [1, 4, 5, 6, 5]
l2 = [3, 5, 7, 2, 5]
for i in l2:
    l1.append(i)
print("Concatenated list using naive method : " + str(l1))

# 59. Check if a key is already present in a dictionary
def checkKey(dict, key):
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")
dict = {'a': 100, 'b': 200, 'c': 300}
key = 'b'
checkKey(dict, key)
key = 'w'
checkKey(dict, key)

# 60. Split a list into evenly sized chunks
def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]
chunk_size = 2
my_list = [1,2,3,4,5,6,7,8,9]
print(list(split(my_list, chunk_size)))

# 61. Parse a string to a float or int
b_str = "1500"
b_int = int(b_str)
print(type(b_int))
print(b_int)

# 62. Print colored text to the terminal
print('\x1b[38;2;5;86;243m' + 'Abhi' + '\x1b[0m')

# 63. Convert string to datetime
import datetime
def convert(date_time):
    format = '%b %d %Y %I:%M%p'
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str
date_time = 'Dec 4 2018 10:07AM'
print(convert(date_time))

# 64. Get the last element of the list
test_list = [1, 4, 5, 6, 3, 5]
print("The original list is : " + str(test_list))
for i in range(0, len(test_list)):
    if i == (len(test_list) - 1):
        print("The last element of list using loop : "
              + str(test_list[i]))
test_list.reverse()
print("The last element of list using reverse : "
      + str(test_list[0]))

# 65. Get a substring of a string
my_string = "I love python."
print(my_string[2:6])
print(my_string[2:])
print(my_string[:-1])

# 67. Read a file line by line into a list
with open("data_file.txt") as f:
    content_list = f.readlines()
print(content_list)
content_list = [x.strip() for x in content_list]
print(content_list)

# 68. Randomly select an element from the list
import random
my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))

# 69. check if a string is a number(float)
def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False
a_string = "1.33"
is_valid_float = check_float(a_string)
print(is_valid_float)

# 70. Count the occurrence of an item in a list
a_list = ["a", "b", "a"]
occurrences = a_list.count("a")
print(occurrences)

# 71. Append to a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()

# 72. Delete an element from a dictionary
d = {'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary")
print(d)
key=input("Enter the key to delete(a-d):")
if key in d:
    del d[key]
else:
    print("Key not found!")
    exit(0)
print("Updated dictionary")
print(d)

# 73. Create a long multiline string
my_string = '''The only way to
learn to program is
by writing code.'''

print(my_string)

# 74. Extract extension from the file name
import os
file_name = 'my_file.txt'
print(os.path.splitext(file_name))

# 75. Measure the elapsed time
import time
start = time.time()
print(23*2.3)
end = time.time()
print(end - start)

# 76. Get the class name of an instance
class Vehicle:
    def name(self, name):
        return name
v = Vehicle()
print(type(v).__name__)

# 77. Convert two lists into a dictionary
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break
print ("Resultant dictionary is : " +  str(res))

# 78. Differentiate between type() and instance()
class Polygon:
    def sides_no(self):
        pass
class Triangle(Polygon):
    def area(self):
        pass
obj_polygon = Polygon()
obj_triangle = Triangle()
print(type(obj_triangle) == Triangle)   	# true
print(type(obj_triangle) == Polygon)    	# false
print(isinstance(obj_polygon, Polygon)) 	# true
print(isinstance(obj_triangle, Polygon))	# true

# 79. Trim whitespace from a string
my_string = " Python "
print(my_string.strip())

# 80. Get the file name from the file path
import os
file_name = os.path.basename('/root/file.ext')
print(os.path.splitext(file_name)[0])
