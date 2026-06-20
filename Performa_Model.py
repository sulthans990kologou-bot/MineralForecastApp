import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Performa Model",
    page_icon="Logo.png",
    layout="wide"
)

st.markdown("""
<style>

/* Background sidebar */
[data-testid="stSidebar"]{
    background:#F8F6F3;
    border-right:1px solid #E7DFD7;
}

/* Hilangkan tulisan APP */
[data-testid="stSidebarNav"] > div:first-child{
    display:none;
}

/* Judul sidebar */
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

/* Item menu */
[data-testid="stSidebarNav"] a{
    border-radius:12px;
    margin-bottom:6px;
}

/* Menu aktif */
[data-testid="stSidebarNav"] a[aria-current="page"]{
    background:#EEE7DF;
    color:#8B5E3C !important;
    font-weight:700;
}

/* Hover */
[data-testid="stSidebarNav"] a:hover{
    background:#F0E8DF;
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

.block-container{
    padding-top:2rem;
}

/* Judul */
.main-title{
    font-size:42px;
    font-weight:800;
    color:#2C2C2C;
    margin-bottom:8px;
}

.sub-title{
    font-size:18px;
    color:#666666;
    margin-bottom:30px;
}

/* Metric Card */
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

/* Section */
.section-title{
    font-size:28px;
    font-weight:700;
    color:#2D2D2D;
    margin-bottom:15px;
}

/* Box */
.custom-box{
    background:white;
    border-radius:20px;
    padding:25px;
    border:1px solid #EAEAEA;
}

.conclusion-box{
    background:white;
    border:1px solid #EAEAEA;
    border-radius:20px;
    padding:35px;
    margin-bottom:12px;
}

.conclusion-title{
    font-size:32px;
    font-weight:700;
    color:#2D2D2D;
    margin-bottom:20px;
}

.conclusion-text{
    color:#444444;
    font-size:18px;
    line-height:1.9;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="main-title">
Performa Model
</div>

<div class="sub-title">
Perbandingan performa model Deep Learning LSTM dan GRU untuk prediksi harga mineral.
</div>
""", unsafe_allow_html=True)

# =====================================
# DATA
# =====================================

hasil_model = pd.DataFrame({
    "Model": ["LSTM", "GRU"],
    "RMSE": [594.69, 393.04],
    "MAE": [521.70, 316.99],
    "MAPE": [3.16, 1.89],
    "R²": [0.8037, 0.9142]
})

# =====================================
# METRIC CARD
# =====================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Model Terbaik</div>
        <div class="metric-value">GRU</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">RMSE</div>
        <div class="metric-value">393.04</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">MAPE</div>
        <div class="metric-value">1.89%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">R²</div>
        <div class="metric-value">0.9142</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================
# TABEL
# =====================================

st.markdown("""
<div class="section-title">
Hasil Evaluasi Model
</div>
""", unsafe_allow_html=True)

st.dataframe(
    hasil_model,
    use_container_width=True,
    hide_index=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================
# GRAFIK
# =====================================

st.markdown("""
<div class="section-title">
Perbandingan Metrik
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    fig_rmse = go.Figure()

    fig_rmse.add_bar(
        x=hasil_model["Model"],
        y=hasil_model["RMSE"]
    )

    fig_rmse.update_layout(
        title="RMSE",
        template="plotly_white",
        height=400
    )

    st.plotly_chart(fig_rmse, use_container_width=True)

with col2:

    fig_mae = go.Figure()

    fig_mae.add_bar(
        x=hasil_model["Model"],
        y=hasil_model["MAE"]
    )

    fig_mae.update_layout(
        title="MAE",
        template="plotly_white",
        height=400
    )

    st.plotly_chart(fig_mae, use_container_width=True)

col3, col4 = st.columns(2)

with col3:

    fig_mape = go.Figure()

    fig_mape.add_bar(
        x=hasil_model["Model"],
        y=hasil_model["MAPE"]
    )

    fig_mape.update_layout(
        title="MAPE",
        template="plotly_white",
        height=400
    )

    st.plotly_chart(fig_mape, use_container_width=True)

with col4:

    fig_r2 = go.Figure()

    fig_r2.add_bar(
        x=hasil_model["Model"],
        y=hasil_model["R²"]
    )

    fig_r2.update_layout(
        title="R²",
        template="plotly_white",
        height=400
    )

    st.plotly_chart(fig_r2, use_container_width=True)

# =====================================
# KESIMPULAN
# =====================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="conclusion-box">
<div class="conclusion-title">
Kesimpulan
</div>

<div class="conclusion-text">
Model GRU menunjukkan performa terbaik dengan nilai RMSE, MAE,
dan MAPE yang lebih rendah serta nilai R² yang lebih tinggi
dibandingkan model LSTM. Oleh karena itu model GRU dipilih sebagai
model utama untuk prediksi harga mineral.
</div>
</div>
""", unsafe_allow_html=True)

with st.expander("Penjelasan Metrik Evaluasi"):
    st.write("""
**RMSE (Root Mean Square Error)**  
Mengukur besar kesalahan prediksi. Semakin kecil semakin baik.

**MAE (Mean Absolute Error)**  
Mengukur rata-rata selisih absolut antara nilai aktual dan prediksi.

**MAPE (Mean Absolute Percentage Error)**  
Mengukur persentase kesalahan prediksi.

**R² (Coefficient of Determination)**  
Menunjukkan kemampuan model menjelaskan variasi data. Semakin mendekati 1 semakin baik.
""")
