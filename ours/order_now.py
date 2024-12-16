import streamlit as st
from beranda import add_order
import pandas as pd

# Contoh penggunaan fungsi
if "orders" not in st.session_state:
    st.session_state.orders = []

st.title("Pesanan")
# Tampilkan data sebagai DataFrame Pandas
if st.session_state.orders:
    df = pd.DataFrame(st.session_state.orders)
    st.write("Tabel Pesanan:")
    st.dataframe(df)  # Menampilkan tabel pandas di Streamlit
if st.session_state.orders != []:
    if st.button("buy"):
        st.write("pesanan anda telah dibuat")