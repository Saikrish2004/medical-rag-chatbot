import streamlit as st

from src.rag_chain import get_rag_chain

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="HealthMate",
    page_icon="🩺",
    layout="wide",
)

st.title("🩺 HealthMate")
st.caption("Medical RAG Chatbot powered by Mistral AI + ChromaDB")

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Load RAG Chain
# -----------------------------
rag_chain = get_rag_chain()

# -----------------------------
# User Input
# -----------------------------
if prompt := st.chat_input("Ask a medical question..."):

    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Searching medical documents..."):

            try:
                response = rag_chain.invoke(prompt)

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                    }
                )

            except Exception as e:
                st.error(f"Error: {e}")