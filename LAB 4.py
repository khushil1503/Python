#Q.1 Print all alphabets in upper case and in lower case

for i in range(65, 91):
    print(chr(i), end=" ")
print()
for i in range(97, 123):
    print(chr(i), end=" ")

#Q.2 Print a multiplication table of a given number

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Q.3 Count no. of alphabets and no. of digits in any given string.

s = input("Enter a string: ")
alphabets = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
print(f"Alphabets: {alphabets}, Digits: {digits}")

#Q.4 Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n) == str(n**2)[-len(str(n)):]

num = int(input("Enter a number: "))
print(f"Prime: {is_prime(num)}")
print(f"Perfect: {is_perfect(num)}")
print(f"Armstrong: {is_armstrong(num)}")
print(f"Palidogram: {is_palidogram(num)}")
print(f"Automophic: {is_automrphic(num)}")

#Q.5 Generate all Pythagorean Triplets with side length <= 30

for a in range(1, 31):
    for b in range(a, 31):
        c = (a**2 + b**2) ** 0.5
        if c.is_integer() and c <= 30:
            print(f"({a}, {b}, {int(c)})")

#Q.6 Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.

for h in range(24):
    if h == 0:
        print("12 AM (Midnight)")
    elif h < 12:
        print(f"{h} AM")
    elif h == 12:
        print("12 PM (Noon)")
    else:
        print(f"{h - 12} PM")

#Q.7 Print nCr and nPr

from math import factorial

n = int(input("Enter n: "))
r = int(input("Enter r: "))

nCr = factorial(n) // (factorial(r) * factorial(n - r))
nPr = factorial(n) // factorial(n - r)

print(f"nCr: {nCr}")
print(f"nPr: {nPr}")


#Q.8 Print factorial of a given number.


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f"Factorial: {factorial(num)}")

#Q.9 Print N natural nos. in reverse

N = int(input("Enter N: "))
for i in range(N, 0, -1):
    print(i, end=" ")

#Q.10 Generate N numbers of Fibonacci series

N = int(input("Enter N: "))
a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b
#Q.11 Calculate sin(x); x is a radian value. The formula is as under:
sin    =    −
  
3
3!
+
  
5
5!
−
  
7
7!
…

(hint: degrees can be converted into radians by 3.14159 / 180.)

import math

x = float(input("Enter x in degrees: "))
x = x * (math.pi / 180) 

sin_x = 0
terms = 10 
for n in range(terms):
    term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    sin_x += term

print(f"sin({x}) ≈ {sin_x}")

