import telebot
import config
from main import main
from dialog import mirror


def check_for_russian(string):
    alphabet = ['a','b', 'c', 'd', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '?', '.', ',', "'", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for one_char in string:
        if one_char in alphabet:
            return True
    return False


bot = telebot.TeleBot(config.TOKEN)


mode = 'trans'




@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Я бот который преобразует английский текст в русскую транскрипцию', parse_mode='html')
	

@bot.message_handler(commands=['trans'])
def tans(message):
	global mode
	mode = 'trans'
	

@bot.message_handler(commands=['dial'])
def dial(message):
	global mode
	mode = 'dial'


if mode == 'trans':	
	@bot.message_handler(content_types=['text'])
	def transkriptor(message):
		
		my_message = message.text.replace('\n', 'razdel')
		if check_for_russian(message.text.lower()) == False:
			final_message = 'Бля ну сказал же только английские заебал:|'	
		else:
			final_message = main(my_message)
			
		bot.send_message(message.chat.id, final_message, parse_mode='html')
		
			
elif mode == 'dial':
	@bot.message_handler(content_types=['text'])
	def dialog(message):
		final_message = mirror(message.text)
		bot.send_message(message.chat.id, final_message, parse_mode='html')
		
else:
	@bot.message_handler(content_types=['text'])
	def select_mode(message):
		final_message = 'Выберите режим'
		bot.send_message(message.chat.id, final_message, parse_mode='html')



bot.polling(none_stop=True)

	