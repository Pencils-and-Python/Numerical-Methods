""" 
Summary:
--------
Program takes an input integer and determines if the number is a prime number.

pseudo code:
------------
input statement as an integer
function to determine if an input is prime.  See parameters.
    Eliminating small cases (n < 2 is not prime, 2 and 3 are prime).
    Checking divisibility by 2 and 3 (since they are the smallest primes).
    Checking divisibility from 5 to √n, skipping even numbers.

Parameters:
-----------
Key Properties of Prime Numbers

    The smallest prime number is 2.
    2 is the only even prime number (all other even numbers are divisible by 2 and are not prime).
    All prime numbers except 2 and 3 can be expressed in the form 6k ± 1, where k is an integer.
    The number 1 is NOT a prime number, because it has only one factor (itself).
    A number n is prime if it is not divisible by any number from 2 to √n.

Examples:
---------
>>> Prime numbers ≤ 20:
2, 3, 5, 7, 11, 13, 17, 19

>>> Composite numbers (not prime) ≤ 20:
4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20
"""

number_input = int(input("Enter an integer (no decimals) to see if the number is a prime: "))

def is_prime(number):
    """Determines if the argument is a prime number"""
    
    try:
        for num in range(2,number,1):
            if number % num == 0:
                not_prime = number
                result = not
                return not_prime
            else:
                prime = number
                return prime
        if number == 3 or number == 2:
            print(f'The number, {number}, is a prime number.')
        
        
        
    except Exception as e:
        print(f'An error occurred: {e}')

is_prime(number_input)
        
        

