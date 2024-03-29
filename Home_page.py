import json
import time
import streamlit as st
import os
from app.prompts import input_to_jobs
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
from langchain.output_parsers import PandasDataFrameOutputParser
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(
    page_title="IkigAI - Main page",
    page_icon="🎨",
)

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

st.caption(
    "Input at least 5 entries per category. Press [Enter] key to have each input into a new line break."
)
input_topics = [
    ":heart: What you like:",
    ":thumbsup: What you are good at:",
    ":moneybag: What you can be paid for:",
    ":earth_africa: What the world needs:",
]
placeholders = [
    "Project planning\nLeading teams\nCoding data pipelines\n...",
    "Mathematics\nOrganising\nAbstraction\n...",
    "Automation\nEntrepreneurship\nMore sustainable processing\n...",
    "Climate mitigation\nGlobalisation\nTeam work\n...",
]
user_input = {k: "" for k in input_topics}
cols = st.columns([1, 1], gap="large")
for i, (k, v) in enumerate(user_input.items()):
    if i % 2 == 0:
        col = cols[0]
    else:
        col = cols[1]

    user_input[k] = col.text_area(
        label=k,
        placeholder=placeholders[i],
        key=f"{k}",
        height=150,
    )

with st.expander(":wrench: Parameters"):
    cols = st.columns(3)
    gpt_model = cols[0].selectbox(
        "OpenAI model",
        (
            "gpt-3.5-turbo",
            "gpt-4-turbo-preview",
        ),
        key="model",
    )
    temperature = cols[1].slider(
        "Model creativity",
        min_value=0.0,
        max_value=1.3,
        value=0.9,
        step=0.1,
        key="temperature",
    )
    cols[1].caption(
        "A low value for creativity will result in less creative more obvious accurate responses."
    )

    response_len = cols[2].select_slider(
        "Response length",
        options=["Short", "Medium", "Long"],
        value="Medium",
        key="max_tokens",
    )
    length_to_tokens = {
        "Short": 256,
        "Medium": 512,
        "Long": 1024,
    }
    max_tokens = length_to_tokens[response_len]

if st.button(":sparkles: Search my ikigai", type="primary", use_container_width=True):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    model = ChatOpenAI(
        api_key=openai_api_key,
        model=gpt_model,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    prompt = ChatPromptTemplate.from_template(input_to_jobs)
    parser = StrOutputParser()  # PandasDataFrameOutputParser()

    chain = prompt | model | parser

    with st.spinner(
        text="Searching within your responses... \n Shouldn't take more than 30 seconds."
    ):
        response = chain.invoke({"user_input": user_input})

    try:
        data = json.loads(response)
        df = pd.DataFrame(data)
    except Exception as e:
        st.text(response)
        st.warning(f"**Error:** {e}. \n Trying again.")
        prompt.append(
            f"Your last response was not a valid format. Error: {e} \n Please try again."
        )
        response = chain.invoke({"user_input": user_input})
        data = json.loads(response)
        df = pd.DataFrame(data)

    st.session_state["ikigai_df"] = df
    st.dataframe(df)
    time.sleep(3)
    st.switch_page("pages/1_Results.py")
