import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Konfigurasi Halaman
st.set_page_config(
    page_title='Dasborr_Kelompok_&',
    page_icon='',
    layout='wide'
)

st.title("Analisis Kecepatan Arus Permukaan Laut")
st.markdown("Berdasarkan Marine Copernicus: Global Ocean Physics Reanalysis")
st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("### Peta Penelitian")
try:
    img_peta_penelitian = Image.open("peta.png")
    st.image(img_peta_penelitian, caption="Koordinat Peta Wilayah Penelitian N:0.8, E:119.00, S:-3.50, W:117.20", width='stretch')
except FileNotFoundError:
    st.error("Gambar peta.jpg tidak ditemukan di folder. Pastikan file peta.jpg sudah ditaruh di folder yang sama.")

st.markdown("<hr/>", unsafe_allow_html=True)

# ==========================================
# BARIS 1: KPI UTAMA
# ==========================================
st.markdown("### Ringkasan Data")

kpi1, kpi2, kpi3 = st.columns(3) 

with kpi1:
    st.markdown("**Rata-rata Arus 10 Tahun**")
    number1 = "0.195" 
    st.markdown(f"<h1 style='text-align: center; color: #1f77b4;'>{number1} m/s</h1>", unsafe_allow_html=True)

with kpi2:
    st.markdown("**Max Arus 10 Tahun**")
    number2 = "0.655" 
    st.markdown(f"<h1 style='text-align: center; color: #e74c3c;'>{number2} m/s</h1>", unsafe_allow_html=True)

with kpi3:
    st.markdown("**Mean El Niño 23-24 (Tertinggi)**")
    number3 = "0.244" 
    st.markdown(f"<h1 style='text-align: center; color: #f39c12;'>{number3} m/s</h1>", unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)

# ==========================================
# BARIS 2: KPI PERIODE LAINNYA
# ==========================================
st.markdown("### Rata-rata Kecepatan Arus Per Periode")

kpi01, kpi02, kpi03, kpi04, kpi05 = st.columns(5)

with kpi01:
    st.markdown("**Pra Super '14**")
    val1 = "0.164" 
    st.markdown(f"<h2 style='text-align: center; color: #2ecc71;'>{val1}</h2>", unsafe_allow_html=True)

with kpi02:
    st.markdown("**El Niño '15-'16**")
    val2 = "0.137" 
    st.markdown(f"<h2 style='text-align: center; color: #2ecc71;'>{val2}</h2>", unsafe_allow_html=True)

with kpi03:
    st.markdown("**Pasca Super '17**")
    val3 = "0.169" 
    st.markdown(f"<h2 style='text-align: center; color: #2ecc71;'>{val3}</h2>", unsafe_allow_html=True)

with kpi04:
    st.markdown("**Pra El Niño '22**")
    val4 = "0.186" 
    st.markdown(f"<h2 style='text-align: center; color: #2ecc71;'>{val4}</h2>", unsafe_allow_html=True)

with kpi05:
    st.markdown("**Pasca El Niño '25**")
    val5 = "0.147" 
    st.markdown(f"<h2 style='text-align: center; color: #2ecc71;'>{val5}</h2>", unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)

# ==========================================
# BARIS 3: DROPDOWN PETA KONTUR SPASIAL (GAMBAR 01 - 07)
# ==========================================
st.markdown("### Visualisasi Peta Kontur Arus Spasial")

# Dropdown menu untuk memilih peta kontur
peta_option = st.selectbox(
    "Pilih Periode Peta Spasial yang Ingin Ditampilkan:",
    [
        "01. Pra El Niño Super 2014",
        "02. El Niño Super 2015-2016",
        "03. Pasca El Niño Super 2017",
        "04. Pra El Niño 2022",
        "05. El Niño 2023-2024",
        "06. Pasca El Niño 2025",
        "07. Rata-rata Arus 10 Tahun"
    ]
)

# Mapping nama opsi dropdown ke nama file asli (.png)
file_map = {
    "01. Pra El Niño Super 2014": "01__Pra_El_Niño_Super_2014.png",
    "02. El Niño Super 2015-2016": "02_El_Niño_Super_2015-2016.png",
    "03. Pasca El Niño Super 2017": "03_Pasca_El_Niño_Super_2017.png",
    "04. Pra El Niño 2022": "04_Pra_El_Niño_2022.png",
    "05. El Niño 2023-2024": "05_El_Niño_2023-2024.png",
    "06. Pasca El Niño 2025": "06_Pasca_El_Niño_2025.png",
    "07. Rata-rata Arus 10 Tahun": "07_Rata-rata_Arus_10_Tahun.png"
}

img_name = file_map[peta_option]

try:
    img_spasial = Image.open(img_name)
    st.image(img_spasial, caption=f"Peta Kontur Spasial: {peta_option}", width='stretch')
except FileNotFoundError:
    st.error(f"Gambar {img_name} tidak ditemukan di folder. Pastikan nama file sudah sesuai.")

st.markdown("<hr/>", unsafe_allow_html=True)

# ==========================================
# BARIS 4: CHART LAYOUT (GRAFIK TIME SERIES 08 & 09)
# ==========================================
st.markdown("### Grafik Tren Bulanan")

chart1, chart2 = st.columns(2)

with chart1:
    st.markdown("**Perbandingan Kecepatan Arus (Rentang 2 Tahun)**")
    try:
        img_gabungan = Image.open("08_Grafik_Gabungan_6_Periode_Bulanan.png")
        st.image(img_gabungan, width='stretch')
    except FileNotFoundError:
        st.error("Gambar 08_Grafik_Gabungan_6_Periode_Bulanan.png tidak ditemukan di folder.")

with chart2:
    st.markdown("**Tren Jangka Panjang (Arus 10 Tahun)**")
    try:
        img_10tahun = Image.open("09_Grafik_Khusus_10_Tahun.png")
        st.image(img_10tahun, width='stretch')
    except FileNotFoundError:
        st.error("Gambar 09_Grafik_Khusus_10_Tahun.png tidak ditemukan di folder.")

st.markdown("<hr/>", unsafe_allow_html=True)
st.caption("Dibuat menggunakan Python & Streamlit")
st.caption("Oleh Kelompok 7,Naurah:050, Raihan:064, Viki:070, Okta:077, Cinde:080, Khadafi:084, Rio:089, Difa:093")
