import streamlit as st


def app():
    st.markdown("# Model")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        parameter1 = st.text_input("parameter1", "Placeholder", key="parameter1")
        st.write("parameter is", parameter1)
    with col2:
        parameter2 = st.text_input("parameter2", "Placeholder", key="parameter2")
        st.write("parameter is", parameter2)
    with col3:
        parameter3 = st.text_input("parameter3", "Placeholder", key="parameter3")
        st.write("parameter is", parameter3)


if __name__ == "__main__":
    app()
