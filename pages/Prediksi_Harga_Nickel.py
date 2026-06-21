import streamlit as st
import pandas as pd
import numpy as np
import joblib

from datetime import date
from tensorflow.keras.models import load_model

st.set_page_config(
    page_title="Prediksi Harga",
    page_icon="Logo.png",
    layout="wide"
)

# =====================================
# LOAD MODEL & DATA
# =====================================

@st.cache_resource
def load_gru():

    model = load_model(
        "gru_model.h5",
        compile=False
    )

    scaler = joblib.load(
        "scaler.pkl"
    )

    return model, scaler


@st.cache_data
def load_data():

    nickel = pd.read_excel(
        "nickel_price_usd_ton_2010_2026.xlsx"
    )

    copper = pd.read_excel(
        "copper_price_usd_ton_2010_2026.xlsx"
    )

    data = pd.DataFrame()

    data["Nickel"] = nickel[
        "Price_USD_per_ton"
    ]

    data["Copper"] = copper[
        "Price_USD_per_ton"
    ]

    return data


model, scaler = load_gru()

data = load_data()

# =====================================
# PREDICT FUNCTION
# =====================================

def predict_future(days):

    scaled_data = scaler.transform(
        data
    )

    window = scaled_data[-30:].copy()

    predictions = []

    for _ in range(days):

        X = np.array([window])

        pred = model.predict(
            X,
            verbose=0
        )[0][0]

        predictions.append(pred)

        new_row = np.array([
            pred,
            window[-1,1]
        ])

        window = np.vstack([
            window[1:],
            new_row
        ])

    last_pred = predictions[-1]

    temp = np.zeros(
        (1,2)
    )

    temp[0,0] = last_pred
    temp[0,1] = window[-1,1]

    pred_real = scaler.inverse_transform(
        temp
    )[0,0]

    return pred_real

# =====================================
# CSS
# =====================================

st.markdown("""
<style>

.stApp{
    background:#FAFAFA;
}

.block-container{
    padding-top:3rem;
}

[data-testid="stSidebar"]{
    background:#F8F6F3;
    border-right:1px solid #E7DFD7;
}

[data-testid="stSidebarNav"] > div:first-child{
    display:none;
}

[data-testid="stSidebarNav"]::before{
    content:"Mineral Forecast";
    font-size:25px;
    font-weight:700;
    color:#8B5E3C;
    display:block;
    padding:20px 20px 10px 20px;
}

[data-testid="stSidebarNavItems"]{
    padding-top:10px;
}

.main-title{
    font-size:42px;
    font-weight:800;
    color:#2C2C2C;
    margin-bottom:10px;
}

.sub-title{
    font-size:18px;
    color:#666666;
    margin-bottom:35px;
}

.stButton > button{
    width:180px;
    height:52px;
    background:#8B5E3C;
    color:white;
    border:none;
    border-radius:10px;
    font-size:16px;
    font-weight:600;
}

.stButton > button:hover{
    background:#A56F44;
    color:white;
}

div[data-testid="stDateInput"]{
    width:105px !important;
}

[data-testid="stMetric"]{
    background:white;
    border:1px solid #EAEAEA;
    border-radius:18px;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="main-title">
Prediksi Harga Nickel
</div>

<div class="sub-title">
Prediksi harga Nickel menggunakan model Deep Learning GRU berbasis data historis Nickel dan Copper.
</div>
""", unsafe_allow_html=True)

# =====================================
# INPUT
# =====================================

st.subheader("Input Prediksi")

tanggal_prediksi = st.date_input(
    "Tanggal Prediksi",
    value=date.today()
)

prediksi_btn = st.button(
    "Jalankan Prediksi"
)

# =====================================
# HASIL
# =====================================

if prediksi_btn:

    harga_saat_ini = float(
        data.iloc[-1]["Nickel"]
    )

    hari = (
        tanggal_prediksi - date.today()
    ).days

    if hari < 1:
        st.warning(
            "Pilih tanggal setelah hari ini."
        )
        st.stop()

    harga_prediksi = predict_future(
        hari
    )

    selisih = (
        harga_prediksi
        - harga_saat_ini
    )

    persen = (
        selisih
        / harga_saat_ini
    ) * 100

    st.markdown("<br>", unsafe_allow_html=True)

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric(
            "Harga Saat Ini",
            f"USD {harga_saat_ini:,.2f}"
        )

    with col2:
        st.metric(
            "Harga Prediksi",
            f"USD {harga_prediksi:,.2f}"
        )

    with col3:
        st.metric(
            "Perubahan Harga",
            f"USD {selisih:,.2f}"
        )

    with col4:
        st.metric(
            "Perubahan (%)",
            f"{persen:.2f}%"
        )

    st.markdown("---")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric(
            "Model",
            "GRU"
        )

    with col2:
        st.metric(
            "Window",
            "30 Hari"
        )

    with col3:
        st.metric(
            "MAPE",
            "1.89%"
        )

    with col4:
        st.metric(
            "Akurasi",
            "98.11%"
        )

    st.info(
        f"""
        Prediksi dilakukan untuk {hari} hari ke depan menggunakan model GRU
        berbasis data historis Nickel dan Copper.

        Hasil prediksi merupakan estimasi berdasarkan pola historis data
        dan tidak merepresentasikan jaminan harga di masa mendatang.
        """
    )
