import time
import numpy as np
import streamlit as st
import pandas as pd
from app.utils import get_most_relevant_image
from streamlit_extras.card import card
import os

if os.path.isfile(".env"):
    from dotenv import load_dotenv

    load_dotenv(".env")
    PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")
else:
    PEXELS_API_KEY = st.secrets["PEXELS_API_KEY"]

st.set_page_config(
    page_title="Results Dashboard - IkigAI",
    page_icon="🎨",
    layout="wide",
)


st.title("Results dashboard | IkigAI")
st.caption(
    "Your ikigai is your life purpose, it's what brings you joy and inspires you to get out of bed every day. 🌟💼"
)

st.markdown(
    r"Your AI assistant has helped you find your ikigai. Here are your results."
)
try:
    results_df = st.session_state["ikigai_df"]
except KeyError:
    st.warning(
        "Please first run a call to the ikigai method in the Main page. Returning to the Home page."
    )
    time.sleep(3)
    st.switch_page("Home_page.py")


def create_data_dashboard(df_row, parent_container=None):
    # Create a Streamlit container to hold all the information
    if parent_container is None:
        container = st.container(border=True)
    else:
        container = parent_container.container(border=True)

    # Display metadata information
    with container:
        # Search for image:
        search_text = df_row["job_title"] + " career"
        try:
            most_relevant_image_url = get_most_relevant_image(
                search_text, PEXELS_API_KEY
            )
        except Exception:
            most_relevant_image_url = "https://images.pexels.com/photos/301703/pexels-photo-301703.jpeg?auto=compress&cs=tinysrgb&w=640&h=420&dpr=2"

        description = df_row["job_description"]

        card(
            title=df_row["job_title"],
            text=description,
            image=most_relevant_image_url,
            url=None,
            styles={
                "card": {
                    "width": "100%",
                    "aspect-ratio": "16 / 9",
                    "border-radius": "10px",
                    "margin": "0px",
                },
            },
        )

        st.caption("Matched traits:")
        cols = st.columns([1, 1], gap="small")
        if not isinstance(df_row["love"], list):
            df_row["love"] = ["--"]
        if not isinstance(df_row["skills"], list):
            df_row["skills"] = ["--"]
        if not isinstance(df_row["economy"], list):
            df_row["economy"] = ["--"]
        if not isinstance(df_row["society"], list):
            df_row["society"] = ["--"]

        cols[0].dataframe(
            df_row["love"],
            use_container_width=True,
            column_config={"value": st.column_config.Column("❤️")},
        )
        cols[1].dataframe(
            df_row["skills"],
            use_container_width=True,
            column_config={"value": st.column_config.Column("👍")},
        )
        cols = st.columns([1, 1], gap="small")
        cols[0].dataframe(
            df_row["economy"],
            use_container_width=True,
            column_config={"value": st.column_config.Column("💰")},
        )
        cols[1].dataframe(
            df_row["society"],
            use_container_width=True,
            column_config={"value": st.column_config.Column("🌍")},
        )

    return container


# Call the function to display the dashboard

cols = st.columns([0.5, 0.5], gap="small")

for i, row in results_df.iterrows():
    n = 0 if i % 2 == 0 else 1
    create_data_dashboard(row, parent_container=cols[n])
