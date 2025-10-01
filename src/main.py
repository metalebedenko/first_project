import os
from dotenv import load_dotenv

# Эта функция сработает, потому что venv активно
load_dotenv() 

author = os.getenv('AUTHOR')

if author:
    print(f"Автор проекта: {author}")
else:
    print("Переменная 'AUTHOR' не найдена.")

