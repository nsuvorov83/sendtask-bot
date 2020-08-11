# SENDTASK-BOT
A simple telegram bot for sending tasks from Telegram to e-mail mailbox (Outlook) to parse incoming e-mails as tasks.

## Clone
```
git clone https://github.com/nsuvorov83/sendtask-bot.git && cd sendtask-bot
```

## Configure
Edit and remove "_example" in .env_example file . The bot processes messages from CFG_OWNER_ID only. You can learn your telegram user_id using @my_id_bot .
![Setting a new rule in Outlook](https://github.com/nsuvorov83/sendtask-bot/raw/master/sendtask_outlook.PNG)

## Run in docker
```
docker-compose up -d
```

## TODO
- [x] Вынести пароли и прочие креды в .env файл
- [x] Сделать сокращение строки темы письма, если она слишком велика. Длинную строку поместить в тело письма
- [x] Подставлять имя отправителя, если пересылаю чужое сообщение в бот. Если сам пишу - не подставлять
- [ ] Добавить теги
