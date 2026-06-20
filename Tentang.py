import streamlit as st

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon="Logo.png",
    layout="wide"
)

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

/* Sidebar */
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

/* Metric */
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

st.title("Tentang Sistem")

st.markdown("""
Mineral Forecast merupakan aplikasi prediksi harga komoditas mineral
yang dikembangkan menggunakan metode Deep Learning untuk membantu
analisis pergerakan harga Nickel berdasarkan data historis pasar.
""")

st.markdown("<br>", unsafe_allow_html=True)

# =====================================
# METRIC
# =====================================

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

st.markdown("---")

# =====================================
# TUJUAN
# =====================================

st.subheader("Tujuan Pengembangan")

st.markdown("""
Aplikasi ini dikembangkan untuk:

- Membantu memprediksi harga Nickel berdasarkan data historis.
- Memanfaatkan teknologi Deep Learning dalam analisis pasar mineral.
- Memberikan estimasi harga untuk beberapa hari ke depan.
- Menjadi media pembelajaran implementasi Machine Learning dan Deep Learning pada data time series.
""")

# =====================================
# DATASET
# =====================================

st.subheader("Dataset")

st.markdown("""
Dataset yang digunakan berasal dari data historis harga komoditas:

- Nickel (USD/Ton)
- Copper (USD/Ton)

Periode data yang digunakan adalah tahun **2010 hingga 2026**
dengan total lebih dari **3.300 data observasi**.

Copper digunakan sebagai fitur tambahan untuk membantu model
mengenali pola pergerakan harga Nickel secara lebih baik.
""")

# =====================================
# MODEL
# =====================================

st.subheader("Model Deep Learning")

st.markdown("""
Model yang digunakan adalah **Gated Recurrent Unit (GRU)**.

Arsitektur model:

- Input Shape : (30, 2)
- GRU Layer : 64 Unit
- Dropout : 0.2
- GRU Layer : 32 Unit
- Dense Output : 1 Unit

Model dilatih menggunakan:

- Optimizer : Adam
- Loss Function : Mean Squared Error (MSE)
- Epoch : 50
- Batch Size : 32

GRU dipilih karena mampu menangani data time series dengan baik
serta memiliki performa yang efisien dibandingkan model recurrent
lain yang lebih kompleks.
""")

# =====================================
# EVALUASI
# =====================================

st.subheader("Hasil Evaluasi Model")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "RMSE",
        "≈ 1.200"
    )

with col2:
    st.metric(
        "MAPE",
        "1.89%"
    )

with col3:
    st.metric(
        "R² Score",
        "0.9142"
    )

with col4:
    st.metric(
        "Akurasi",
        "98.11%"
    )

st.info("""
Hasil evaluasi menunjukkan bahwa model GRU mampu menghasilkan
prediksi dengan tingkat kesalahan yang rendah dan akurasi yang tinggi,
sehingga cukup baik untuk digunakan dalam analisis harga Nickel.
""")

# =====================================
# TEKNOLOGI
# =====================================

st.subheader("Teknologi yang Digunakan")

st.markdown("""
- Python
- Streamlit
- TensorFlow / Keras
- Pandas
- NumPy
- Scikit-Learn
- Plotly
""")

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption("""
Mineral Forecast © 2026

La Ode Muhammad Sulthan Kologou E1E124008 - Muhamad Aswaad Satria Pratama E1E124073 - Fakultas Teknik - Jurusan Informatika - Universitas Halu Oleo
""")