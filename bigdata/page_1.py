import streamlit as st
import utils


def app():
    st.markdown("# View")
    with st.expander("View Presentation"):
        pdf_display = utils.show_pdf("assets/A2.pdf")
    st.markdown(pdf_display, unsafe_allow_html=True)


if __name__ == "__main__":
    app()
