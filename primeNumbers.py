import sys
import math


#########
#Class Prime_Numbers tests whether a given number is prime or not.
#Returns true if it's a prime, false otherwise
#########
class Prime_Number:


	def __init__(self):
		print("")

	def is_prime(self, num):
		for j in range(2, num):
			#num % j would be 0 if j is a divisor of num, making num not a prime
			if((num % j) == 0):
				return False
		return True

	#########
	#Lists all prime numbers less than or equal to the given value.
	#########
	def list_primes(self, num):
		print('All prime numbers less than')
		print(num)
		print('are')
		for i in range(2, num+1):
			if(self.is_prime(i)):
				print(i),

#########
#Main function that calls the other functions.
#########
def main():
	#prime is a Prime_Number object
	prime = Prime_Number()
	#getting the user input...
	upperLimit = int(input('Please enter a number you wish to find all prime numbers less than.'))
	#list all of the prime numbers less than or equal to the user input
	prime.list_primes(upperLimit)


main()
