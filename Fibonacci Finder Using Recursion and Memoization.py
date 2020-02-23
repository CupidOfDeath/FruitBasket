#Importing os for 'Clear Screen' functionality
import os
#Importing time to add time.sleep functionality
import time
#A program to find out the nth term of the fibonacci sequence!
#Fibonacci sequence : 1, 1, 2, 3, 5, 8, 13, 21, 34,.........
#The default value of maximum recursion depth is 1000 and it hasn't been altered

#Defining clear() function


while True:
	fibonacci_cache = {}

	def fibonacci(n):
		if n in fibonacci_cache:
			return fibonacci_cache[n]
		elif n == 1:
			return 1
		elif n == 2:
			return 1
		else:
			value = fibonacci(n-1) + fibonacci(n-2)
			fibonacci_cache[n] = value
			return value

	n = int(input('Enter the desired nth term of the fibonacci squence: '))
	print('The '+str(n)+'th term of the fibonacci sequence is '+str(fibonacci(n)) )
	
	user_command = str(input("Do you want to go again? [y/n] \n"))
	if user_command.lower() == 'y':
		print('Okay! \n')
		time.sleep(0.2) #Sleep for 0.2 seconds, to display the Okay! text
		os.system('CLS' if os.name=='nt' else clear) #if the system is nt i.e. Windows, execute a 'CLS' else execute a 'clear'
	else:
		break
print('Bye!')
		
		
			


