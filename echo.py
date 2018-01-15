import telepot
import time

telegram_token = ''


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    user = bot.getUpdates(allowed_updates='message')
    message = user[0]['message']['text']
    
    bot.sendMessage(chat_id, text=message)


bot = telepot.Bot(telegram_token)
bot.message_loop(handle)

# Keep the program running
while 1:
    time.sleep(10)
