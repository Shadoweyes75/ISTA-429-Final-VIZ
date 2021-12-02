import streamlit as st
from PIL import Image

st.set_page_config(
        page_title = "ISTA 429 Vizualization Mockup",
        page_icon = "chart_with_upwards_trend",
        layout = "wide"
    )

st.markdown("# ISTA 429 Vizualization Mockup")


col1, col2 = st.columns(2)


with col1:
    st.header("Graphs")
    st.markdown("### RGB")
    image = Image.open("pics/rgbGraphTemp.png")
    st.image(image)
    
    st.markdown("### PS2")
    image = Image.open("pics/ps2GraphTemp.png")
    st.image(image)

    st.markdown("### THERMAL")
    image = Image.open("pics/thermalGraphTemp.png")
    st.image(image)
    
with col2:
    st.header("PointCloud")
    dateIn = st.selectbox(
        "Date",
        ("1-1-0000", "1-2-0000", "1-3-0000", "1-4-0000"))
    genoIn = st.selectbox(
        "Genotype",
        ("gen1", "gen2", "gen3", "gen4"))
    plantIn = st.selectbox(
        "Individial Plant",
        ("Plant 1", "Plant 2", "Plant 3", "Plant 4"))

    image2 = Image.open("pics/lettuceTemp.jpg")
    st.image(image2)
