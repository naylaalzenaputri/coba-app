import streamlit as st

def dashboard():
    st.title("dashboard")

pages ={
    "Your Account" : [
        st.Page("profile.py", title="Buat Profile")
        st.page("manage.py", title)
    ]
}
pg = st.navigation(["profile.py", dashboard])
pg.run()