import streamlit as st

st.title("PROFILE")
st.write("Mohon isi data diri anda")
x = st.text_input("siapa nama anda?")
st.write(f'Selamat datang, {x} !')