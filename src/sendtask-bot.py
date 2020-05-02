import os
import telebot
import smtplib
import textwrap
from email.mime.text import MIMEText

#Configuration
CFG_TOKEN = os.environ.get('CFG_TOKEN') #TELEGRAM_BOT_TOKEN
CFG_SMTP_LOGIN = os.environ.get('CFG_SMTP_LOGIN') #'%YOUR_SMTP_LOGIN_ON_YANDEX%'
CFG_SMTP_PASS = os.environ.get('CFG_SMTP_PASS') #'%YOUR_SMTP_PASS_ON_YANDEX%'
CFG_SMTP_FROM = os.environ.get('CFG_SMTP_FROM') #'%FROM_EMAIL_ADDRESS%'
CFG_SMTP_TO = os.environ.get('CFG_SMTP_TO') #'%TO_EMAIL_ADDRESS%'

#Change type if OWNER_ID is str
try:
    CFG_OWNER_ID = int(os.environ.get('CFG_OWNER_ID')) #YOUR_USER_ID_IN_TELEGRAM
except:
    CFG_OWNER_ID = os.environ.get('CFG_OWNER_ID')

bot = telebot.TeleBot(CFG_TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    #Checking whether it's owner of the bot
    if message.from_user.id == CFG_OWNER_ID:
        do_next(message)
    else: 
        pass

def do_next(message):
    #Ping
    if(message.text == 'ping'):
        bot.send_message(message.from_user.id, "pong")
        return 0
    
    #Sening a message to outlook
    #Check if Subject is too long
    txt = message.text
    msg = MIMEText('')
    if len(txt) > 40:
        txt = textwrap.shorten(txt, width=40, placeholder="...")
        msg = MIMEText(message.text)
    else:
        msg = MIMEText("Задача из Telegram")
    
    #Check whether forwarded from another user
    if "forward_sender_name" in message.json:
        txt = f'[{message.json["forward_sender_name"]}] {txt}'
    elif "forward_from" in message.json:
        txt = f'[{message.json["forward_from"]["first_name"]}] {txt}'

    #Add ready data to MIME object
    msg['From'] = CFG_SMTP_FROM
    msg['To'] = CFG_SMTP_TO
    msg['Subject'] = f'[TASK] {txt}'

    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
        server.login(CFG_SMTP_LOGIN, CFG_SMTP_PASS)
        server.sendmail(CFG_SMTP_FROM, CFG_SMTP_TO, msg.as_string()) 
        bot.send_message(message.from_user.id, "Задача отправлена в Outlook")
        server.quit()
    except Exception as err:
        #Exceptions processing with sending text of an error
        bot.send_message(message.from_user.id, f"При отправке сообщения произошла ошибка: {str(err)}")

#Running the bot
bot.polling(True, 0)