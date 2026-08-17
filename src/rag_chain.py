from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from src.llm import get_llm
from src.prompt import PROMPT
from src.retriever import get_retriever




def format_docs(docs):
    return "\n\n".join(
        f"[Page {doc.metadata.get('page', 'Unknown')}]\n{doc.page_content}"
        for doc in docs
    )
def get_rag_chain():
    """
    Create and return the RAG chain.
    """

    retriever = get_retriever()
    llm = get_llm()

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | PROMPT
        | llm
        | StrOutputParser()
    )

    return rag_chain