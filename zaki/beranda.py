import streamlit as st
from data_deskrip import *

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
    st.write(" ".join(deskrip_Home))
    st.subheader("Gunakan menu dibagian kiri untuk Menjelajahi lebih banyak produk lainnya.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Cpu")
        st.image("zaki/kumpulan gambar/53bc3a1d-cf61-41d7-91f4-2124dbde60d9.jpg", caption="Intel core i9 14900K Box")
        st.button("Go to CPU page", key="switch_button_1", on_click=switch_page, args=("CPU",))
    
    with col2:
        st.header("Gpu")
        st.image("zaki/kumpulan gambar/d909e419-85d0-476f-995d-4e2476f310c8.jpg", caption="MSI GeForce RTX 4090 GAMING X TRIO 24GB GDDR6X")
        st.button("Go to GPU page", key="switch_button_2", on_click=switch_page, args=("GPU",))

    with col3:
        st.header("Casing")
        st.image("zaki/kumpulan gambar/b70fc2df-20f4-4626-ad91-1de714210895.jpg", caption="TECWARE FLATLINE TG MK2")
        st.button("Go to Casing page", key="switch_button_3", on_click=switch_page, args=("Casing",))
    




elif st.session_state.page == "Motherboard":
    st.title("Motherboard")
    st.write(" ".join(deskrip_Motherboard))
    
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        st.subheader("Asrock")
        st.image("zaki/kumpulan gambar/13757756_509be07d-f324-4df7-832e-e3b0d0009bcd_600_600.jpg", caption="ASROCK B550M PRO4 AMD")
        with st.popover("Press"):
            st.markdown("**Rp. 1.548.000**")
            st.markdown("Spesifikasi:")
            st.markdown(" ".join(sp_satu))
            st.button("Order now", key="mobo_1")
        harga_col4 = 1548000 # Harganya
    
    with col5:
        st.subheader("Srock")
        st.image("zaki/kumpulan gambar/20221111162833.jpg", caption="SROCK MOTHERBOARD B560M HDV M.2 R2.0 (INTEL)")
        with st.popover("Press"):
            st.markdown("**Rp. 1.250.000**")
            st.markdown("Spesifikasi:")
            st.markdown(" ".join(sp_dua))
            st.button("Order now", key= "mobo_2")
        harga_col5 = 1250000 # Harganya
            
    with col6:
        st.subheader("Asrock")
        st.image("zaki/kumpulan gambar/20221115104303.jpg", caption="ASROCK MOTHERBOARD A520M-HVS (AMD)")
        with st.popover("Press"):
            st.markdown("**Rp. 989.000**")
            st.markdown("Spesifikasi:")
            st.markdown(" ".join(sp_tiga))
            st.button("Order now", key="mobo_3")
        harga_col6 = 989000 # Harganya
    with col7:
        st.subheader("Asus")
        st.image("zaki/kumpulan gambar/20200617162250.jpg", caption="ASUS Motherbord ROG STRIX B460-F GAMING")
        with st.popover("Press"):
            st.markdown("**Rp.3.300.000**")
            st.markdown("Spesifikasi:")
            st.markdown(" ".join(sp_empat))
            st.button("Order now", key="mobo_4")
        harga_col7 = 3300000 #harganya

        







elif st.session_state.page == "CPU":
    st.title("CPU")
    st.write("**Central processing unit**")
    st.write(" ".join(deskrip_CPU))

    cpu1, cpu2, cpu3, cpu4 = st.columns(4)
    with cpu1:
        st.subheader("Amd ryzen 5000 series")
        st.image("zaki/kumpulan gambar/cea0c491-d4f5-43da-974b-cb5c06597b95.jpg", caption="AMD Ryzen 9 5900X")
        with st.popover("Press"):
            st.markdown("**Rp. 5.730.000**")
            st.markdown(" ".join(sp_lima))
            st.button("Order now", key="cpu1")
    harga_cpu1 = 5730000 # Harganya

    with cpu2:
        st.subheader("Intel pentium Gold")
        st.image("zaki/kumpulan gambar/20200611151837_th.jpg", caption="intel pentium G5420")
        with st.popover("Press"):
            st.markdown("**Rp.840.000**")
            st.markdown(" ".join(sp_enam))
            st.button("Order now", key="cpu2")
    harga_cpu2 = 840000
    with cpu3:
        st.subheader("Amd ryzen 3000 series")
        st.image("zaki/kumpulan gambar/ffe4a4fa-23ef-4748-8e7c-926ae68b3820.jpg", caption="Ryzen 5 3600")
        with st.popover("Press"):
            st.markdown("**Rp.2.020.000**")
            st.markdown(" ".join(sp_tujuh))
            st.button("Order now", key="cpu3")
    harga_cpu2 = 2020000
    with cpu4:
        st.subheader("Intel gen 10")
        st.image("zaki/kumpulan gambar/9126088_0d6b3035-4d20-4d61-8df3-39ac27acbdf8_700_700.jpg", caption="Intel I5 10400F")
        with st.popover("Press"):
            st.markdown("**Rp.1.635.000**")
            st.markdown(" ".join(sp_delapan))
            st.button("Order now", key="cpu4")
    harga_cpu2 = 2020000



    




elif st.session_state.page == "GPU":
    st.title("GPU")
    st.write(" ".join(deskrip_GPU))
    
    gpu1, gpu2, gpu3, gpu4 = st.columns(4)

    with gpu1:
        st.subheader("Amd Rx")
        st.image("zaki/kumpulan gambar/1024.png", caption="Radeon RX 580 GAMING X 8G")
        with st.popover("Press"):
            st.markdown("**Rp. 1.650.000**")
            st.markdown(" ".join(sp_sembilan))
            st.button("Order now", key="gpu1")
    harga_gpu1 = 1650000 # harganya

    with gpu2:
        st.subheader("Nvidia G series")
        st.image("zaki/kumpulan gambar/1024 (1).png", caption="GTX 1660 Gaming X 6G")
        with st.popover("Press"):
            st.markdown("**Rp. 1.679.000**")
            st.markdown(" ".join(sp_sepuluh))
            st.button("Order now", key="gpu2")
    harga_gpu2 = 2020000 # harganya
    with gpu3:
        st.subheader("Intel arc")
        st.image("zaki/kumpulan gambar/e60d7796-d02c-486e-8c6a-dc94ed501ab8.png", caption="Intel ARC 750")
        with st.popover("Press"):
            st.markdown("**Rp. 3.499.000**")
            st.markdown(" ".join(sp_sebelas))
            st.button("Order now", key="gpu3")
    harga_gpu3 = 3499000 # harganya















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