# SENDTASK-BOT
A simple telegram bot for sending tasks from Telegram to e-mail mailbox (Outlook) to parse incoming e-mails as tasks.

## Clone
```
git clone https://github.com/nsuvorov83/sendtask-bot.git && cd sendtask-bot
```

## Configure
Edit "Configuration" section in src/sendtask-bot.py . The bot processes messages from CFG_OWNER_ID only. You can learn your telegram user_id using @my_id_bot .

## Run in docker
```
docker build --tag=sendtask-bot .
docker run  -it -d sendtask-bot
```

## TODO
- [ ] Подставлять имя отправителя, если пересылаю чужое сообщение в бот. Если сам пишу - не подставлять
- [ ] Добавить теги