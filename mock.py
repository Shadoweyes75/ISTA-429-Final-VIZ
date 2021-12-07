import streamlit as st
from PIL import Image

#makes a dropdown box for all plants that match plot/geno/treat values
#plot is the plot the plant is found in
#geno is genotype of the plant wanted
#treat is the treatmen of the plant
def get_plants_for_dropdown(plot, geno, treat):
        plantIn = st.selectbox(
            "Plants",
            ("plant1","plant2","plant3"))
        return plantIn


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
    plant = st.text_input("Plant Name",
                              "Plant 1")
    #st.selectbox(x, y) creates a dropdown menue
    #x is the title for the dropdown box
    #y is the different dropdown options
    #stores selection into variable, in this case dateIn
    plotIn = st.selectbox(
        "Plot",
        ("-","1", "2", "3", "4"))
    treatmentIn = st.selectbox(
        "Treatment",
        ("-","1", "2", "3"))
    genoIn = st.selectbox(
        "Genotype",
        ("-","gen1", "gen2", "gen3", "gen4"))
    if(plotIn != "-" or treatmentIn != "-" or genoIn != "-"):
        plant = get_plants_for_dropdown(plotIn, treatmentIn, genoIn)
    

    image2 = Image.open("pics/lettuceTemp.jpg")
    st.image(image2)
