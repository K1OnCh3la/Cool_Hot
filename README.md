## Инструкция по использованию
У вас должна быть установлена Ollama с любой нейронной сетью.
в 34 строке response = ollama.generate(model='mistral', prompt=prompt) замените mistral на свою модель.
В файле config.txt напишете путь к папке со статьями.
Откройте командную строку. Перейдите в директорию с проектом и запустите команду: pyinstaller --onefile --add-data "config.txt;." main.py
Перейдите в папку dist и запустите .exe
