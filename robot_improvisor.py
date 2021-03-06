import pyttsx
import os
import sys
import requests
import re
from bs4 import BeautifulSoup
from gtts import gTTS
import os    



#url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get("https://en.wikipedia.org/wiki/George_Washington")

data = r.text

soup = BeautifulSoup(data, "html.parser")

body_div = soup.find('div', id='bodyContent')
nums = re.compile("[12][0-9]{3}")
period = re.compile("\.")
counter = 1
input_var = ''

def clean(string) :
    cleaned1 = re.sub(r'\W+', '', string)
    #cleaned2 = re.sub('[\[[0-9]?\]]', '', cleaned1)
    cleaned3 = re.sub("'", '', cleaned1)
    return re.sub(r'([^\s\w])+', '', string)

def say(string) :
	
	try:
		tts = gTTS(text=string, lang='en')
		tts.save(str(counter) + ".mp3")
		os.system("afplay -v 1 " + str(counter) + ".mp3")
		global input_var
		input_var = raw_input('Enter to continue or q to quit: ')
	except :
		print("error")
	return

for paragraph in body_div.find_all('p'):
	candidates = paragraph.get_text().split(".")
	for candidate in candidates:
		
		if len(clean(candidate)) > 50 and len(clean(candidate)) < 100 and input_var != 'q':
			say(clean(candidate))
		counter = counter + 1
    	
