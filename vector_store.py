from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import faiss
import numpy as np


class VectoreStore:

    def __init__(self, model='all-MiniLM-L6-v2', chunk_size=512, chunk_overlap=50):
        self.model_name = model
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def create_vector_store(self, markdowns):
        model = SentenceTransformer(self.model_name)
        chunks = self._split_markdowns_into_chunks(markdowns)
        emdeddings = model.encode(chunks)

        dim = emdeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(np.array(emdeddings))

        return index, model, chunks

    def _split_markdowns_into_chunks(self, markdowns):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=['\n\n', '\n', ' ', '']
        )

        chunks = []

        for md_text in markdowns:
            chunks.extend(text_splitter.split_text(md_text))

        return chunks
