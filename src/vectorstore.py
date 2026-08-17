from langchain_chroma import Chroma


def create_vectorstore(chunks, embeddings):
    """
    Create and persist a Chroma vector database.
    """

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db",
    )

    return vectorstore


def load_vectorstore(embeddings):
    """
    Load an existing Chroma vector database.
    """

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings,
    )

    return vectorstore