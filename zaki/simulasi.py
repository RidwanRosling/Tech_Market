import streamlit as st
import pandas as pd
# Komponen dan harga
def parts():
    """
    Menyimpan semua data komponen dan harga-harganya
    """
    cpu = {
        "Intel Core i5 (LGA 1700)": 2000000,
        "Intel Core i7 (LGA 1700)": 4000000,
        "AMD Ryzen 5 (AM4)": 2500000,
        "AMD Ryzen 7 (AM4)": 4500000,
    }
    mobo = {
        "ASUS TUF B450M-PLUS II (AM4)": 1500000,
        "MSI B550M Pro-VDH (AM4)": 1200000,
        "Gigabyte A520M DS3H V2 (AM4)": 900000,
        "MSI Pro Z690-A Wifi6 (LGA 1700)": 3000000,
        "ASUS Prime Z690-P D4 (LGA 1700)": 3700000,
    }
    ram = {
        "8GB DDR4": 500000,
        "16GB DDR4": 1000000,
        "32GB DDR4": 2000000,
    }
    vga = {
        "NVIDIA GTX 1650": 2500000,
        "NVIDIA RTX 3060": 6000000,
        "AMD Radeon RX 6700": 5000000,
    }
    storage = {
        "SSD 256GB": 600000,
        "SSD 512GB": 1000000,
        "HDD 1TB": 750000,
    }
    psu = {
        "500W Bronze": 500000,
        "650W Gold": 1000000,
        "750W Platinum": 1500000,
    }
    casing = {
        "Casing Standart": 300000,
        "Casing Gaming": 1000000,
    }
    
    return {
        "CPU": cpu,
        "Motherboard": mobo,
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

def matching(cpu_choice, mobo_choice):
    """
    memeriksa kecocokan CPU dan Motherboard berdasarkan socket
    """
    if "LGA 1700" in cpu_choice and "LGA 1700" in mobo_choice:
        return True
    if "AM4" in cpu_choice and "AM4" in mobo_choice:
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

    if cpu_name and mobo_name and not matching(cpu_name, mobo_name):
        st.warning("Socket CPU dan Motherboard tidak cocok!")
        return

    ram_name, ram_price = choose_component("RAM", components["RAM"])
    if ram_name:
        selected_components.append(("RAM", ram_name, ram_price))

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