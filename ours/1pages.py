import streamlit as st

st.logo("ours/kumpulan gambar/Logo1.png",size="large")

pages = {
    "🖥️-🦖": [
        st.Page("beranda.py", title="Beranda"),
        st.Page("Rekomendasi.py", title="Rekomendasi"),
        st.Page("simulasi.py", title="Simulasi")
    ]
}

pg = st.navigation(pages)
pg.run()