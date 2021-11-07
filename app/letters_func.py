glas = ('a', 'e', 'i', 'o', 'u', 'y')
soglas = ('b', 'c', 'd', 'f', 'g','h', 'j', 'k', 'l', 'm','n', 'p', 'q', 'r', 's','t', 'v', 'w', 'x', 'z')

def a_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if text[let_next] in soglas and text[let_next+1] in glas:
		return 'эй'
	elif text[let_next] == 'r':
		return 'а'
	return 'э' 	

def b_func(text, letter_index):
	return 'б'

def c_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if text[let_next] in ('e', 'i', 'y'):
		return 'с'
	return 'к'

def d_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if text[let_next] == 'space' and text[let_prev] == 'e':
		return 'т'
	return 'д'

def e_func(text, letter_index):
	if len(text) > 5:
		n = 3
	else:
		n = 3	
	let_next = letter_index+1
	let_prev = letter_index-1
	srez = text[letter_index-n:letter_index]	
	flag = 0
	for n in srez:
		if n in glas:
			flag += 1

	if text[let_prev] == 'y':
		return 'е'

	if text[let_next] in soglas and text[let_next+1]:
		return 'и'
		
	if text[let_next] == 'space' and flag == 0: 
		return 'и'
	elif flag>0:
		return ''

	return 'э'
	

def f_func(text, letter_index):
	return 'ф'

def g_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if text[let_next] in ('e', 'i', 'y'):
		return 'дж'
	return 'г'
	
def h_func(text, letter_index):
	return 'х'

def i_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if (text[let_next] in soglas and text[let_next+1] in soglas) or text[let_next] == 'space' or text[let_next+1] == 'e':
		return 'аи'
	return 'и'

def j_func(text, letter_index):
	return 'дж'

def k_func(text, letter_index):
	return 'к'

def l_func(text, letter_index):
	return 'л'

def m_func(text, letter_index):
	return 'м'

def n_func(text, letter_index):
	return 'н'

def o_func(text, letter_index):
	return 'о'

def p_func(text, letter_index):
	return 'п'

def q_func(text, letter_index):
	return 'ку'

def r_func(text, letter_index):
	return 'р'

def s_func(text, letter_index):
	return 'с'

def t_func(text, letter_index):
	return 'т'

def u_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if text[let_next] in soglas and text[let_next+1] in glas:
		return 'ю'
	elif text[let_next] in soglas:
		return 'а'
	return 'у'

def v_func(text, letter_index):
	return 'в'

def w_func(text, letter_index):
	return 'в'

def x_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if text[let_prev] in glas and text[let_next] in glas:
		'гз' 
	return 'кс'

def y_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if text[let_next] == 'space':
		return 'ай'
	elif text[let_prev] in soglas and text[let_next] in soglas and text[let_next+1] in soglas: 
		return 'ай'	
	elif text[let_prev] == 'space':
		return 'ю'
	return 'и'

def z_func(text, letter_index):
	return 'з'

def ai_func(text, letter_index):
	return 'эй'
def ay_func(text, letter_index):
	return 'эй'
def aw_func(text, letter_index):
	return 'oa'
def al_func(text, letter_index):
	return 'oa'	
def ei_func(text, letter_index):
	return 'еи'
def ea_func(text, letter_index):
	return 'еа'
def ey_func(text, letter_index):
	return 'еу'
def ee_func(text, letter_index):
	return 'ии'
def ew_func(text, letter_index):
	return 'ев'
def eu_func(text, letter_index):
	return 'еу'
def oo_func(text, letter_index):
	return 'уу'
def oa_func(text, letter_index):
	return 'оа'
def ou_func(text, letter_index):
	return 'оу'	
def ie_func(text, letter_index):
	return 'ие'

def ch_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if text[let_next] == 'oo' and text[let_next+1] == 'l':
		return 'к'
	return 'ч'

def ck_func(text, letter_index):
	return 'к'

def tht_func(text, letter_index):
	return 'тч'
def bt_func(text, letter_index):
	return 'бт'
def gh_func(text, letter_index):
	return 'гх'
def dg_func(text, letter_index):
	return 'дж'
def th_func(text, letter_index):
	let_next = letter_index+1
	let_prev = letter_index-1
	if text[let_prev] == 'space':
		return 'тз' 
	return 'ч'

def sh_func(text, letter_index):
	return 'сх'
def gn_func(text, letter_index):
	return 'гн'
def mb_func(text, letter_index):
	return 'мб'
def mn_func(text, letter_index):
	return 'мн'
def kn_func(text, letter_index):
	return 'кн'
def wh_func(text, letter_index):
	return 'вх'
def ng_func(text, letter_index):
	return 'нг'
def ph_func(text, letter_index):
	return 'пх'
def wr_func(text, letter_index):
	return 'вр'
def qu_func(text, letter_index):
	return 'кв'	


 
def space_func(text, letter_handler):
	return 'space'
def prefix_func(text, letter_handler):
	return 'prefix'	


def point_func(text, letter_index):
	return '.'
def comma_func(text, letter_index):
	return ','		
def exmarc_func(text, letter_index):
	return '!'		
def quemarc_func(text, letter_index):
	return '?'
def covichka_func(text, letter_index):
	return "'"
def razdel_func(text, letter_index):
	return '\n'	

def one_func(text, letter_index):
	return '1'
def two_func(text, letter_index):
	return '2'
def three_func(text, letter_index):
	return '3'
def four_func(text, letter_index):
	return '4'
def five_func(text, letter_index):
	return '5'
def six_func(text, letter_index):
	return '6'
def seven_func(text, letter_index):
	return '7'
def eight_func(text, letter_index):
	return '8'
def nine_func(text, letter_index):
	return '9'
def zero_func(text, letter_index):
	return '0'										
							


if __name__ == '__main__':
	print(y_func(['w','y','space'], 1))
			