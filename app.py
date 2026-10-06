import streamlit as st

from app.model_loader import load_model
from app.ui import render_ui


@st.cache_resource
def initialize_model():
    return load_model()


def main():

    st.set_page_config(
        page_title="SLM Lab",
        page_icon="🤖",
        layout="wide"
    )

    with st.spinner("Loading SLM..."):

        tokenizer, model, device = initialize_model()

    render_ui(
        tokenizer,
        model,
        device
    )


if __name__ == "__main__":
    main()