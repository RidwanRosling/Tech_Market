from beranda import add_order
import streamlit as st


# Inisialisasi daftar pesanan di session state
if "orders" not in st.session_state:
    st.session_state.orders = []

# Fungsi untuk menambahkan pesanan ke daftar
def add_order(item_name, price):
    st.session_state.orders.append({"item": item_name, "price": price})
    st.success(f"{item_name} berhasil ditambahkan ke pesanan!")

# Tampilan halaman
st.title("Order Page")

# Contoh implementasi tombol dan penambahan data

# Tampilkan daftar pesanan
st.subheader("Daftar Pesanan:")
if st.session_state.orders:
    for idx, order in enumerate(st.session_state.orders, start=1):
        st.write(f"{idx}. {order['item']} - {order['price']}")
else:
    st.write("Belum ada pesanan.")
