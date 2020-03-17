#A typracer game!
#This program requires one to have a 'typetest.txt' named file in the same folder as that containing the script. 
#The 'typetext.txt' file is expected to have any number of texts seperated by a line for the code to work properly.

import time
import random

def text_generator():
	with open('typetest.txt', 'r') as r:
		stuff = r.readlines()
	
	x = random.randint(0, (int(len(stuff)) - 1))
	return stuff[x]

rep_num = 0
total_speed = 0
while True:
	n = 5
	text = text_generator()
	word_number = (int(text.count(' ')) + 1)

	print(text)

	for i in range(0,5):
		print(n-i)
		time.sleep(1)

	print('Go')
	start = time.time()
	user_in = input()
	end = time.time()

	l_user_in = user_in.split()
	l_text = text.split()

	error = 0
	invalid = False
	try:
		for index, item in enumerate(l_text):
			if l_text[index] != l_user_in[index]:
				error += 1

		wpm = (((word_number/(end-start))*60))
		wpm -= ((error/word_number)*wpm)
		total_speed += wpm
		rep_num += 1
		print(f'Your speed was {wpm} wpm and you made {error} errors!')

	except IndexError:
		print('You did not complete the text!')
	repeat = input('Would you like to go again?[y/n]: ')
	if repeat == 'n':
		break
	elif repeat == 'y':
		pass
	else:
		invalid = True
		break

if invalid:
	print('Invalid Input!')

try:
	avg_speed = total_speed / rep_num
	if rep_num == 1:
		flag = 'race'
	else:
		flag = 'races'
	print(f'Your average speed in the last {rep_num} {flag} was {avg_speed} wpm!')
	
except ZeroDivisionError:
	print('You did not complete any races!')

