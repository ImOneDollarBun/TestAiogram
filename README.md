## Установка и запуск
1. Клонируем
####
```git clone https://github.com/ImOneDollarBun/TestAiogram.git```

2. Переходим в папку проекта
####
```cd TestAiogram```
3. Создаем виртуалку и активируем её
####
```python -m venv venv```
####
```source venv/bin/activate```
4. Устанавливаем зависимости (Библы)
####
```pip install -r requirements.txt```
5. Добавьте свой токен бота (от BotFather) в файл окружения ``.env``
####
На Ubuntu
```nano .env```
6. Запуск бота
####
```python main.py```