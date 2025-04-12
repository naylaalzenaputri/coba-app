import streamlit as st


pages ={
    "Your Account" : [
        st.Page("profile.py", title="Buat Profile"),
        st.Page("manage.py", title="Kelola Akun"),
    ],
    "Belajar yuk!" : [
        st.Page("link.py", title="Link Video Pembelajaran"),
        st.Page("latihan.py", title="Latihan soal, yuk!"),
    ],
}
pg = st.navigation(pages)
pg.run()