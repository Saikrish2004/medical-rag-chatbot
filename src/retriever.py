from src.embeddings import get_embeddings
from src.vectorstore import load_vectorstore

def get_retriever(k=3):
    embeddings = get_embeddings()
    vectorstore = load_vectorstore(embeddings)

    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k},
    )