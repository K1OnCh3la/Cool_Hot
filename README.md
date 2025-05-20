## Инструкция по использованию
1. У вас должна быть установлена Ollama с любой нейронной сетью.
2. в 34 строке response = ollama.generate(model='mistral', prompt=prompt) замените mistral на свою модель.
3. В файле config.txt напишете путь к папке со статьями.
4. Откройте командную строку. Перейдите в директорию с проектом и запустите команду: pyinstaller --onefile --add-data "config.txt;." main.py
5. Перейдите в папку dist и запустите .exe
