import streamlit as st
import pandas as pd

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
        "Please first run a call to the ikigai method in the Main page [here](../Home_page.py)."
    )
    st.stop()


def create_data_dashboard(df_row, parent_container=None):
    # Create a Streamlit container to hold all the information
    if parent_container is None:
        container = st.container(border=True)
    else:
        container = parent_container.container(border=True)

    # Display metadata information
    with container:
        st.markdown(f"##### {df_row['job_title']}")
        st.caption(f"Add a short career description here.")
        cols = st.columns([1, 1], gap="small")
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
    try:
        create_data_dashboard(row, parent_container=cols[n])
    except Exception:
        continue
