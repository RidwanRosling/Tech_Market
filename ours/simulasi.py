import streamlit as st
import pandas as pd
# Komponen dan harga
def parts():
    """
    Menyimpan semua data komponen dan harga-harganya
    """
    cpu = {
        "AMD Ryzen 5 3600 (AM4)": 1100000,
        "AMD Ryzen 5 4500 (AM4)": 1200000,
        "AMD Ryzen 5 4600G (AM4)": 1500000,
        "AMD Ryzen 9 5900x (AM4)": 5700000,
        "Intel Core i5 11400 (LGA 1700)": 2100000,
        "Intel Core i5 12400F (LGA 1700)": 1500000,
        "Intel Core i9 14900KS (LGA 1700)": 12000000,
        "Intel Pentium G5420 (LGA 1151)": 245000,
        "Intel Core i3 4170 (LGA 1150)": 135000,
        "AMD Ryzen 5 5500 (AM4)": 1320000,
    }
    mobo = {
        "ASROCK B550M PRO4 (AM4)(DDR4)(M-ATX)": 1548000,
        "ASRock H470M-HDV/M.2 (LGA 1200)(DDR4)(M-ATX)" : 845000,
        "MSI B450 TOMAHAWK MAX (AM4)(DDR4)(ATX)": 1809000,
        "MSI A520M-A Pro (AM4)(DDR4)(M-ATX)": 865000,
        "Kyo Kaizen H110 LGA 1151 (LGA 1151)(DDR4)(M-ATX)": 599000,
        "Biostar B550MH (AM4)(DDR4)(M-ATX)": 1050000,
        "MSI PRO H610M-S WIFI DDR4 (LGA 1700)(DDR4)(M-ATX)": 1245000,
        "Asus Rog Maximus Z790 HERO (LGA 1700)(DDR5)(ATX)": 12140000,
        "VenomRX Intel H81 M.2 (LGA 1150)(DDR3)(M-ATX)": 545000,
    }
    fan_cooler = {
        "Deepcool AG400 Plus (AIR)": 310000,
        "Prime Polar 240T V2.0 (AIO)(M-ATX)": 750000,
        "Cooler Master Hyper 212 Black Edition (AIR)": 750000,
        "PC Cooler RT500 DIGITAL ARGB BK (AIR)": 400000,
        "Kyo Thermalease GT390 (AIR)": 200000,
        "MSI MEG CoreLiquid S360 (AIO)(ATX)": 3950000,
        "Raptor X2000 (AIR)": 85000,
        "Fan Cooler AM4 Original (AIR)": 60000,
    }
    ram = {
        "Teamgroup DDR4 16GB (DDR4)": 555000,
        "Corsair Vengeance LPX 16GB 2x8GB DDR4-3200 (DDR4)": 688000,
        "V-Gen Tsunami DDR4 PC2400 3000MHz 16GB Dual Channel (DDR4)": 1017000,
        "Crucial DDR4 8GB (DDR4)": 290000,
        "Kingston Fury DDR4 3200MHz 16GB (DDR4)": 474000,
        "G.Skill Trident Z5 2X16 (DDR5)": 1755000,
        "VenomRX DDR3 PC12800 8GB (DDR3)": 100000,
        "Corsair DDR4 Vengeance LPX PC21000 16GB (DDR4)": 722000,
    }
    vga = {
        "Asus GT 710 2GB": 580000,
        "Biostar Radeon RX 550 4GB DDR5": 1500000,
        "Gigabyte GeForce RTX 3060 WINDFORCE OC 12GB": 4700000,
        "Gigabyte RTX 3050": 3150000,
        "MSI RTX 4090 XTRIO 24GB": 33100000,
        "NVIDIA GeForce GTX 1660 Ti": 1855000,
        "Radeon RX 580 8GB": 1441000,
        "VenomRX Geforce GTX 1660 Ti 6GB GDDR6": 2765000,
        "VenomRX Geforce GTX 750 Ti 4GB DDR5": 979000,
        "VenomRX Radeon RX 580 8GB DDR5": 1364000,
    }
    storage = {
        "Acer RE100 SSD 512GB SATA III": 550000,
        "Kyo Kaizen M.2 512GB": 440000,
        "Samsung 970 EVO 500GB NVMe SSD": 1100000,
        "Samsung SSD 990 PRO 1TB": 2300000,
        "SSD Ace Power 512GB": 550000,
        "Teamgroup SSD 128GB": 225000,
        "Transcend 225S 1TB 2.5 SATA3": 1000000,
        "V-Gen Rescue 960GB SATA3": 784000,
        "V-Gen SSD M.2 NVMe 1TB": 800000,
    }
    psu = {
        "FSP HV PRO 550W": 660000,
        "Aerocool LUX 550W 80+ Bronze": 540000,
        "Corsair CX550M 550W 80+ Bronze Certified": 1100000,
        "Gigabyte P550B 550W 80+ Bronze": 630000,
        "Aerocool United 500W": 460000,
        "PSU Ace Power FP550-550W 80+ Bronze": 597000,
        "MSI MEG Ai1300P 1300W": 5039000,
        "GameMax PSU 450W GP-450 80 + Bronze": 515000,
    }
    casing = {
        "Aerocool CS-107 FRGB Acrylic Panel (M-ATX)": 578000,
        "Armaggeddon Aquaron Duplex M-ATX Black (M-ATX)": 490000,
        "Digital Alliance N30S V2 M-ATX (M-ATX)": 390000,
        "MSI MAG PANO M100R BLACK (ATX)": 1494000,
        "Neotez Deus (M-ATX)": 450000,
        "NYK Nemesis Notus T68 (M-ATX)": 345000,
        "NZXT H510 (ATX)": 1197000,
        "Paradox Gaming Case Antartica (ATX)": 450000,
        "Simbadda SIM V-3162 + PSU 380W (ATX)": 395000,
    }
    
    return {
        "CPU": cpu,
        "Motherboard": mobo,
        "Fan Cooler": fan_cooler,
        "RAM": ram,
        "Graphic Card": vga,
        "Storage": storage,
        "Power Supply": psu,
        "Casing": casing
    }

def choose_component(component_name, options):
    """
    nampilin daftar komponen dan meminta pengguna memilih komponennya
    mengembalikan (return) nama dan harga komponen yang dipilih
    """
    # Menambahkan pilihan kosong (placeholder) di awal daftar
    options_list = ["Pilih komponen"] + list(options.keys())
    
    selected_component = st.selectbox(f"Pilih {component_name}:", options_list)
    if selected_component != "Pilih komponen":
        return selected_component, options[selected_component]
    else:
        return None, 0

def matching(cpu_choice, mobo_choice, ram_choise):
    """
    memeriksa kecocokan CPU dan Motherboard berdasarkan socket
    """
    if "LGA 1700" in cpu_choice and "LGA 1700" in mobo_choice:
        return True
    if "LGA 1151" in cpu_choice and "LGA 1151" in mobo_choice:
        return True
    if "LGA 1150" in cpu_choice and "LAG 1150" in mobo_choice:
        return True
    if "LGA 1200" in cpu_choice and "LGA 1200" in mobo_choice:
        return True
    if "AM4" in cpu_choice and "AM4" in mobo_choice:
        return True
    if "DDR5" in mobo_choice and "DDR5" in ram_choise:
        return True
    if "DDR4" in mobo_choice and "DDR4" in ram_choise:
        return True
    if "DDR3" in mobo_choice and "DDR3" in ram_choise:
        return True
    return False

def main():
    st.title("Simulasi Perakitan Komputer")
    components = parts()
    selected_components = []

    # Pemilihan komponen
    cpu_name, cpu_price = choose_component("Processor", components["CPU"])
    if cpu_name:
        selected_components.append(("Processor", cpu_name, cpu_price))

    mobo_name, mobo_price = choose_component("Motherboard", components["Motherboard"])
    if mobo_name:
        selected_components.append(("Motherboard", mobo_name, mobo_price))

    if cpu_name and mobo_name and not matching(cpu_name, mobo_name, ""):
        st.warning("Socket CPU dan Motherboard tidak cocok!")
        return

    fan_cooler_name, fan_cooler_price = choose_component("Fan Cooler", components["Fan Cooler"])
    if fan_cooler_name:
        selected_components.append(("Fan Cooler", fan_cooler_name, fan_cooler_price))

    ram_name, ram_price = choose_component("RAM", components["RAM"])
    if ram_name:
        selected_components.append(("RAM", ram_name, ram_price))

    if mobo_name and ram_name and not matching(mobo_name, "",ram_name):
        st.warning("Socket RAM dan Motherboard tidak cocok!")

    vga_name, vga_price = choose_component("Graphic Card", components["Graphic Card"])
    if vga_name:
        selected_components.append(("Graphic Card", vga_name, vga_price))

    storage_name, storage_price = choose_component("Storage", components["Storage"])
    if storage_name:
        selected_components.append(("Storage", storage_name, storage_price))

    psu_name, psu_price = choose_component("Power Supply", components["Power Supply"])
    if psu_name:
        selected_components.append(("Power Supply", psu_name, psu_price))

    casing_name, casing_price = choose_component("Casing", components["Casing"])
    if casing_name:
        selected_components.append(("Casing", casing_name, casing_price))

    # menampilkan tabel komponen yang dipilih dan total harga
    if selected_components:
        st.subheader("Komponen yang dipilih:")
        df = pd.DataFrame(selected_components, columns=["Komponen", "Nama", "Harga"])
        st.dataframe(df)

        # total harga
        total_price = df["Harga"].sum()
        st.write(f"\n**Total Harga**: Rp {total_price:,}")
    
    st.write("Terima kasih telah menggunakan simulasi ini!")

main()