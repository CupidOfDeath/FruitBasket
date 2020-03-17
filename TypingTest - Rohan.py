#A typracer game!
#This variation pulls out the first paragraph from a random article from Wikipedia(EN)

import time
import random
from bs4 import BeautifulSoup as bs
import requests as req
def text_generator():
	URL = "https://en.wikipedia.org/wiki/Special:Random"
	r = req.get(URL)
	soup = bs(r.content, 'html.parser')
	para = soup.find_all('p')
	i=0
	for i in range(len(para)):
		if para[i].text and para[i].text.strip():
			return(para[i].text)
			break



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
try:
	for index, item in enumerate(l_text):
		if l_text[index] != l_user_in[index]:
			error += 1

	wpm = round(((word_number/(end-start))*60) - error)
	print(f'Your speed was {wpm} wpm and you made {error} errors!')

except IndexError:
	print('You did not complete the text!')
