import logging
from init_app import init_app, rag_query
import ollama

logging.getLogger("pdfminer").setLevel(logging.ERROR)

index, model, chunks = init_app()

while True:
    question = input()

    context = rag_query(question, index, model, chunks)

    prompt = (f"""
Отвечай основываясь только на содержании файлов, везде где можно приводи цитату из контекста, после цитаты всегда пиши имя автору статьи, откуда взята цитата.
        {context}
Для каждой статьи, используемой для ответа, выведи библиографическую запись.
        {question}
ТУТ МОЖНО ПИСАТЬ
    """)

    response = ollama.generate(model='mistral', prompt=prompt)

    print(response['response'])
