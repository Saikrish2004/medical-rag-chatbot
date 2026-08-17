from langchain_huggingface import HuggingFaceEmbeddings


def get_embeddings():
    """
    Load and return the Hugging Face embedding model.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings