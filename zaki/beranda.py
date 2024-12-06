import streamlit as st

# Inisialisasi session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Fungsi untuk navigasi
def switch_page(page_name):
    st.session_state.page = page_name

# Sidebar atau navigasi
st.sidebar.title("Menu")
if st.sidebar.button("Home", use_container_width=True):
    switch_page("Home")
if st.sidebar.button("Motherboard 😃", use_container_width=True):
    switch_page("Motherboard")
if st.sidebar.button("CPU 😎", use_container_width=True):
    switch_page("CPU")
if st.sidebar.button("GPU 💀", use_container_width=True):
    switch_page("GPU")
if st.sidebar.button("SSD 🧐", use_container_width=True):
    switch_page("SSD")
if st.sidebar.button("RAM 🙂", use_container_width=True):
    switch_page("RAM")
if st.sidebar.button("PSU ⚡", use_container_width=True):
    switch_page("PSU")
if st.sidebar.button("Casing 🤔", use_container_width=True):
    switch_page("Casing")


# Menampilkan konten berdasarkan halaman
if st.session_state.page == "Home":
    st.title("Selamat datang di Merapi")
    st.subheader("(Mending Rakit PC)")
    st.write("**Solusi Lengkap untuk Merakit dan Meng-upgrade PC Impian Anda, Tanpa Ribet.**")
    st.write("Salah satu alasan utama mengapa merakit PC adalah pilihan terbaik untuk jangka panjang adalah kemudahannya untuk di-upgrade sesuai kebutuhan di masa depan.")
    st.write("Dengan merakit PC, Anda dapat memilih komponen berkualitas yang sesuai dengan kebutuhan saat ini, seperti motherboard dengan dukungan prosesor dan RAM terbaru. Ketika kebutuhan meningkat, seperti untuk gaming, pekerjaan kreatif, atau tugas berat lainnya, Anda cukup mengganti atau menambahkan komponen tertentu tanpa harus membeli PC baru secara keseluruhan. Hal ini tidak hanya menghemat biaya, tetapi juga memastikan performa PC Anda selalu optimal seiring perkembangan teknologi.")
    st.subheader("Gunakan menu dibagian kiri untuk Menjelajahi lebih banyak produk lainnya.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Cpu")
        st.image("Zaki/kumpulan gambar/53bc3a1d-cf61-41d7-91f4-2124dbde60d9.jpg", caption="Intel core i9 14900K Box")
    
    with col2:
        st.header("Gpu")
        st.image("Zaki/kumpulan gambar/d909e419-85d0-476f-995d-4e2476f310c8.jpg", caption="MSI GeForce RTX 4090 GAMING X TRIO 24GB GDDR6X")

    with col3:
        st.header("Casing")
        st.image("Zaki/kumpulan gambar/b70fc2df-20f4-4626-ad91-1de714210895.jpg", caption="TECWARE FLATLINE TG MK2")
    




elif st.session_state.page == "Motherboard":
    st.title("Motherboard")
    st.write("Ini adalah halaman informasi Motherboard.")




elif st.session_state.page == "CPU":
    st.title("CPU")
    st.write("Ini adalah halaman informasi CPU.")




elif st.session_state.page == "GPU":
    st.title("GPU")
    st.write("ini adalah halaman informasi GPU")




elif st.session_state.page == "SSD":
    st.title("SSD")
    st.write("ini adalah halaman informasi SSD")




elif st.session_state.page == "RAM":
    st.title("RAM")
    st.write("ini adalah halaman informasi RAM")




elif st.session_state.page == "PSU":
    st.title("PSU")
    st.write("ini adalah halaman informasi PSU")




elif st.session_state.page == "Casing":
    st.title("Casing")
    st.write("ini adalah halaman informasi Casing")