from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore


def main():
    print("Loading PDF...")

    documents = load_pdf("data/medical_book.pdf")

    print(f"Loaded {len(documents)} pages")

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Loading embedding model...")

    embeddings = get_embeddings()

    print("Creating Chroma Vector Database...")

    create_vectorstore(chunks, embeddings)

    print("Vector database created successfully!")


if __name__ == "__main__":
    main()