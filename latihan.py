import streamlit as st

st.write("berapa hasil dari 2+2 =")
x = st.text_input("jawaban kamu")
submit = st.button("Submit!")

if submit:
    if x == "4":
        st.success("good job kids")
    else:
        st.error("salahhh")