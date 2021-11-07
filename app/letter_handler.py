from text_handler import *
from letters_func import *
from list_str import *
#text = 'spacWhen people ask me how I learned to speak German I tell them it was simpleai'

def letters_handler(text):
	text = text_handler(text)
	text_final_rus_list = []
	letter_index = -1
	for letr in text:
		letter_index = letter_index + 1
		text_final_rus_list.append(eval(letr + '_func(text, letter_index)'))
		text_final_rus = list_str(text_final_rus_list)
	return text_final_rus	

if __name__ == '__main__':
	print(letters_handler('spacWhen people ask me how I learned to speak German I tell them it was simpleai'))	

