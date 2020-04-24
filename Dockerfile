FROM python:3.7

ADD ./src/sendtask-bot.py /
RUN pip install pyTelegramBotAPI
CMD python sendtask-bot.py