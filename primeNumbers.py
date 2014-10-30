import sys
import math


#########
#Tests whether a given number is prime or not.
#Returns true if it's a prime, false otherwise
#########
def is_prime(num):
	for j in range(2, num):
		#num % j would be 0 if j is a divisor of num, making num not a prime
		if((num % j) == 0):
			return False
	return True

#########
#Lists all prime numbers less than or equal to the given value.
#########
def list_primes(num):
	print 'All prime numbers less than' 
	print num 
	print 'are'
	for i in range(2, num+1):
		if(is_prime(i)):
			print i,

#########
#Main function that calls the other functions.
#########
def main():
	upperLimit = int(raw_input('Please enter a number you wish to find all prime numbers less than.'))
	list_primes(upperLimit)


main()
