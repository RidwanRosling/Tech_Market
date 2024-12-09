import streamlit as st
import json

st.title("Rekomendasi Produk Tech")

# Baca data dari knowledge_base.json
try:
    with open('zaki/knowledge_base.json', 'r') as file:
        knowledge_base = json.load(file)
except FileNotFoundError:
    st.error("File knowledge_base.json tidak ditemukan!")
    knowledge_base = {"questions": []}

# Inisialisasi riwayat chat
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Input dari user
user_question = st.text_input("Tanyakan sesuatu tentang produk tech:")

# Tombol untuk mendapatkan respons
if st.button("Tanya"):
    if user_question:
        # Cari jawaban di knowledge base
        response = "Maaf, saya tidak mengerti pertanyaan Anda."
        for qa in knowledge_base["questions"]:
            if qa["question"].lower() == user_question.lower():
                response = qa["answer"]
                break
        
        # Tambahkan ke riwayat chat
        st.session_state.chat_history.append({"user": user_question, "bot": response})

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