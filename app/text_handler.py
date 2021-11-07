letter_combinations = ('ai', 'ay', 'aw', 'al', 'ei', 'ea', 'ey', 'ee', 'ew', 'eu', 'oo', 'oa', 'ou', 'ie', 'ch', 'ck',
							 'tht', 'bt', 'gh', 'dg', 'th', 'sh', 'gn', 'mb', 'mn', 'kn', 'wh', 'ng', 'ph', 'wr', 'qu', 'razdel')
def text_handler(text):

	text = text.lower()

	text_final = []


	for letter_comb in letter_combinations:
		if letter_comb in text:
			text = text.replace(letter_comb, '('+letter_comb+')')


	text = list(text)
	

	for letter in text:

		if letter == ' ': 
			text_final.append('space')
			continue
		elif letter == '.':
			text_final.append('point')
			continue	
		elif letter == ',':
			text_final.append('comma')
			continue	
		elif letter == '!':
			text_final.append('exmarc')
			continue	
		elif letter == '?':
			text_final.append('quemarc')
			continue
		elif letter == "'":
			text_final.append('covichka')	

		elif letter == '1':
			text_final.append('one')
			continue
		elif letter == '2':
			text_final.append('two')
			continue
		elif letter == '3':
			text_final.append('three')
			continue
		elif letter == '4':
			text_final.append('four')
			continue
		elif letter == '5':
			text_final.append('five')
			continue
		elif letter == '6':
			text_final.append('six')
			continue
		elif letter == '7':
			text_final.append('seven')
			continue
		elif letter == '8':
			text_final.append('eight')
			continue
		elif letter == '9':
			text_final.append('nine')
			continue
		elif letter == '0':
			text_final.append('zero')
			continue										

				


		elif letter == '(':	         	         								
			n = text.index(letter)   	        								  
			m = text.index(')')      	       								   
			text[n] = 'zwezd'            	       								    
			text[m] = 'zwezd'           	        								  
											
			srez = text[n:m]         	                                             
			srez.remove('zwezd')         	      							            	
			srez = ''.join(srez)     	                                        
			text_final.append(srez)
			text[n:m] = [' ']


		else:
			text_final.append(letter)
		text_final = list(filter(lambda s: s != 'zwezd', text_final))
	text_final.append('space')
	return text_final



if __name__ == '__main__':
	text = 'When people root qurazdel'
	print(text_handler(text))	