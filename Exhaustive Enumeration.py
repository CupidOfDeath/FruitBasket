#Finding the square root of a number using exhaustive enumeration

x = int(input('Enter the number which you want to find the square root of: '))
g = 0.0
epsilon = 0.01
step = 0.1
n = 0

while abs(g*g-x) > epsilon:
	g += step
	n += 1

print('The square root of', x, 'is', g)
print('The number of computations it took is', n)
