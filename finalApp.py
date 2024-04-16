import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Water Quality Project", layout="wide", page_icon="🌊", initial_sidebar_state="expanded")

IMAGE_JESUS = "media/JesusPic.jpg"
IMAGE_ANGIE = "media/AngiePic.jpg"
IMAGE_ERNESTO = "media/JesusPic.jpg"
IMAGE_MICHEL = "media/JesusPic.jpg"
IMAGE_FIU = "media/FIU_LOGO.png"
IMAGE_BANNER = "media/Water_Banner.jpg"


# create change font size button
# add images
# sidebar

#Define function to load media
def load_media(column, file_path, caption):
    with column:
        if file_path.endswith(".jpeg") or file_path.endswith(".PNG")or file_path.endswith(".jpg"):
            column.image(file_path, caption=caption,width=150)
        elif file_path.endswith(".mp4"):
            column.video(file_path)
        elif file_path.endswith(".mp3"):
            column.audio(file_path)
def scatter_plots(df):
    st.subheader("Scatter Plot")
    fig = px.scatter(df, x="Depth m", y="Temp °C", size="pH", color="ODO mg/L")
    st.plotly_chart(fig)

def maps(df):
    st.subheader("Maps")
    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_data=["Depth m", "pH", "Temp °C", "ODO mg/L"], zoom=15)
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)

def line_plots(df):
    st.subheader("Line Plot")
    color = st.color_picker("Choose a color", "#081E3F")
    fig = px.line(df, x=df.index, y="ODO mg/L")
    fig.update_traces(line_color=color)
    st.plotly_chart(fig)

def three_d_plots(df):
    st.subheader("3D Plot")
    fig = px.scatter_3d(df, x="Longitude", y="Latitude", z="Depth m", color="ODO mg/L")
    fig.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig)

def raw_data(df):
    st.subheader("Raw Data")
    st.dataframe(df)
    st.subheader("Descriptive Statistics")
    st.dataframe(df.describe())

# Define functions to render different pages
def render_home_page():
    st.image(IMAGE_BANNER, use_column_width=True)
    st.title("HCI FINaAL Project")
    st.title("Home")
    st.subheader("Sub Header Here")
    st.write("Paragraph Here")
    st.divider()
    st.subheader("Sub Header 2 Here")
    st.write("Paragraph 2 Here")
    st.divider()





def render_About():
    st.title("About")
    st.subheader("Get to know the team!")
    st.divider()
    col1, col2, col3, col4 = st.columns(4)
    load_media(col1, IMAGE_JESUS, "Jesus Elespuru, Senior, Back end, Data-Collection, Florida International University")
    load_media(col2, IMAGE_ANGIE, "Angie Martinez, Senior, Front end, Data-Collection, Florida International University")
    load_media(col3, IMAGE_ERNESTO, "Ernesto Rodriguez, Junior, Back end, Florida International University")
    load_media(col4, IMAGE_MICHEL, "Michel Avalos, Junior, Front end, Florida International University")
    st.divider()

def render_Data():

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv("mission156-complete.csv")  # Provide the path to your default dataset

    st.header("Biscayne Bay Water Quality Monitoring")
    st.subheader("Water Quality Analysis")

    min_depth, max_depth = df["Depth m"].min(), df["Depth m"].max()
    min_temp, max_temp = df["Temp °C"].min(), df["Temp °C"].max()
    min_ph, max_ph = df["pH"].min(), df["pH"].max()

    selected_depth = st.slider("Select Depth (m)", min_value=min_depth, max_value=max_depth,
                                       value=(min_depth, max_depth))
    selected_temp = st.slider("Select Temperature (°C)", min_value=min_temp, max_value=max_temp,
                                      value=(min_temp, max_temp))
    selected_ph = st.slider("Select pH", min_value=min_ph, max_value=max_ph, value=(min_ph, max_ph))

    filtered_df = df[(df["Depth m"] >= selected_depth[0]) & (df["Depth m"] <= selected_depth[1]) &
                     (df["Temp °C"] >= selected_temp[0]) & (df["Temp °C"] <= selected_temp[1]) &
                     (df["pH"] >= selected_ph[0]) & (df["pH"] <= selected_ph[1])]
    Scatter_Plots_tab, Maps_tab, Line_Plots_tab, threeD_Plots_tab, Raw_Plots_tab = st.tabs(["Scatter Plots", "Maps", "Line", "3D Plots", "Raw Data"])

    with Scatter_Plots_tab:
        scatter_plots(filtered_df)
    with Maps_tab:
        maps(filtered_df)
    with Line_Plots_tab:
        line_plots(filtered_df)
    with threeD_Plots_tab:
        three_d_plots(filtered_df)
    with Raw_Plots_tab:
        raw_data(filtered_df)
def render_Research():
    st.title("Research")
    st.subheader("About our Research")
    st.write("Paragraph Here")
    st.divider()
    st.subheader("Sub Header 2 Here")
    st.write("Paragraph 2 Here, also we can use pics from biscayne")
    st.divider()


with st.sidebar:
    st.image(IMAGE_FIU,width=100)
    st.title("HCI FINAL PROJECT")
    page = st.sidebar.selectbox("Page", options=["Home", "Research", "Data", "About"])


# Conditionally render pages based on selection
if page == "Home":
    render_home_page()
elif page == "About":
    render_About()
elif page == "Data":
    render_Data()
elif page == "Research":
    render_Research()




