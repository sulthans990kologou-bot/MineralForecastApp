import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Mineral Forecast",
    page_icon="Logo.png",
    layout="wide"
)

st.markdown("""
<style>

/* Sidebar */
[data-testid="stSidebar"]{
    background:#F8F6F3;
}

/* Hilangkan tulisan APP */
[data-testid="stSidebarNav"] > div:first-child{
    display:none;
}

/* Tambahkan header custom ke navigation */
[data-testid="stSidebarNav"]::before{
    content:"Mineral Forecast";
    font-size:25px;
    font-weight:700;
    color:#8B5E3C;
    display:block;
    padding:20px 20px 0px 20px;
}

/* Jarak menu */
[data-testid="stSidebarNavItems"]{
    padding-top:10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# CSS
# =====================================

st.markdown("""
<style>

.stApp{
    background:#FAFAFA;
}

[data-testid="stSidebar"]{
    background:#F8F6F3;
    border-right:1px solid #E7DFD7;
}

section[data-testid="stSidebar"]{
    padding-top:15px;
}

.block-container{
    padding-top:2rem;
}

/* Sidebar Header */
.sidebar-header{
    display:flex;
    align-items:center;
    gap:12px;
    margin-bottom:20px;
}

.sidebar-title{
    color:#8B5E3C;
    font-size:30px;
    font-weight:700;
}

/* Main Title */
.main-title{
    font-size:48px;
    font-weight:800;
    color:#2C2C2C;
    margin-bottom:10px;
}

.sub-title{
    font-size:22px;
    color:#666666;
    margin-bottom:35px;
}

/* Metric */
.metric-card{
    background:#EEE7DF;
    border:1px solid #E4D9CE;
    border-radius:18px;
    padding:24px;
    text-align:center;
}

.metric-label{
    color:#6D6D6D;
    font-size:15px;
}

.metric-value{
    color:#8B5E3C;
    font-size:28px;
    font-weight:700;
    margin-top:10px;
}

/* Info Card */
.info-card{
    background:#F3F7FC;
    border:1px solid #DCE4EF;
    border-radius:18px;
    padding:24px;
    text-align:center;
}

.info-title{
    color:#6D6D6D;
    font-size:15px;
}

.info-value{
    color:#0B4D94;
    font-size:20px;
    font-weight:700;
    margin-top:10px;
}

/* About */
.about-box{
    background:white;
    border:1px solid #EAEAEA;
    border-radius:20px;
    padding:35px;
}

.about-title{
    font-size:32px;
    font-weight:700;
    color:#2D2D2D;
    margin-bottom:20px;
}

.about-text{
    font-size:18px;
    color:#444444;
    line-height:1.9;
}

.section-title{
    font-size:30px;
    font-weight:700;
    color:#2D2D2D;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="main-title">
Sistem Prediksi Harga Mineral Sulawesi Tenggara
</div>

<div class="sub-title">
Platform analisis dan prediksi harga Nickel berbasis Deep Learning menggunakan model LSTM dan GRU
</div>
""", unsafe_allow_html=True)

# =====================================
# METRIC
# =====================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">
            Model Terpilih
        </div>
        <div class="metric-value">
            GRU
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">
            Tingkat Error (MAPE)
        </div>
        <div class="metric-value">
            1.89%
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">
            Koefisien Determinasi (R²)
        </div>
        <div class="metric-value">
            0.9142
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">
            Akurasi Prediksi
        </div>
        <div class="metric-value">
            98.11%
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================
# INFO DATASET
# =====================================

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-title">
            Rentang Dataset
        </div>
        <div class="info-value">
            2010 – 2026
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-title">
            Komoditas Utama
        </div>
        <div class="info-value">
            Nickel
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <div class="info-title">
            Variabel Analisis
        </div>
        <div class="info-value">
            Nickel & Copper
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# =====================================
# GRAFIK HISTORIS
# =====================================

st.markdown("""
<div class="section-title">
Visualisasi Data Historis
</div>
""", unsafe_allow_html=True)

# Load Data
nickel = pd.read_excel(
    "nickel_price_usd_ton_2010_2026.xlsx"
)

copper = pd.read_excel(
    "copper_price_usd_ton_2010_2026.xlsx"
)

nickel["Date"] = pd.to_datetime(
    nickel["Date"]
)

copper["Date"] = pd.to_datetime(
    copper["Date"]
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=nickel["Date"],
        y=nickel["Price_USD_per_ton"],
        name="Nickel (USD/Ton)",
        line=dict(width=3, color="#9C6B3E")
    )
)

fig.add_trace(
    go.Scatter(
        x=copper["Date"],
        y=copper["Price_USD_per_ton"],
        name="Copper (USD/Ton)",
        line=dict(width=3, color="#1F77B4")
    )
)

fig.update_layout(
    height=500,
    template="plotly_white",
    hovermode="x unified",

    title=dict(
        text="Pergerakan Harga Nickel dan Copper",
        x=0.02,
        font=dict(size=22)
    ),

    margin=dict(
        l=50,
        r=30,
        t=80,
        b=30
    ),

    legend=dict(
        orientation="v",
        yanchor="top",
        y=1.20,
        xanchor="right",
        x=1.0,
        bgcolor="rgba(255,255,255,0.85)",
        bordercolor="#E0E0E0",
        borderwidth=1,
        font=dict(size=13)
    ),

    xaxis=dict(
        title="Tahun",
        showgrid=False
    ),

    yaxis=dict(
        title="Harga (USD/Ton)",
        gridcolor="#ECECEC"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================
# ABOUT
# =====================================

st.markdown("""
<div class="about-box">

<div class="about-title">
Tentang Sistem
</div>

<div class="about-text">

Sistem ini dikembangkan untuk mendukung proses analisis dan prediksi harga komoditas mineral di Sulawesi Tenggara, khususnya Nickel. Model prediksi dibangun menggunakan pendekatan Deep Learning melalui algoritma Long Short-Term Memory (LSTM) dan Gated Recurrent Unit (GRU).

Data yang digunakan merupakan data historis harga Nickel dan Copper periode 2010–2026. Berdasarkan hasil evaluasi, model GRU menunjukkan performa terbaik dengan nilai MAPE sebesar <b>1.89%</b>, akurasi prediksi <b>98.11%</b>, dan koefisien determinasi <b>0.9142</b>.

Platform ini dirancang sebagai media analisis yang membantu pengguna memahami pola pergerakan harga mineral serta menghasilkan prediksi yang akurat untuk mendukung pengambilan keputusan.

</div>

</div>
""", unsafe_allow_html=True)
