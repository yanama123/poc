"""The myMath-Module adds mathematic features that are not included in the module math"""
from math import *
import cmath

inf = float('inf')

def gcd_two(a, b): #This function calculates the greatest common divisior of two numbers with Euclid's algorithm
    if min(a, b) == 0:
        return max(a, b)
    else:
        return lcd_two(max(a, b) % min(a, b), min(a, b))

def gcd(*args): #This function calculates the greatest common divisior of any count of numbers with the function lcd_two
    savedvalue = 0
    for number in args:
        savedvalue = lcd_two(savedvalue, number)
    return savedvalue

def lcm_two(a, b): #This function calculates the least common multiple of two numbers with the function gcd_two
    return a * b / gcd_two(a, b)

def lcm(*args): #This function calculates the least common multiple of any count of numbers with the function lcm_two
    savedvalue = 1
    for number in args:
        savedvalue = gcd_two(savedvalue, number)
    return savedvalue

def isprime(n): #This function tests if a number is a prime
    testlist = [2] + list(range(3, floor(sqrt(n)) + 1, 2))
    for testnumber in testlist:
        if n % testnumber == 0:
            return False
    return True

def primessmaller(n): #This function returns all primes smaller than the argument (Runs shorter than test every odd number with isprime!)
    primes = [2] #The found primes
    testnow = 3 #The number to test
    while testnow < n:
        testnumbers = [prime for prime in primes if prime <= sqrt(testnow)]
        divisorfound = False
        for testnumber in testnumbers:
            if testnow % testnumber == 0:
                divisorfound = True
                break
        if not divisorfound:
            primes.append(testnow)
        testnow = testnow + 2
    return primes

def firstprimes(n): #This function returns the first n primes
    primes = [2] #The found primes
    testnow = 3 #The number to test
    while len(primes)<n:
        testnumbers = [prime for prime in primes if prime <= sqrt(testnow)] #The possible divisors
        divisorfound = False
        for testnumber in testnumbers:
            if testnow % testnumber == 0:
                divisorfound = True
                break
        if not divisorfound:
            primes.append(testnow)
        testnow = testnow + 2
    return primes
