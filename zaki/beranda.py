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
        st.button("Go to CPU page", key="switch_button_1", on_click=switch_page, args=("CPU",))
    
    with col2:
        st.header("Gpu")
        st.image("Zaki/kumpulan gambar/d909e419-85d0-476f-995d-4e2476f310c8.jpg", caption="MSI GeForce RTX 4090 GAMING X TRIO 24GB GDDR6X")
        st.button("Go to GPU page", key="switch_button_2", on_click=switch_page, args=("GPU",))

    with col3:
        st.header("Casing")
        st.image("Zaki/kumpulan gambar/b70fc2df-20f4-4626-ad91-1de714210895.jpg", caption="TECWARE FLATLINE TG MK2")
        st.button("Go to Casing page", key="switch_button_3", on_click=switch_page, args=("Casing",))
    




elif st.session_state.page == "Motherboard":
    st.title("Motherboard")
    st.write("Motherboard adalah komponen utama dalam sebuah PC yang berfungsi sebagai papan sirkuit utama tempat semua komponen lain saling terhubung dan berkomunikasi. Bisa dibilang, motherboard adalah tulang\
             punggung dari sebuah komputer karena tanpa itu, komponen lain seperti prosesor, RAM, kartu grafis, dan penyimpanan tidak dapat berfungsi bersama.")
    
    col4, col5, col6, col7 = st.columns(4)
    with col4:
        st.subheader("Asrock")
        st.image("zaki/kumpulan gambar/13757756_509be07d-f324-4df7-832e-e3b0d0009bcd_600_600.jpg", caption="ASROCK B550M PRO4 AMD")
        with st.popover("Press"):
            st.markdown("**Rp. 1.548.000**")
            st.markdown("Spesifikasi:")
            st.markdown("Supports 3rd Gen AMD AM4 Ryzen™ / Future AMD Ryzen™\
                        Processors 8 Power Phase Design, Digi Power\
                        Supports DDR4 4733+ (OC)\
                        1 PCIe 4.0 x16, 1 PCIe 3.0 x16, 1 PCIe 3.0 x1, 1 M.2 Key E for WiFi\
                        Graphics Output Options: HDMI, DisplayPort, D-Sub\
                        AMD CrossFireX™\
                        7.1 CH HD Audio (Realtek ALC1200 Audio Codec), Nahimic Audio\
                        6 SATA3, 1 Hyper M.2 (PCIe Gen4 x4), 1 M.2 (PCIe Gen3 x2 & SATA3)\
                        2 USB 3.2 Gen2 (Rear Type A+C), 8 USB 3.2 Gen1 (4 Front, 4 Rear)\
                        Realtek Gigabit LAN")
            st.button("Order now", key="mobo_1")
        harga_col4 = 1548000 # Harganya
    
    with col5:
        st.subheader("Srock")
        st.image("zaki/kumpulan gambar/20221111162833.jpg", caption="SROCK MOTHERBOARD B560M HDV M.2 R2.0 (INTEL)")
        with st.popover("Press"):
            st.markdown("**Rp. 1.250.000**")
            st.markdown("Spesifikasi:")
            st.markdown("Supports 10th Gen Intel® Core™ Processors and 11th Gen Intel® Core™ Processors (LGA1200)\
                        6 Power Phase design\
                        Supports Intel® Turbo Boost Max 3.0 Technology\
                        Intel® B560\
                        2 x DDR4 DIMM Slots\
                        10th Gen Intel® Core™ Processors support DDR4 non-ECC, un-buffered memory up to 4600+(OC)*\
                        Supports ECC UDIMM memory modules (operate in non-ECC mode)\
                        Max. capacity of system memory: 64GB**\
                        Supports Intel® Extreme Memory Profile (XMP) 2.0\
                        7.1 CH HD Audio (Realtek ALC897 Audio Codec)\
                        Giga PHY Intel® I219V\
                        11th Gen Intel® Core™ Processors -1 x PCI Express 4.0 x16 Slot* 10th Gen Intel® Core™ Processors - 1 x PCI Express 3.0 x16 Slot* - 2 x PCI Express 3.0 x1 Slots\
                        4 x SATA3 6.0 Gb/s Connectors, support Intel® Rapid Storage Technology 18, NCQ, AHCI and Hot Plug\
                        1 x Hyper M.2 Socket (M2_1), supports M Key type 2260/2280 M.2 PCI Express module up to Gen4x4 (64 Gb/s) (Socket M2_1 works with 11th Gen Intel® Core™ processors only)*\
                        1 x Ultra M.2 Socket (M2_2), supports M Key type 2260/2280 M.2 SATA3 6.0 Gb/s module and M.2 PCI Express module up to Gen3 x4 (32 Gb/s)*\
                        Micro ATX Form Factor: 9.6-in x 7.8-in, 24.4 cm x 19.8 cm ")
            st.button("Order now", key= "mobo_2")
        harga_col5 = 1250000 # Harganya
            
    with col6:
        st.subheader("Asrock")
        st.image("zaki/kumpulan gambar/20221115104303.jpg", caption="ASROCK MOTHERBOARD A520M-HVS (AMD)")
        with st.popover("Press"):
            st.markdown("**Rp. 989.000**")
            st.markdown("Spesifikasi:")
            st.markdown("Unique Feature\
                        ASRock Super Alloy\
                        Premium 50A Power Choke\
                        Sapphire Black PCB\
                        High Density Glass Fabric PCB\
                        ASRock Ultra M.2 (PCIe Gen3 x4 & SATA3)\
                        ASRock Full Spike Protection (for all USB, Audio, LAN Ports)\
                        ASRock Live Update & APP Shop\
                        CPU\
                        Supports AMD AM4 Socket Ryzen™ 3000, 4000 G-Series and 5000 and 5000 G-Series Desktop Processors*\
                        6 Power Phase design\
                        Not compatible with AMD Ryzen™ 5 3400G and Ryzen™ 3 3200G.\
                        Chipset\
                        AMD A520\
                        Memory\
                        Dual Channel DDR4 Memory Technology\
                        2 x DDR4 DIMM Slots\
                        AMD Ryzen series CPUs ")
            st.button("Order now", key="mobo_3")
        harga_col6 = 989000 # Harganya
    with col7:
        st.subheader("Asus")
        st.image("zaki/kumpulan gambar/20200617162250.jpg", caption="ASUS Motherbord ROG STRIX B460-F GAMING")
        with st.popover("Press"):
            st.markdown("**Rp.3.300.000**")
            st.markdown("Spesifikasi:")
            st.markdown("ASUS ROG STRIX B460-F GAMING (Socket 1200/B460/DDR4/S-ATA 600/ATX)\
                        Intel Socket LGA1200 for 10th Gen Intel Core, Pentium Gold and Celeron Processors*\
                        4 x DIMM, Max. 128GB, DDR4 2933/2800/2666/2400/2133 MHz Non-ECC, Un-buffered Memory*\
                        SupremeFX Shielding Technology")
            st.button("Order now", key="mobo_4")
        harga_col7 = 3300000 #harganya

        







elif st.session_state.page == "CPU":
    st.title("CPU")
    st.write("**Central processing unit**")
    st.write("atau dalam bahasa Indonesia dikenal sebagai unit pemrosesan pusat,\
            adalah komponen utama dalam komputer yang bertanggung jawab untuk menjalankan perintah dan\
            instruksi dari perangkat lunak (software). CPU sering disebut sebagai otak komputer karena semua proses\
            inti pengolahan data dilakukan di sana.")

    cpu1, cpu2, cpu3, cpu4 = st.columns(4)
    with cpu1:
        st.subheader("Amd ryzen 5000 series")
        st.image("zaki/kumpulan gambar/cea0c491-d4f5-43da-974b-cb5c06597b95.jpg", caption="AMD Ryzen 9 5900X")
        with st.popover("Press"):
            st.markdown("**Rp. 5.730.000**")
            st.markdown("- 12 Core\n - 24 threads\n - Base clock 3.4Ghz\n - Max clock up to 4.8GhzTotal L2 Cache 6MB\n - Total L3 Cache 64MB\n - Unlocked Yes\
                        \n - CMOS TSMC 7nm FinFET\n - Package AM4\n - PCI Express Version PCIe 4.0\n - Thermal Solution (PIB) Not included\n - Default TDP / TDP 105W")
            st.button("Order now", key="cpu1")
    harga_cpu1 = 5730000 # Harganya

    with cpu2:
        st.subheader("Intel pentium Gold")
        st.image("zaki/kumpulan gambar/20200611151837_th.jpg", caption="intel pentium G5420")
        with st.popover("Press"):
            st.markdown("**Rp.840.000**")
            st.markdown("- CPU Socket Type : LGA 1151\n - Processors Generation : 9th Gen\n - Family : Coffeelake\n - Cores : 2\n\
                        - Threads : 4\n - Operating Frequency : 3.8GHz\n - Max Turbo Frequency : -\n - Cache : 4 MB\n - Manufacturing Tech : 14 nm\n - Integrated Graphics : Intel UHD Graphics 610\
                        \n - Thermal Design Power : 54 W\n - Thermal Solution (Cooler) : Included")
            st.button("Order now", key="cpu2")
    harga_cpu2 = 840000
    with cpu3:
        st.subheader("Amd ryzen 3000 series")
        st.image("zaki/kumpulan gambar/ffe4a4fa-23ef-4748-8e7c-926ae68b3820.jpg", caption="Ryzen 5 3600")
        with st.popover("Press"):
            st.markdown("**Rp.2.020.000**")
            st.markdown("- 6 core\
                        \n - 12 threads\
                        \n - Base clock 3.6Ghz\
                        \n - Max boost clock 4.2Ghz\
                        \n - total L1 cache 64kb\
                        \n - total L2 cache 3MB\
                        \n - titak L3 cache 32Mb\
                        \n - unlocked\
                        \n - yes\
                        \n - CMOS\
                        \n - TSMC 7nm FinFET\
                        \n - Package\
                        \n - AM4\
                        \n - PCI Express® VersionROM-06a\
                        \n - PCIe 4.0 x16\
                        \n - Thermal Solution\
                        \n - Wraith Stealth\
                        \n - Default TDP / TDPROM-06a\
                        \n - 65W\
                        \n - Max Temps\
                        \n - 95°")
            st.button("Order now", key="cpu3")
    harga_cpu2 = 2020000
    with cpu4:
        st.subheader("Intel gen 10")
        st.image("zaki/kumpulan gambar/9126088_0d6b3035-4d20-4d61-8df3-39ac27acbdf8_700_700.jpg", caption="Intel I5 10400F")
        with st.popover("Press"):
            st.markdown("**Rp.1.635.000**")
            st.markdown("- 6 Core\
                        \n - 12 Threads\
                        \n - Processor base frequency 2.90Ghz\
                        \n - Max Turbo frequency 4.30Ghz\
                        \n - cache 12 MB intel® Smart cache\
                        \n - Bus speed 8 GT/s\
                        \n - TDP 65 W")
            st.button("Order now", key="cpu4")
    harga_cpu2 = 2020000



    




elif st.session_state.page == "GPU":
    st.title("GPU")
    st.write("**GPU** (Graphics Processing Unit), atau dalam bahasa Indonesia disebut unit\
              pemrosesan grafis, adalah komponen hardware yang dirancang khusus untuk menangani\
              dan mempercepat pemrosesan grafik. GPU awalnya digunakan terutama untuk rendering\
              gambar 3D pada komputer, tetapi kini memiliki aplikasi yang jauh lebih luas, termasuk\
              untuk komputasi umum (GPGPU) seperti AI,\
              pembelajaran mesin, dan simulasi fisika.")
    
    gpu1, gpu2, gpu3, gpu4 = st.columns(4)

    with gpu1:
        st.subheader("Amd Rx")
        st.image("zaki/kumpulan gambar/1024.png", caption="Radeon RX 580 GAMING X 8G")
        with st.popover("Press"):
            st.markdown("**Rp. 1.650.000**")
            st.markdown("- Interface: PCI-E\
                        \n - Core Clock: 1244 MHz\
                        \n - Memory: 8GB DDR5\
                        \n - Memory Clock: 1750 MHz\
                        \n - Memory Bus: 256 Bit\
                        \n - Display Outputs: 1x HDMI, 2x DP\
                        \n - Cooling: Double Fan Ultimate Cooling\
                        \n - Power Input: PCIe 8-pin\
                        \n - Power Consumption: 150 W\
                        \n - Type: ATX\
                        \n - Support OS: Win 7,10 and 11")
            st.button("Order now", key="gpu1")
    harga_gpu1 = 1650000 # harganya

    with gpu2:
        st.subheader("Nvidia G series")
        st.image("zaki/kumpulan gambar/1024 (1).png", caption="GTX 1660 Gaming X 6G")
        with st.popover("Press"):
            st.markdown("**Rp. 1.679.000**")
            st.markdown("- Memory Amount : 6G\
                        \n - Memory Interface : 192bit\
                        \n - DRAM Type : GDDR6\
                        \n - Graphics Clock : 1530 MHz\
                        \n - Boost Clock : 1830 MHz\
                        \n - Memory Clock : 14 Gbps\
                        \n - CUDA Cores : 1408\
                        \n - Memory Bandwidth (GB/sec) : 336\
                        \n - Microsoft DirectX : 12 API, Vulkan API\
                        \n - OpenGL : 4.6\
                        \n - Bus Support : PCI-E 3.0 x 16\
                        \n - DVI : Dual-Link DVI-D\
                        \n - HDMI : HDMI 2.0b\
                        \n - DisplayPort : DP1.4a x 1\
                        \n - Maximum Digital Resolution : 7680x4320@60Hz\
                        \n - Height : 2 Slot\
                        \n - Board Size : 235 x 115 x 40 mm\
                        \n - Graphics Card Power : 125 W\
                        \n - Recommended System Power : 450 W")
            st.button("Order now", key="gpu2")
    harga_gpu2 = 2020000 # harganya
    with gpu3:
        st.subheader("Intel arc")
        st.image("zaki/kumpulan gambar/e60d7796-d02c-486e-8c6a-dc94ed501ab8.png", caption="Intel ARC 750")
        with st.popover("Press"):
            st.markdown("**Rp. 3.499.000**")
            st.markdown("- Memory Size : 8 GB\
                        \n - Memory Type : GDDR6\
                        \n - Graphics Memory Interface : 256 bit\
                        \n - Graphics Memory Bandwidth : 512 GB/s\
                        \n - Graphics Memory Speed : 16 Gbps\
                        \n - Vertical Segment : Desktop\
                        \n - Xecores : 28\
                        \n - Render Slices : 7\
                        \n - Ray Tracing Units : 28\
                        \n - Intel® Xe Matrix Extensions (Intel® XMX) : Engines448")
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