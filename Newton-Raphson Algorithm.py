#Finding the cube root of a given number using Newton-Raphson algorithm

x = int(input('Enter the number which you want to find the square root of: '))
epsilon = 0.01
g = x / 2
n = 0

while abs(g*g-x) >= epsilon:
	g = (g-(g*g-x)/(2*g))
	n += 1

print('The square root of', x, 'is', g)
print('The number of computations it took is', n)
