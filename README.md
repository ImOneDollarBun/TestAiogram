## Установка и запуск
1. Клонируем
####
```git clone https://github.com/ImOneDollarBun/TestAiogram.git```

2. Переходим в папку проекта
####
```cd TestAiogram```
####
3. Создаем виртуалку и активируем её
####
```python -m venv venv```
####
```source venv/bin/activate```
####
4. Устанавливаем зависимости (Библы)
####
```pip install -r requirements.txt```
####
5. Добавьте свой токен бота (от BotFather) в файл окружения ``.env``
####
На Ubuntu
```nano .env```
####
6. Запуск бота
####
```python main.py```
#
### Чтобы кинуть бота в фон на убунте выполните
####
```nohup python3 main.py```
###
Можно сделать автозапуск бота через ``systemctl``
####
```sudo nano /etc/systemd/system/ExcelBot.service```
####
```
[Unit]
Description=TG Bot
After=network.target

[Service]
User=root
WorkingDirectory=/root/TestAiobot/
ExecStart=/usr/bin/python3 main.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```
####
Перезапускаем демона
####
```systemctl daemon-reload```
####
Запускаем наш сервис (бота)
####
```systemctl start ExcelBot.service```
####
Проверяйте работоспособность
```systemctl status ExcelBot```
и включаем в автозагрузку
####
```systemctl enable ExcelBot```
