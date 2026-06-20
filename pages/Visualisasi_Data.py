import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Visualisasi Data",
    page_icon="Logo.png",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

nickel = pd.read_excel(
    "nickel_price_usd_ton_2010_2026.xlsx"
)

copper = pd.read_excel(
    "copper_price_usd_ton_2010_2026.xlsx"
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

st.title("Visualisasi Data Historis")

st.markdown("""
Visualisasi pergerakan harga Nickel dan Copper yang digunakan
sebagai dataset pelatihan model Deep Learning GRU.
""")

# =====================================
# METRIC
# =====================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Jumlah Data",
        f"{len(nickel):,}"
    )

with col2:
    st.metric(
        "Periode",
        "2010-2026"
    )

with col3:
    st.metric(
        "Komoditas",
        "Nickel"
    )

with col4:
    st.metric(
        "Fitur Model",
        "2"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================
# GRAFIK
# =====================================

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=nickel["Date"],
        y=nickel["Price_USD_per_ton"],
        mode="lines",
        name="Nickel (USD/Ton)",
        line=dict(
            color="#9C6B3F",
            width=2
        )
    )
)

fig.add_trace(
    go.Scatter(
        x=copper["Date"],
        y=copper["Price_USD_per_ton"],
        mode="lines",
        name="Copper (USD/Ton)",
        line=dict(
            color="#2A76B8",
            width=2
        )
    )
)

fig.update_layout(
    title="Pergerakan Harga Nickel dan Copper",
    height=600,
    template="plotly_white",
    hovermode="x unified",

    legend=dict(
        orientation="v",
        yanchor="top",
        y=1.20,
        xanchor="right",
        x=1
    ),

    xaxis_title="Tahun",
    yaxis_title="Harga (USD/Ton)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# STATISTIK DATASET
# =====================================

st.markdown("## Ringkasan Dataset")

c1,c2 = st.columns(2)

with c1:

    st.markdown("### Nickel")

    st.dataframe(
        nickel.describe(),
        use_container_width=True
    )

with c2:

    st.markdown("### Copper")

    st.dataframe(
        copper.describe(),
        use_container_width=True
    )

# =====================================
# INSIGHT
# =====================================

st.markdown("## Insight Data")

st.info("""
• Harga Nickel memiliki volatilitas yang lebih tinggi dibanding Copper.

• Tahun 2022 menunjukkan lonjakan harga Nickel yang signifikan.

• Copper cenderung memiliki pola yang lebih stabil.

• Kedua komoditas digunakan sebagai fitur input pada model GRU untuk meningkatkan kemampuan prediksi.
""")
