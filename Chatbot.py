from openai import OpenAI
import streamlit as st
import os

with st.sidebar:
    # Check if file .env exists in root directory
    if os.path.isfile(".env"):
        from dotenv import load_dotenv

        load_dotenv(".env")
        OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
        openai_api_key = st.text_input(
            "OpenAI API Key",
            value=OPENAI_API_KEY,
            key="chatbot_api_key",
            type="password",
        )
    else:
        openai_api_key = st.text_input(
            "OpenAI API Key", key="chatbot_api_key", type="password"
        )
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.title("🎨 IkigAI")
st.caption(
    r"An AI assistant to help you find your ikigai. Your ikigai is your life purpose, it's what brings you joy and inspires you to get out of bed every day. 🌟💼"
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=st.session_state.messages
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
