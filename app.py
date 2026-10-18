import streamlit as st

st.set_page_config(page_title="Shabana Portfolio", page_icon="✨")

st.title("Hi, I am Shabana")
st.subheader("Aspiring AI Developer")
st.write("---")
st.write("Welcome to my AI Portfolio")
st.write("I am passionate about AI and building tech with Python.")
st.write("Skills: Python | AI ML | Streamlit")
st.write("Project: AI Portfolio Website - Live!")

if st.button("Say Hello"):
    st.balloons()
    st.success("Thanks for visiting!")

st.caption("Made with love by Shabana")