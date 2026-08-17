import os

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()


def get_llm():
    """
    Load and return the Mistral chat model.
    """

    llm = ChatMistralAI(
        model="mistral-small-latest",
        api_key=os.getenv("MISTRAL_API_KEY"),
        temperature=0.2,
    )

    return llm