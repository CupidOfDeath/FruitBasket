
#This program assumes that the user has installed geckodriver in the same path as that in which the program is saved

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller

key_word = input("Enter the desired string to be searched: ")
scope = input("Press G if you would like to google the string and Y if you'd like to search it up on YouTube: ")
keyboard = Controller()

if scope.upper() == 'Y':
	driver = webdriver.Firefox(executable_path = './geckodriver')
	driver.get('http:www.youtube.com')
	searchbar = driver.find_element_by_id('search-input')
	searchbar.click()
	keyboard.type(key_word)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

elif scope.upper() == 'G':
	driver = webdriver.Firefox(executable_path = './geckodriver')
	driver.get('http:www.google.com')
	keyboard.type(key_word)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

else:
	print('Invalid Command!')
