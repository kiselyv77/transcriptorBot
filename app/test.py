text = 'rrr'
k = 'a'
def a(text):
	global k
	k = 'trans' + text

print(k)
a(text)
print(k)	
