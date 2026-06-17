import streamlit as st

from agent.travel_agent import run_agent
from memory import get_chat_history


st.set_page_config(
    page_title="TRAVEL ASSISTANT",
    page_icon="✈️",
    layout="wide"
)


with st.sidebar:

    st.title("Settings")

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

st.title("✈️Travel ASSISTANT")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input(
    "Ask me about travel..."
)


if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        
        history = get_chat_history(
            st.session_state.messages
        )
        
        response = run_agent(
            f"""
        Conversation History:
        {history}

        Current User Query:
        {prompt}
        """
        )


        response = run_agent(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )