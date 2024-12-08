import streamlit as st
from PIL import Image

# Fungsi untuk mengubah ukuran gambar
def resize_image(image_path, size=(300, 300)):
    img = Image.open(image_path)
    img_resized = img.resize(size)
    return img_resized

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
        st.image("zaki/kumpulan gambar/53bc3a1d-cf61-41d7-91f4-2124dbde60d9.jpg", caption="Intel core i9 14900K Box")
        st.button("Go to CPU page", key="switch_button_1", on_click=switch_page, args=("CPU",))
    
    with col2:
        st.header("Gpu")
        st.image(resize_image("zaki/kumpulan gambar/d909e419-85d0-476f-995d-4e2476f310c8.jpg"), caption="MSI GeForce RTX 4090 GAMING X TRIO 24GB GDDR6X")
        st.button("Go to GPU page", key="switch_button_2", on_click=switch_page, args=("GPU",))

    with col3:
        st.header("Casing")
        st.image("zaki/kumpulan gambar/b70fc2df-20f4-4626-ad91-1de714210895.jpg", caption="TECWARE FLATLINE TG MK2")
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
        st.image(resize_image("zaki/kumpulan gambar/cea0c491-d4f5-43da-974b-cb5c06597b95.jpg"), caption="AMD Ryzen 9 5900X")
        with st.popover("Press"):
            st.markdown("**Rp. 5.730.000**")
            st.markdown("- 12 Core\n - 24 threads\n - Base clock 3.4Ghz\n - Max clock up to 4.8GhzTotal L2 Cache 6MB\n - Total L3 Cache 64MB\n - Unlocked Yes\
                        \n - CMOS TSMC 7nm FinFET\n - Package AM4\n - PCI Express Version PCIe 4.0\n - Thermal Solution (PIB) Not included\n - Default TDP / TDP 105W")
            st.button("Order now", key="cpu1")


    with cpu2:
        st.subheader("Intel pentium Gold")
        st.image("zaki/kumpulan gambar/20200611151837_th.jpg", caption="intel pentium G5420")
        with st.popover("Press"):
            st.markdown("**Rp.840.000**")
            st.markdown("- CPU Socket Type : LGA 1151\n - Processors Generation : 9th Gen\n - Family : Coffeelake\n - Cores : 2\n\
                        - Threads : 4\n - Operating Frequency : 3.8GHz\n - Max Turbo Frequency : -\n - Cache : 4 MB\n - Manufacturing Tech : 14 nm\n - Integrated Graphics : Intel UHD Graphics 610\
                        \n - Thermal Design Power : 54 W\n - Thermal Solution (Cooler) : Included")
            st.button("Order now", key="cpu2")


    with cpu3:
        st.subheader("Amd ryzen 3000 series")
        st.image(resize_image("zaki/kumpulan gambar/f9b52508-10b7-416f-85fb-a6dfc883c0a2.jpg"), caption="Ryzen 5 3600")
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


    with cpu4:
        st.subheader("Intel gen 10 series")
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
        st.subheader("Amd Rx series")
        st.image(resize_image("zaki/kumpulan gambar/1024.png"), caption="Radeon RX 580 8G")
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

    with gpu2:
        st.subheader("Nvidia G series")
        st.image(resize_image("zaki/kumpulan gambar/1024 (1).png"), caption="GTX 1660 Gaming X 6G")
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


    with gpu3:
        st.subheader("Intel arc series")
        st.image(resize_image("zaki/kumpulan gambar/e60d7796-d02c-486e-8c6a-dc94ed501ab8.png"), caption="Intel ARC 750")
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


    with gpu4:
        st.subheader("Amd Radeon RX")
        st.image("zaki/kumpulan gambar/amd radeon RX 6700xt.png", caption="Amd radeon RX 6700xt")
        with st.popover("Press"):
            st.markdown("**Rp. 3.821.000**")
            st.markdown("- Memory Size : 12 GB\
                        \n - Memory Type : GDDR6\
                        \n - Boost clock : up to 2622 Mhz\
                        \n - Game Clock : up to 2514 Mhz\
                        \n - Stream processors : 2560\
                        \n - Process technology : 7 nm\
                        \n - Memory bus : 192 bit\
                        \n - Memory bandwith(GB/sec) : 386GB/s\
                        \n - Card bus : PCI-E 4.0 x 16\
                        \n - Digital max resolution : 7680x4320\
                        \n - Multi view : 4\
                        \n - Card size : L = 281, W = 115, H = 49 mm\
                        \n - PCB Form = ATX\
                        \n - Dirctx : 12 ultimate\
                        \n - OpenGL : 4.6\
                        \n - Power requirement : 650W\
                        \n - Power connectors : 8 pin*1, 6pin*1\
                        \n - Output : DisplayPort 1.4a *2 HDMI 2.1*2")
            st.button("Order now", key="gpu4")


elif st.session_state.page == "SSD":
    st.title("SSD")
    st.write("**SSD (Solid State Drive)** adalah jenis perangkat penyimpanan data yang menggunakan memori\
              flash untuk menyimpan informasi secara permanen. Tidak seperti HDD (Hard Disk Drive) yang\
              menggunakan piringan magnetik dan kepala baca/tulis mekanis, SSD tidak memiliki komponen\
              mekanis yang bergerak. Hal ini membuat SSD lebih cepat, lebih tahan lama,\
              dan lebih hemat daya dibandingkan HDD.")

    ssd1, ssd2, ssd3, ssd4 = st.columns(4)

    with ssd1:
        st.subheader("SSD Sata")
        st.image(resize_image("zaki/kumpulan gambar/4ccbb8c4-b46b-4382-93b0-5744db37c59d.jpg"), caption="Samsung SSD 870 EVO 500GB Sata 3")
        with st.popover("Press"):
            st.markdown("**Rp.821.000**")
            st.markdown("- Dimension (WxHxD) : 3.94 X 2.75  X 0.27\
                        \n - Weight : 89g.\
                        \n - Performance : Speed Read/write speeds of up to 560/530 MB/s\
                        \n - Encryption : Class 0 (AES 256) TCG/Opal v2.0, MS eDrive (IEEE1667)\
                        \n - Type Interface : SATA 6 Gb/s Interface, compatible with SATA 3 Gb/s & SATA 1.5 Gb/s interface\
                        \n - Usage Application : Client PCs / Laptops\
                        \n - Sequential Read Speed : Up to 560 MB/s Sequential Read\
                        \n - Sequential Write Speed : Up to 530 MB/s Sequential Write\
                        \n - Cache Memory : Samsung 512 MB Low Power DDR4 SDRAM\
                        \n - Trim Support : Yes\
                        \n - S.M.A.R.T. Support : yes\
                        \n - GC (Garbage Collection) : Auto Garbage Collection Algorithm\
                        \n - WWN Support : yes\
                        \n - Device Sleep Mode Support : Yes\
                        \n - Average Power Consumption (system level) : Average: 2.2 W *Maximum: 3.5 W (Burst mode)\
                        \n - Power consumption (Idle) : Max. 30 mW")
            st.button("Order now", key="ssd1")

    with ssd2:
        st.subheader("SSD NVMe")
        st.image("zaki/kumpulan gambar/9c4fd703-0174-49d8-bb13-3a1e6f80cd63.png", caption="Crucial SSD P3 Plus PCIe Gen4 M.2 NVMe")
        with st.popover("Press"):
            st.markdown("**Rp.690.000**")
            st.markdown("Size : 500GB, Read/write: 4700/1900Mb/s, TBW 110")
            st.button("Order now", key="ssd2")

    with ssd3:
        st.subheader("SSD SATA")
        st.image("zaki/kumpulan gambar/d136092d-c8a8-45cd-b548-8590dec76d04.jpg", caption="SSD KYO KAIZEN 128GB SATA III 2.5 6GB/S SSD SATA 3")
        with st.popover("Press"):
            st.markdown("**Rp.145.000**")
            st.markdown("- Tipe: 2,5 SATA3 6GB/S\
                        \n - Kapasitas : 128GB\
                        \n - Flash : 3D NAND FLASH\
                        \n - Write Speed : Up To 570 MB/s\
                        \n - Read Speed : Up To 470 MB/s\
                        \n - Power Consumption : 5 V")
            st.button("Order now", key="ssd3")

    with ssd4:
        st.subheader("SSD NVMe")
        st.image("zaki/kumpulan gambar/fd2e1dee-335d-465b-a9e3-701c2238c603.jpg", caption="ACER FA100 M.2 NVMe PCIe Gen3 x4 SSD - 1TB")
        with st.popover("Press"):
            st.markdown("**Rp.919.000**")
            st.markdown("- interface : PCIe gen3 x4, NVMe1.4\
                        \n - Form factor : M.2 2280\
                        \n - Max. sequential reading speed (MB/s) : 3300\
                        \n - Max. sequential writing speed (MB/s) : 2700\
                        \n - Random read speed (IOPS) : 402K\
                        \n - Random write speed (IOPS) : 261K\
                        \n - Treabytes written (TBW) : 600TBW")
            st.button("Order now", key="ssd4")


elif st.session_state.page == "RAM":
    st.title("RAM")
    st.write("**RAM (Random Access Memory)** adalah jenis memori komputer yang digunakan\
              untuk menyimpan data dan instruksi sementara yang sedang digunakan oleh\
              prosesor. RAM berfungsi sebagai (memori kerja) komputer yang memungkinkan\
              akses data yang cepat. Tidak seperti penyimpanan permanen seperti SSD atau\
              HDD, data pada RAM bersifat volatil, yang berarti akan hilang ketika komputer dimatikan")
    
    ram1, ram2, ram3, ram4 = st.columns(4)

    with ram1:
        st.subheader("Ram DDR4")
        st.image("zaki/kumpulan gambar/2e8569ef-3f2a-4142-8b4b-827d1374c96c.png", caption="RAM Kingston Fury Beast RGB DDR4 3200MHz (PC25600) 8GB (1x8GB)")
        with st.popover("Press"):
            st.markdown("**Rp.375.000**")
            st.markdown("- CL(IDD) 17 cycles\
                        \n - Row Cycle Time (tRCmin) 45.75ns(min.)\
                        \n - Refresh to Active/Refresh 350ns(min.)\
                        \n - Command Time (tRFCmin)\
                        \n - Row Active Time (tRASmin) 32ns(min.)\
                        \n - UL Rating 94 V - 0\
                        \n - DDR4 3200MHz")
            st.button("Order now", key="ram1")

    with ram2:
        st.subheader("Ram DDR3")
        st.image("zaki/kumpulan gambar/d7e77d83-d5db-42e9-a2a6-a3923df5793d.jpg", caption="RAM EnPC LONGDIMM DDR3 8GB 1600Mhz")
        with st.popover("Press"):
            st.markdown("**Rp.92.000**")
            st.markdown("- Memory Type : DDR3\
                        \n - Form Factor : U-DIMM\
                        \n - Capacity : 8GB\
                        \n - Speeds : 1600\
                        \n - Dimensions (LxWxH) : 133 x 30 x 3 mm")
            st.button("Order now", key="ram2")

    with ram3:
        st.subheader("Ram DDR4")
        st.image("zaki/kumpulan gambar/eb13cfa9-5667-46ef-8d48-8868723cf4f7.jpg", caption="Team Ram T-Create Expert 16GB Kit (8GBX2) DDR 4 PC3600")
        with st.popover("Press"):
            st.markdown("**Rp. 495.000**")
            st.markdown("- Capacity : 16GB (8GBx2)\
                        \n - Module Type : 288 Pin Unbuffered DIMM Non ECC\
                        \n - Frequency : 3600\
                        \n - Latency : CL18-22-22-42\
                        \n - Data Transfer : 28,800 MB/s\
                        \n - Bandwidth : (PC4 28800)\
                        \n - Voltage : 1.35V\
                        \n - Dimensions : 32(H) x 134(L) x 6.5(W)mm\
                        \n - Heat Spreader : Aluminum heat spreader")
            st.button("Order now", key="ram3")
    
    with ram4:
        st.subheader("Ram DDR5")
        st.image("zaki/kumpulan gambar/1eb5bb92-3439-4b10-b2cb-ad031736ae25.png", caption="PREDATOR VESTA II DDR5 6000 MHz RGB U-DIMM [Desktop RAM] - 32GB KIT")
        with st.popover("Press"):
            st.markdown("**Rp.1.899.000**")
            st.markdown("- Model Name : Predator Vesta II RGB Memory\
                        \n - DRAM : DDR5 RGB UDIMM\
                        \n - Capacity : 32GB (16GB x2) // 64GB (32GB x2)\
                        \n - Frequency : 6000MHz\
                        \n -  Timing :\
                        \n  32GB: CL32\
                        \n  64GB: CL30\
                        \n - Working Voltage : 1.35 V\
                        \n - Working Temperature : 0C to 85C\
                        \n - Storage Temperature : -55C to 100C")
            st.button("Order now", key="ram4")


elif st.session_state.page == "PSU":
    st.title("PSU")
    st.write("**PSU (Power Supply Unit)** adalah komponen pada komputer yang berfungsi\
              untuk mengubah arus listrik dari sumber daya (biasanya listrik AC dari\
              stopkontak) menjadi arus listrik DC yang stabil untuk mendukung operasi\
              komponen-komponen di dalam komputer, seperti motherboard, prosesor (CPU),\
              kartu grafis (GPU), RAM, dan penyimpanan")
    
    psu1, psu2, psu3 = st.columns(3)

    with psu1:
        st.subheader("PSU 550W")
        st.image("zaki/kumpulan gambar/9126088_a9b9de8d-fb27-411f-bc8e-cfe52048fe45_700_700.jpg", caption="Cooler Master MWE 550 V2 - 550W")
        with st.popover("Press"):
            st.markdown("**Rp. 770.000**")
            st.markdown("- MODEL MPE-5501-ACABW-B\
                        \n - ATX VERSION ATX 12V V2.52\
                        \n - PFC Active PFC\
                        \n - INPUT VOLTAGE 200-240Vac\
                        \n - INPUT CURRENT 5A\
                        \n - INPUT FREQUENCY 50-60Hz\
                        \n - DIMENSIONS (L X W X H) 140 x 150 x 86 mm\
                        \n - FAN SIZE 120mm\
                        \n - FAN BEARING HDB\
                        \n - FAN SPEED 1500 RPM\
                        \n - NOISE LEVEL @ 20% 13.8 dBA\
                        \n - NOISE LEVEL @ 50% 18.4 dBA\
                        \n - NOISE LEVEL @ 100% 31.2 dBA\
                        \n - EFFICIENCY 88% Typically\
                        \n - 80 PLUS RATING 80 PLUS Bronze EU 230V\
                        \n - ERP 2014 LOT 3 Yes\
                        \n - POWER GOOD SIGNAL 100-500ms\
                        \n - HOLD UP TIME >14ms at 100% Full Load@230Vac\
                        \n - MTBF >100,000 Hours\
                        \n - PROTECTIONS OVP, OPP, SCP, UVP, OTP\
                        \n - REGULATORY CCC, CE, TUV-RH, RCM, EAC, cTUVus, FCC, BSMI, KC, CB\
                        \n - ATX 24-PIN CONNECTORS 1\
                        \n - EPS 4+4 PIN CONNECTORS 1\
                        \n - SATA CONNECTORS 6\
                        \n - PERIPHERAL 4-PIN CONNECTORS 3\
                        \n - PCI-E 6+2 PIN CONNECTORS 2\
                        \n - SERIE MWE Bronze Series\
                        \n - 80 PLUS Bronze\
                        \n - MODULAR Non Modular\
                        \n - WATTAGE 500 to 750W")
            st.button("Order now", key="psu1")

    
    with psu2:
        st.subheader("PSU 650W")
        st.image("zaki/kumpulan gambar/aa9ab9f6-4514-4664-9a6a-4c0ed60fc8e3.jpg", caption="Aerocool LUX 650W 80+ Bronze ATX PSU")
        with st.popover("Press"):
            st.markdown("**RP. 649.000**")
            st.markdown("- AC Input 200-240VAC 5A 50-60Hz\
                        \n - DC Output +3.3V +5V +12V -12V +5VSB\
                        \n - Max Current 20A 20A 50A 0.3A 2.5A\
                        \n - Max.Combined Power 120W 600W 3.6W 12.5W\
                        \n - 650W\
                        \n - EAN CODE 4718009156241")
            st.button("Order now", key="psu2")


    with psu3:
        st.subheader("PSU 750W")
        st.image("zaki/kumpulan gambar/40877f9f-1898-4e03-99d4-faf44b789030.jpg",  caption="CV Series CV750 750 Watt 80 Plus Bronze")
        with st.popover("Press"):
            st.markdown("**Rp. 939.000**")
            st.markdown("- Weight 1.9\
                        \n - Adjustable Single/Multi 12V Rail No\
                        \n - ATX Connector 1\
                        \n - ATX12V Version v2.31\
                        \n - Continuous power W 750 Watts\
                        \n - Fan bearing technology Sleeve\
                        \n - Fan size mm 120mm\
                        \n - MTBF hours 100,000 hours\
                        \n - Multi-GPU ready No\
                        \n - Warranty 3 Year\
                        \n - PSU Form Factor ATX\
                        \n - Zero RPM Mode No")
            st.button("Order now", key="psu3")


elif st.session_state.page == "Casing":
    st.title("Casing")
    st.write("Casing PC adalah komponen penting dalam sistem komputer yang sering dianggap hanya sebagai\
              pelindung fisik. Namun, casing memiliki peran lebih besar daripada itu.")
    
    case1, case2, case3 = st.columns(3)

    with case1:
        st.subheader("Case sades")
        st.image("zaki/kumpulan gambar/20190829131515_th.jpg", caption="Case Sades Seth")
        with st.popover("Press"):
            st.markdown("**Rp. 450.000**")
            st.markdown(" - M/B Form Factor:ATX,MICRO ATX,ITX\
                        \n - Front I/O Ports:USB3.0+USB1.0*2+AUDIO+MIC\
                        \n - Dimensions of chassis:W190xH470xD415mm,with black painting on Inner chassis\
                        \n - Bottom installation of PSU: YES\
                        \n - Card reader:No,arcylic side panel\
                        \n - Convex side panel:No\
                        \n - Driver Bays:5.25″ eksternal*0;3.5″ HDD*2;2.5″SSD*2\
                        \n - Support CPU Up to:160mm\
                        \n - Support VGA Cards Up to:350mm\
                        \n - PCI slot:7, pre-installed holes for Water Cooling:240\
                        \n - HDD/SSD:2/2 PCS\
                        \n - Support hidden cables:Yes")
            st.button("Order now", key="case1")

    with case2:
        st.subheader("Case sades")
        st.image("zaki/kumpulan gambar/20180419113802_th.jpg", caption="Case Sades Sphinx White")
        with st.popover("Press"):
            st.markdown("**Rp. 455.000**")
            st.markdown("- Color: White\
                        \n - Dimensions: 380(L)x185(W)x425(H)\
                        \n - Material: 0.7mm thick SPCC black steel plate\
                        \n - Inner construction : 0.5mm steel plate\
                        \n - Motherboard: ATX,M-ATX, ITX\
                        \n - HD Device: 23.5,42.5\
                        \n - Heat Removal System:\
                        \n - Pront Plate : 2x12cm fan(Optional)\
                        \n - Back Plate: 1x12cm fan(Optional)\
                        \n - Front I/O: USB 3.01, USB 2.02,headset 1x\
                        \n - Power Supply: PSII,PSU(ATX)\
                        \n - Net wet: 4.3kg\
                        \n - PCI Expension slots: 7\
                        \n - Support VGA Card lenght: 370mm\
                        \n - Support CPU Cooler Height: 150mm")
            st.button("Order now", key="case2")

    with case3:
        st.subheader("Case Db")
        st.image("zaki/kumpulan gambar/20151105161736.jpg", caption="Casing Digital Alliance 335B")
        with st.popover("Press"):
            st.markdown("**Rp. 395.000**")
            st.markdown("Motherboard Support	Micro ATX\
                        \n                      Standard ATX\
                        \n - Liquid Cooling Capable	No\
                        \n - Power Supply Supported	Standard PS2\
                        \n - Power Supply Included	Yes\
                        \n - Dimension (H*W*D)	370(L)x180(W)x430(H) mm\
                        \n - Net Weight	4.55 + 10Kgs\
                        \n - Accecories	Screw Parts, Power Cable")
            st.button("Order now", key="case3")