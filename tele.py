import telebot

bot = telebot.TeleBot('8554885181:AAEaC6Cup3k2IIIMdIA6h3qPB6bbBi1w--M')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Привет, Босс!')

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, '<b>Команды для использования</b>/start', parse_mode='HTML')

bot.polling(none_stop=True)
