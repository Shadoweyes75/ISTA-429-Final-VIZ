import streamlit as st
from PIL import Image

#page_config sets up the title of the page (this mainly affects the
#text that appears on the browser tab as far as I know)
#icon makes the icon on the browser tab into a chart emoji
st.set_page_config(
        page_title = "ISTA 429 Vizualization Mockup",
        page_icon = "chart_with_upwards_trend",
        layout = "wide"
    )
#st.markdown writes text onto the page
st.markdown("# ISTA 429 Vizualization Mockup")

#st.columns(n) creates n equally spaced columns on the page 
col1, col2 = st.columns(2)

#adds content to col1
with col1:
    #writes text as header of the graph
    st.header("Graphs")
    st.markdown("### RGB")
    #opens an image file
    image = Image.open("pics/rgbGraphTemp.png")
    #st.image displays an image on the screen
    st.image(image)
    
    st.markdown("### PS2")
    image = Image.open("pics/ps2GraphTemp.png")
    st.image(image)

    st.markdown("### THERMAL")
    image = Image.open("pics/thermalGraphTemp.png")
    st.image(image)
    
with col2:
    st.header("PointCloud")
    #st.selectbox(x, y) creates a dropdown menue
    #x is the title for the dropdown box
    #y is the different dropdown options
    #stores selection into variable, in this case dateIn
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
