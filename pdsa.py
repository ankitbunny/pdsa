# -*- coding: utf-8 -*-
"""pdsa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ovJo4-h8BYJl2blPaeRkzVomf_1Ca80i

#Important notes

int() function can only convert strings that represent whole numbers, not numbers with decimal points.
"""

a = '3.1'
int(float(a))
int(a)

print(type((1,)), type((1)))

"""## note when there is a division operation
make code to handle Indeterminate form : x/0 || infi/infi

# Programm run
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

"""# Print"""

a = [1,2,3]
print ("Second element = %d" %(a[1]))

"""## Math"""

import math
x = 10
math.sqrt(x)

"""modular operator"""

print(1 // 2)
print(0 // 2)
print(3 // 2)

"""# even Odd number"""

import math
def is_prime(x):
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

"""only even digits"""

def check (n):
  while n != 0:
    d = n % 10
    if d % 2 != 1:
      return False
    n = n // 10
  return True

"""# Prime numbers

### create list of all prime factors of a number
"""

def factors(n):
  out = []  # output data type
  for i in range(1, n + 1): # 'n + 1' to include i = n also as range only goes one below the parameter provided
    if n % i == 0:  # min number to start checking div is 1 -> start range from 1 | lower bound of range function
      out.append(i) # appending to output data type | method of list
  return out

"""### is a number Prime ?"""

def is_prime(n):
  return factors(n) == [1, n]

def is_prime(n):
  return len(factors(n)) == 2

def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

def is_prime(n):
  result, i = True, 2
  while result and i < n:
    if n % i == 0:
      result = False
    i += 1
  return result

# GPT
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:  # If n is less than or equal to 1, it's not prime
        return False
    if n <= 3:  # If n is 2 or 3, it's prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # If n is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # Check potential divisors up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # If n is divisible by i or (i + 2), it's not prime
            return False
        i += 6
    return True

"""## _
- if "a" is a factor of a number then there should also exist "b" such that a*b = number
- one of a,b should be <= square_root of number and other >= square root of number

"""

import math
def is_prime(n):
  for i in range(2, int(math.sqrt(n)) + 1): # int(9.7) = 9
    if n % i == 0:
      return False
  return True

is_prime(11)

"""### Geting all Prime number upto 100"""

def prime_upto_100():
  out = []
  for i in range(1, 101):
    if is_prime(i):
      out.append(i)
  return out
print(prime_upto_100())

"""## finding first n primes"""

def first_n_prime(n):
  prime_counter, out, i  = 0, [], 2 # 2 is smallest prime
  while prime_counter != n:
    if is_prime(i):
      out.append(i)
      prime_counter += 1
    i += 1
  return out
print(first_n_prime(15))

def first_n_prime(n):
  prime_counter, out, i  = 0, [], 2 # 2 is smallest prime
  while prime_counter != n: # use < or > as it insures that the loop terminates
    if is_prime(i):
      out, prime_counter = out + [i], prime_counter + 1
    i += 1
  return out
print(first_n_prime(15))

"""## What are the difference observed between consiquitive prime numbers that occur between 1 and n
- difference: frequency
"""

def prime_freq(n):
  diff_freq = {} # dict declaration
  last_prime = 2
  for i in range(3, n + 1):
    if is_prime(i):
      new_prime = i
      try:  # alternate :: if d in diff_freq.keys()
        diff_freq[new_prime - last_prime] += 1
      except:
        diff_freq[new_prime - last_prime] = 1
      last_prime = i
  return diff_freq

print(prime_freq(50))

"""# Plot Sine curve"""

import matplotlib.pyplot as plt
import numpy as np
# Data for plotting
t = np.arange (0.0, 2.0, 0.01)
s = 1 + np.cos(2 * np.pi * t)
fig, ax = plt.subplots ()
ax.plot (t, s)
plt.show()

"""GCD(m,n)"""

m = 2
n = 4
print(": ",m,n)
m, n = max(m,n), min(m,n) # Switching m, n to contain max and min value
print(": ",m,n)

"""# Finding GCD of two numbers

1 is always a common factor
"""

def gcd(x,y):
  for i in range(min(x,y), 0, -1): # it has to be smaller then or = to min
    if x % i == 0 and y % i == 0:
      return i

def gcd(m,n):
  m, n = max(m,n), min(m,n)
  if m % n == 0 :
    return n
  return gcd(n, m - n)

def gcd(m,n):
  assert m > 0 and n > 0, 'entered numbers are not greater then zero'
  assert type(m) == type(1) and type(n) == type(1), "entered number are not intigers"
  m, n = max(m,n), min(m,n)
  if m % n == 0 :
    return n
  return gcd(n, m % n)

print(gcd(8,5))
print(gcd(8,16))

print(gcd(0,0))

print(gcd(1.2,2))

5%4

"""# Exceptions"""

x, z = 1, 0
try:
  x/ z
except ZeroDivisionError:
  print("Zero in Denominator in z")

try:
  y = int("abc")
except ValueError:
  print("not a valid number")

try:
  y = 5*d
except NameError:
  print("declare d")

try:
  l = [1,2,3]
  l[4]
except IndexError:
  print("Index out of range")

d = {'a': 1, 'b': 2}
print(d['a'])
try:
  d['c']
except KeyError:
  print("define key c")

read from unexisting file

writing to a file but disk is full

try:
    # Input: Get two numbers from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Division: Attempt to divide num1 by num2
    result = num1 / num2

except ZeroDivisionError:
    # Handle division by zero
    print("Error: Division by zero is not allowed.")
except ValueError:
    # Handle invalid input (e.g., non-integer input)
    print("Error: Invalid input. Please enter valid integers.")
except Exception as e:
    # Handle any other unexpected exceptions and log the details
    print(f"An unexpected error occurred: {e}")
else:
    # Code to run when there are no exceptions
    print(f"The result of {num1} divided by {num2} is {result:.2f}")
finally:
    # Cleanup code or other operations that always need to run
    print("Thank you for using this program.")

"""# Dictionary"""

score = {}
scores = {'sher' : 1, 'pub': 2}
print(f'{score}: {scores}')

"""# Classes & Objects

Class:
- Template of User Defined Data Type
 - data Storage| Properties | Data Members
    - implementation
      - private
 - public function manuplation of data | Behaviour
    - Specifation
      - Public

Object:
- Instance of template

##**why use return statement in __str__()**
"""

class Point:
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y
  def __str__(self):
    print(f'({self.x}, {self.y})')
b = Point(3,4)
print(b)

"""without using print statement cannot call representation of a instance, but using print in __str__ does not return a value as string hence error.

Print can only print string even numbers are converted to string then printed
"""

print(1)

"""## Adding Attribute linked to a instance is feasible even if it is not included in ***Class Defination***"""

class temp:
  def __init__(self, a, b):
    self.a, self.b = a, b

a = temp(1,2)
print(a.a, ":", a.b)
print("..")
a.c = 123
print(a.c)

class Point:
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y
  def __str__(self):
    return f'({self.x}, {self.y})'  # without self.x, self.y it give wrong values
a = str(Point(1,2))
b = Point(3,4)
print(a)
print(b)

"""## Point Class"""

# Cartesian
class Point:
  def __init__(self, x = 0, y = 0): # constructor Function
    self.x = x
    self.y = y
  def __str__(self):  #Convert Object to String # invoked by print statement
    return f'({self.x}, {self.y})'
  def translate(self, delta_x, delta_y):
    self.x = self.x + delta_x # or self.x += delta_x
    self.y = self.y + delta_y
    return self # now when ever we use object_name.transfate() then it will always return the updated object
  def distance_origin(self):
    import math
    return math.sqrt((self.x ** 2) + (self.y ** 2))
  #________________________
  # overload operator addition
  # __add__
  # __mult__
  # __lt__ <
  # __ge__ >=
  def __add__(self, a):
    return Point(self.x + a.x, self.y + a.y)

# Polar
class Point:
  def __init__(self, x = 0, y = 0):
    import math
    self.r = math.sqrt((x ** 2) + (y ** 2))
    self.theta = math.atan(y/x) if x != 0 else 0
  def distance_origin(self):
    return self.r
  def translate(self, delta_x, delta_y):
    import math
    new_x = delta_x + (self.r * math.cos(self.theta))
    new_y = delta_y + (self.r * math.sin(self.theta))
    self.r = math.sqrt((new_x * new_x) + (new_y * new_y))
    self.theta = math.atan(new_y / new_x) if new_x != 0 else 0
    return Point(new_x, new_y)
  def __str__(self):
    import math
    return f'({math.cos(self.theta) * self.r}, {math.sin(self.theta) * self.r})'
  def __add__(self, x):
    import math
    new_x = (x.r * math.cos(x.theta)) + (self.r * math.cos(self.theta))
    new_y = (x.r * math.sin(x.theta)) + (self.r * math.sin(self.theta))
    return Point(new_x, new_y)

a = Point(3,4)
b = Point(2,8)
#print(f'a.theta = {a.theta}')
print(a, b, ":", a+b)
print(f'{a} tralnslated by (2,2) is {a.translate(2,2)}')
print("...")
c = a.translate(3,3)
print(c)
print(a.distance_origin())  # need to use function"()" without it it will be different ....

"""# Counters in class"""

class temp:
  c_class = 0
  def __init__(self, a):
    temp.c_class += 1
    self.a = a
  def __str__(self):
    return f'a: {self.a}'

a = temp(1)
print(a.a)
b = temp(9)
print(b.a)

"""# Run time Checking"""

import time
a = time.perf_counter() # performance counter
for _ in range(10000):  # some code
  pass
b = time.perf_counter()
print(b-a)  # default unit is Second

class timer:
  import time
  def __init__(self):
    self.start = 0
    self.stop = 0
    self.elapsed =

"""# Analysis

## not considered : Function calls
## Considered: Comparisions & assigments
"""

4//2

"""#Searching

## Binary Search
"""

def binary_search(l, x):
  if len(l) == 0:
    return False
  n = len(l) // 2
  if l[n] == x:
    return True
  elif l[n] < x:
    return binary_search(l[n + 1:], x)
  else:
    return binary_search(l[:n], x)

# ???
def binary_search(l,x):
  i, j = 0, len(l) - 1
  while i <= j:
    m = (j + i) // 2
    if l[m] == x:
      return True
    if l[m] < x:
      i = m
    else:
      j = m
  return False

def binary_search(arr, target):
    # Initialize low and high pointers
    low, high = 0, len(arr) - 1

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2

        if arr[mid] == target:
            # Element found
            return True
        elif arr[mid] < target:
            # Adjust the low pointer to search in the right half
            low = mid + 1
        else:
            # Adjust the high pointer to search in the left half
            high = mid - 1

    # Element not found
    return False

l = [1,2,3,4,5,7,8,9,10]
binary_search(l, 1)

# Basic Test Cases
assert binary_search([1, 2, 3, 4, 5], 3) == True
assert binary_search([1, 2, 3, 4, 5], 6) == False

# Edge Cases
assert binary_search([], 42) == False
assert binary_search([42], 42) == True
assert binary_search([42, 43], 42) == True
assert binary_search([42, 43], 43) == True

# Lists with Repeated Elements
assert binary_search([1, 2, 2, 3, 4, 5], 2) == True
assert binary_search([1, 2, 2, 3, 4, 5], 6) == False

# Lists with Negative Numbers
assert binary_search([-5, -3, -1, 0, 2, 4], -3) == True
assert binary_search([-5, -3, -1, 0, 2, 4], 1) == False

# Large Lists
assert binary_search(list(range(1, 1000001)), 500000) == True
assert binary_search(list(range(1, 1000001)), 0) == False

"""# Sorting

## Selection Sort

select the min/max element from current list(by shrinking it) and append it to newly created list
"""

def min_index(l):
    min_value, min_values_index = l[0],0
    for i in range(len(l)):
      if l[i] < min_value:
        min_value, min_values_index = l[i], i
    return min_values_index

def selection_sort(l):
  out = []
  while len(l) > 0:
    split_point = min_index(l)
    out.append(l[split_point])
    l = l[:split_point] + l[split_point + 1 :] # if split_point != len(l) else l[:split_point]
  return out

def selection_sort(l):
  i, limit = -1, len(l)
  while i < limit - 1:
    min_index = i + 1
    for j in range(i+1, limit):
      if l[j] < l[min_index]:
        min_index = j
    l[i+1], l[min_index] = l[min_index], l[i+1]
    i += 1
  return l

print(selection_sort([5, 2, 9, 3, 6]))

# Basic Test Cases
assert selection_sort([5, 2, 9, 3, 6]) == [2, 3, 5, 6, 9]
assert selection_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
assert selection_sort([9, 6, 3, 2, 1]) == [1, 2, 3, 6, 9]

# Edge Cases
assert selection_sort([]) == []
assert selection_sort([42]) == [42]

# List Sorted in Descending Order
assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert selection_sort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]

# List with Duplicate Elements
assert selection_sort([5, 2, 5, 2, 6, 6]) == [2, 2, 5, 5, 6, 6]
assert selection_sort([3, 3, 3, 2, 1, 3, 2]) == [1, 2, 2, 3, 3, 3, 3]

# List with Negative Numbers
assert selection_sort([-5, -2, -9, -3, -6]) == [-9, -6, -5, -3, -2]
assert selection_sort([-3, -3, -3, -3, -3]) == [-3, -3, -3, -3, -3]
assert selection_sort([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]


print("Sucess")

"""Critical Corner points"""

l = [0,1,2,3,4,5]
print(l, ":",len(l))
print("l[:0]:", l[:0])
print("l[:1]:", l[:1])
print("l[5:]:", l[5:])
print("l[5+1:]:", l[5+1:])
print("l[10:]:", l[10:])


for i in range(0,0):
  print("i: ",i)

for j in range(2,0):
  print("j: ",j)


for k in range(2,0, -1):
  print("k: ",k)

"""in List sorting"""

def selection_sort(l):
  i = 0
  while i < len(l):
    j = min_index(l[i:]) + i
    l[i], l[j] = l[j], l[i]
    i += 1
  return l

l = [2,1,3,2,4,5,2,3,5,1]
selection_sort(l)
print(l)

"""## Insertion Sort

Decreasing order
"""

def correct_insert(l, x):
  inserted = False
  for i in range(len(l)):
   if l[i] < x:
     inserted = True
     return l[:i] + [x] + l[i:]
  if inserted == False:
    return [x] + l[:]

"""Increasing Order"""

def correct_insert(l,x):
  inserted = False

def i_sort(l):
  out = []
  for i in l:
    out = correct_insert(out, i)
  return out

def i_sort(l):
  for index_of_element_to_insert in range(len(l)):
    reverse_index = index_of_element_to_insert - 1
    while reverse_index >= 0:
      if l[index_of_element_to_insert] < l[reverse_index]:
        l[index_of_element_to_insert], l[reverse_index] = l[reverse_index], l[index_of_element_to_insert]
        reverse_index -= 1
        index_of_element_to_insert -= 1
      else:
        break
  return l

l = [5, 2, 9, 3, 6]
print(i_sort(l))

# Basic Test Cases
assert i_sort([5, 2, 9, 3, 6]) == [2, 3, 5, 6, 9]
assert i_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
assert i_sort([9, 6, 3, 2, 1]) == [1, 2, 3, 6, 9]

# Edge Cases
assert i_sort([]) == []
assert i_sort([42]) == [42]

# List Sorted in Descending Order
assert i_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert i_sort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]

# List with Duplicate Elements
assert i_sort([5, 2, 5, 2, 6, 6]) == [2, 2, 5, 5, 6, 6]
assert i_sort([3, 3, 3, 2, 1, 3, 2]) == [1, 2, 2, 3, 3, 3, 3]

# List with Negative Numbers
assert i_sort([-5, -2, -9, -3, -6]) == [-9, -6, -5, -3, -2]
assert i_sort([-3, -3, -3, -3, -3]) == [-3, -3, -3, -3, -3]
assert i_sort([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]


print("Sucess")

"""## Merge Sort"""

def merge(l, m):
  """
  O(m+n)
  """
  out = []
  i, j = 0,0
  while i < len(l) and j < len(m):
    if l[i] < m[j]:
      out.append(l[i])
      i += 1
    else:
      out.append(m[j])
      j += 1
  if i < len(l):
    out += l[i:]
  else:
    out += m[j:]
  return out

def m_sort(l):
  """
  O(n * log(n)) # n from O(m+n) of merge step
  """
  if len(l) > 1:
    mid_point = len(l) // 2
    l = merge(m_sort(l[:mid_point]), m_sort(l[mid_point:]))
  return l

l = [5, 2, 9, 3, 6]
print(m_sort(l))

# Basic Test Cases
assert m_sort([5, 2, 9, 3, 6]) == [2, 3, 5, 6, 9]
assert m_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
assert m_sort([9, 6, 3, 2, 1]) == [1, 2, 3, 6, 9]

# Edge Cases
assert m_sort([]) == []
assert m_sort([42]) == [42]

# List Sorted in Descending Order
assert m_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert m_sort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]

# List with Duplicate Elements
assert m_sort([5, 2, 5, 2, 6, 6]) == [2, 2, 5, 5, 6, 6]
assert m_sort([3, 3, 3, 2, 1, 3, 2]) == [1, 2, 2, 3, 3, 3, 3]

# List with Negative Numbers
assert m_sort([-5, -2, -9, -3, -6]) == [-9, -6, -5, -3, -2]
assert m_sort([-3, -3, -3, -3, -3]) == [-3, -3, -3, -3, -3]
assert m_sort([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]


print("Sucess")

"""## Quick Sort"""

def devider(l, pivot):
  lower, upper = [], []
  for i in l:
    if i < pivot:
      lower.append(i)
    else:
      upper.append(i)
  return (lower, upper[1:])

def q_sort(l):
  if len(l) > 1:
    pivot = l[0]
    lower, upper = devider(l, pivot)
    if len(lower) > 1:
      lower = q_sort(lower)
    if len(upper) > 1:
      upper = q_sort(upper)
    l = lower + [pivot] + upper
  return l

"""### in place Quick Sort"""

def rearrage(l, lower = 0, upper = -1):
  pivot = l[lower]
  if upper == -1:
    upper = len(l) - 1
  for i in range(lower + 1, upper + 1):
    if l[i] < pivot:

def q_sort(l, lower = 0, upper = -1):

l = [5, 2, 9, 3, 6]
print(q_sort(l))

# Basic Test Cases
assert q_sort([5, 2, 9, 3, 6]) == [2, 3, 5, 6, 9]
assert q_sort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
assert q_sort([9, 6, 3, 2, 1]) == [1, 2, 3, 6, 9]

# Edge Cases
assert q_sort([]) == []
assert q_sort([42]) == [42]

# List Sorted in Descending Order
assert q_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert q_sort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]

# List with Duplicate Elements
assert q_sort([5, 2, 5, 2, 6, 6]) == [2, 2, 5, 5, 6, 6]
assert q_sort([3, 3, 3, 2, 1, 3, 2]) == [1, 2, 2, 3, 3, 3, 3]

# List with Negative Numbers
assert q_sort([-5, -2, -9, -3, -6]) == [-9, -6, -5, -3, -2]
assert q_sort([-3, -3, -3, -3, -3]) == [-3, -3, -3, -3, -3]
assert q_sort([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]


print("Sucess")

"""#List

why use l[-1:] | it returns a list containg last element only(slice of list in form of list)
"""

l = [1,2,4]
print(l[-1])
l[-1:]

"""last index is skipped when slicing by index"""

l = [0,1,2]
print(l[-1], l[:1], l[:-1])

"""Copy of L is passed to any function"""

l = [4,1,2]
def c(l):
  return l[-1:] + l[:-1]
print(c(l), l)

"""Updating a list with its sorted version || Inplace sorting"""

l.sort()
print(l)

"""geting a sorted version under a new name"""

l = [2,1,4]
l1 = sorted(l)
print(l, l1)

"""pop"""

l = [1,2,3,4]
print(l)
x = l.pop()
print(l)
print(x)

l = [1,2,3,4]
print(l)
l.pop(0)
print(l)

l = [1,2,3,4]
print(l)
del l[-1]
print(l)

"""insert"""

l = [1,2,3]
print(l)
l.insert(4)

l = [1,2,3]
print(l)
l.insert(0,4)
print(l)

l = {'a':0, 'b' :1}
print(l)
if l['a']:
  print("a")
if l['b']:
  print("b")

"""# Linked List

## Forward Only
"""

class linked_list:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next
  def is_empty(self):
    return True if self.value == None else False
  def append(self, value):
    if self.next != None:
      temp = self
      while temp.next != None:
        temp = temp.next
      temp.next = linked_list(value = value)
    else:

  def insert(self, value):

  def delete(self, value):

class Node_pointer_value_pointer:
  def __init__(self, previous = None, value = None, next = None):
    self.previous = previous
    self.value = value
    self.next = next

"""## Two Way"""



"""# Queue"""

l = [1,2,3]
print(l.pop(1))  # returns mentioned element by default last
l

class Queue:
  def __init__(self):
    self.queue = []
  def enqueue(self, element):
    self.queue.append(element)
  def is_empty(self):
    return len(self.queue) == 0
  def dequeue(self):
    if self.is_empty():
      return "Queue is empty"
    else:
      return self.queue.pop(0)
  def __str__(self):
    return str(self.queue)

q = Queue()
print(q)
q.enqueue(1)
q.enqueue(2)
print(q)
print(q.dequeue())
print(q)
q.dequeue()
print(q)

import unittest

class TestQueueMethods(unittest.TestCase):
    def test_enqueue(self):
        test_queue = Queue()
        test_queue.enqueue(5)
        self.assertEqual(str(test_queue), "[5]")  # Test if element is correctly enqueued

    def test_dequeue(self):
        test_queue = Queue()
        test_queue.enqueue(5)
        test_queue.enqueue(10)
        dequeued_element = test_queue.dequeue()
        self.assertEqual(dequeued_element, 5)  # Test if correct element is dequeued
        self.assertEqual(str(test_queue), "[10]")  # Test if queue is modified after dequeue

    def test_is_empty(self):
        test_queue = Queue()
        self.assertEqual(test_queue.is_empty(), True)  # Test if queue is initially empty
        test_queue.enqueue(7)
        self.assertEqual(test_queue.is_empty(), False)  # Test if queue is not empty after enqueue

    def test_dequeue_from_empty_queue(self):
        test_queue = Queue()
        dequeued_element = test_queue.dequeue()
        self.assertEqual(dequeued_element, "Queue is empty")  # Test dequeue from an empty queue

# Run the tests
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueueMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

"""# Stack"""

class Stack:
  def __init__(self):
    self.stack = []
  def push(self, element):
    self.stack.append(element)
  def size(self):
    return len(self.stack)
  def is_empty(self):
    return self.size() == 0
  def pop(self):
    if self.is_empty():
      return "Stack is empty"
    return self.stack.pop()
  def peek(self):
    if self.is_empty():
      return "Stack is empty"
    return self.stack[-1]
  def __str__(self):
    return str(self.stack)

import unittest

class TestStackMethods(unittest.TestCase):
    def test_push(self):
        test_stack = Stack()
        test_stack.push(5)
        self.assertEqual(str(test_stack), "[5]")  # Test if element is correctly pushed onto the stack

    def test_pop(self):
        test_stack = Stack()
        test_stack.push(5)
        test_stack.push(10)
        popped_element = test_stack.pop()
        self.assertEqual(popped_element, 10)  # Test if the correct element is popped
        self.assertEqual(str(test_stack), "[5]")  # Test if stack is modified after pop

    def test_is_empty(self):
        test_stack = Stack()
        self.assertEqual(test_stack.is_empty(), True)  # Test if stack is initially empty
        test_stack.push(7)
        self.assertEqual(test_stack.is_empty(), False)  # Test if stack is not empty after push

    def test_peek(self):
        test_stack = Stack()
        test_stack.push(8)
        test_stack.push(3)
        self.assertEqual(test_stack.peek(), 3)  # Test if peek returns the top element correctly
        self.assertEqual(test_stack.size(), 2)  # Test if size remains unchanged after peek

    def test_pop_from_empty_stack(self):
        test_stack = Stack()
        popped_element = test_stack.pop()
        self.assertEqual(popped_element, "Stack is empty")  # Test pop from an empty stack

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStackMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

"""# Graph Algo

## inputed edges
"""

# Vertex [0 to 4] total range 5
edges = [(0,1), (0,2),
         (1,2), (1,3),
         (2,3), (2,4),
         (3,4), (3,3)]

"""## making Matrix to represent a graph"""

import numpy as np
def edges_to_matrix(edges = [(0,1), (0,2), (1,2), (1,3), (2,3), (2,4), (3,4), (3,3)]):
  maximum = -1
  for i, j in edges:
    if i > maximum:
      maximum = i
    if j > maximum:
      maximum = j

  matrix = np.zeros(shape=(maximum+1, maximum+1))
  for i,j in edges:
    matrix[i][j] = 1
  return matrix


matrix = edges_to_matrix(edges)
print(matrix)

"""## making adjcency list to represent graph"""



"""## BFS"""

def bfs(matrix):
  """
  initialize a queue to hold the starting vertex



  """

"""## DFS

## DAG

## Weighted Graphs
"""