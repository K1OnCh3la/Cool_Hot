import numpy as np

from extractor import Extractor
from vector_store import VectoreStore


def init_app():

    with open("config.txt", "r") as f:
        folder_path = f.read().strip()

    extractor = Extractor(folder_path)
    vector_store = VectoreStore()

    data = extractor.extract_all_pdfs()

    index, model, chunks = vector_store.create_vector_store(data)

    return index, model, chunks


def rag_query(question, index, model, chunks):
    question_embedding = model.encode([question])
    k = 3
    distances, indices = index.search(np.array(question_embedding), k)
    context = "\n\n".join([chunks[i] for i in indices[0]])
    return context
