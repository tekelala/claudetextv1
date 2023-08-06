import streamlit as st
from anthropic import Anthropic

st.set_page_config(page_title="Anthropic Chat", page_icon=":robot:") 

anthropic = Anthropic(api_key=st.secrets["ANTHROPIC_KEY"])

if "generated_text" not in st.session_state:
    st.session_state.generated_text = "" 

if "conversation" not in st.session_state:
    st.session_state.conversation = ""

st.title("Anthropic Chat")

user_input = st.text_input("You:", value="", key="input")
if user_input:
    st.session_state.conversation += f"You: {user_input}\n"

    response = anthropic.completions.create(
        model="claude-2",
        prompt=st.session_state.conversation,
        max_tokens=100,
        stop_sequences=["Assistant:"]
    )

    st.session_state.generated_text = response.completion
    st.session_state.conversation += f"Assistant: {st.session_state.generated_text}\n"

if st.session_state.generated_text:
    for line in st.session_state.conversation.split("\n"):
        st.text(line)