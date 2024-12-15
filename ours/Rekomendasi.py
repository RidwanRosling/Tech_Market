import streamlit as st
import json
import pandas as pd
from chatbot import get_pc_recommendation
from chatbot import get_bot_response
st.title("Recomendation Product Merapi")

# Baca data dari knowledge_base.json
try:
    with open('ours/knowledge_base.json', 'r') as file:
        knowledge_base = json.load(file)
except FileNotFoundError:
    st.error("File knowledge_base.json tidak ditemukan!")
    knowledge_base = {"questions": []}
    

# Inisialisasi riwayat chat
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.caption("type 'help' to see what bot can do!")

# Input dari user
user_question = st.text_input("Asking Something About our Products:")

# Tombol untuk mendapatkan respons
if st.button("ASK"):
    if user_question:
        # Dapatkan respons dari chatbot
        response = get_bot_response(user_question)
        
        # Tambahkan ke riwayat chat
        st.session_state.chat_history.append({"user": user_question, "bot": response})

# Tombol untuk mendapatkan rekomendasi PC
if st.button("Rekomendasi PC"):
    pc_recommendations = get_pc_recommendation()  # Mengambil data rekomendasi dari chatbot.py

    if pc_recommendations:
        st.write("🤖 Bot: here is the ready-made pc we recommend🫡")
        # Memastikan data "recomend_me_a_pc" ada di dalam file JSON
        pc_data = []
        for pc, specs in pc_recommendations["recomend_me_a_pc"].items():
            pc_info = {
                "PC": pc,
                "PRICE": specs.get("PRICE"),
                "CPU": specs.get("CPU"),
                "Fan Cooler": specs.get("Fan Cooler"),
                "MOBO": specs.get("MOBO"),
                "RAM": specs.get("RAM"),
                "STORAGE": specs.get("STORAGE"),
                "GPU": specs.get("GPU"),
                "PSU": specs.get("PSU"),
                "CASING": specs.get("CASING")
            }
            pc_data.append(pc_info)

        # Konversi ke DataFrame Pandas
        df = pd.DataFrame(pc_data)
        #agar memulai dari index 1
        df.index = pd.RangeIndex(start=1, stop=len(df) + 1, step=1)


        # Menampilkan DataFrame di Streamlit
        st.write(df)
    else:
        st.error("Tidak ada rekomendasi PC ditemukan.")


# Tampilkan riwayat chat
st.subheader("Riwayat Chat:")
for chat in st.session_state.chat_history:
    st.write(f"👤 Anda: {chat['user']}")
    st.write(f"🤖 Bot: {chat['bot']}")
    st.write("---")

# Tombol untuk menghapus riwayat
if st.button("Hapus Riwayat Chat"):
    st.session_state.chat_history = []
    st.rerun()  # Menggunakan st.rerun() sebagai pengganti st.experimental_rerun()