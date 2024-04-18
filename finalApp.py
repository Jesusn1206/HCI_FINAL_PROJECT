import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Water Quality Project", layout="wide", page_icon="🌊", initial_sidebar_state="expanded")

IMAGE_JESUS = "media/JesusPic.jpg"
IMAGE_ANGIE = "media/AngiePic.jpg"
IMAGE_ERNESTO = "media/ErnestoPic.jpg"
IMAGE_MICHEL = "media/MichelPic.jpg"
IMAGE_FIU = "media/FIU_LOGO.png"
IMAGE_BANNER = "media/Water_Banner.jpg"
IMAGE_BBC_Research1 = "media/BBC_Research1.jpg"
IMAGE_BBC_Research2 = "media/BBC_Research2.jpg"
IMAGE_FIU_BANNER = "media/FIU_Banner.png"

MAJORS = [
    "",  # Placeholder for an empty selection
    "Accounting",
    "Aerospace Engineering",
    "Agricultural Science",
    "Anthropology",
    "Architecture",
    "Art History",
    "Biochemistry",
    "Biomedical Engineering",
    "Chemical Engineering",
    "Civil Engineering",
    "Computer Science",
    "Criminal Justice",
    "Cybersecurity",
    "Dentistry",
    "Economics",
    "Electrical Engineering",
    "Environmental Science",
    "Film Studies",
    "Finance",
    "Graphic Design",
    "History",
    "Industrial Engineering",
    "International Relations",
    "Journalism",
    "Linguistics",
    "Management",
    "Marketing",
    "Mathematics",
    "Mechanical Engineering",
    "Medicine",
    "Music",
    "Nursing",
    "Nutrition",
    "Pharmacy",
    "Philosophy",
    "Physics",
    "Political Science",
    "Psychology",
    "Public Health",
    "Sociology",
    "Software Engineering",
    "Statistics",
    "Theater",
    "Urban Planning",
    "Veterinary Science",
    "Web Development"
]



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
    st.title("HCI FINAL PROJECT")
    st.title("Home")
    # Project overview paragraph
    st.write("Our project focuses on analyzing the water quality surrounding the Biscayne Bay and Haulover Beach areas. \
            These are vital ecosystems in South Florida, providing habitat for diverse marine life and recreational \
            opportunities for residents and visitors alike. Understanding the water quality of these areas is crucial \
            for environmental conservation efforts, ensuring the health of aquatic ecosystems, and safeguarding public health.")
    # Additional details on the project overview
    st.write("In addition to assessing general water quality parameters such as pH, temperature, and dissolved oxygen, \
           our analysis also includes evaluating the presence of pollutants, including heavy metals, nutrients, and \
           microplastics. By investigating these factors, we aim to gain a comprehensive understanding of the factors \
           influencing water quality in the Biscayne Bay and Haulover Beach regions.")

    # Data collection and analysis paragraph
    st.divider()
    st.subheader("Data Collection and Analysis")
    st.write("To conduct our analysis, we implemented a multi-faceted approach to data collection and analysis. Field \
           measurements were conducted at various locations within Biscayne Bay and Haulover Beach to capture \
           real-time water quality data. Additionally, water samples were collected and analyzed in laboratory settings \
           to assess chemical compositions and pollutant levels.")

    # Further details on data collection methods
    st.write("Our team collaborated with local environmental organizations and regulatory agencies to access \
           existing datasets and leverage their expertise in water quality monitoring. This collaborative effort \
           allowed us to gather a comprehensive dataset spanning multiple years, facilitating longitudinal analysis \
           and trend identification.")

    # Goals of data analysis
    st.write("Through our data analysis, we aim to identify spatial and temporal patterns in water quality parameters, \
           assess the impact of anthropogenic activities such as urbanization and industrialization, and propose \
           evidence-based recommendations for water quality management and conservation efforts.")

    st.divider()
    col5, col6, col7 = st.columns([1, 1, 1])
    with col6:
        st.image(IMAGE_FIU_BANNER, width=200)
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
    col5, col6, col7 = st.columns([1, 1, 1])
    with col6:
        st.image(IMAGE_FIU_BANNER, width=200)

def render_Data():

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("File was Uploaded Succesfully")
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
    st.subheader("About Our Research")
    col1, col2 = st.columns(2)

    with col1:
        # Research overview paragraph
        st.write("Our research was conducted primarily on a boat, allowing us to collect data directly from Biscayne Bay and \
           Haulover Beach. Conducting research on-site provided us with a unique opportunity to gather real-time water quality \
           measurements and observations, ensuring the accuracy and reliability of our data.")
        # Additional details on the research process
        st.write("Equipped with specialized sampling equipment and instruments, our research team navigated through various \
                   locations within Biscayne Bay and Haulover Beach. We collected water samples, conducted in-situ measurements, \
                   and documented environmental conditions to capture a comprehensive snapshot of the water quality dynamics in the \
                   study area.")
    with col2:
        st.image(IMAGE_BBC_Research1, use_column_width=True)


    # Subheader and paragraph for additional information
    st.divider()
    st.subheader("Data Collection Process")
    col3, col4 = st.columns(2)
    with col3:
        st.write("During our research expeditions, we utilized state-of-the-art sensors and sampling techniques to gather \
           data on a wide range of parameters, including temperature, pH, dissolved oxygen, and nutrient concentrations. \
           By employing rigorous data collection protocols, we ensured the integrity and quality of our dataset, enabling \
           robust analysis and interpretation.")

        # Utilizing images from Biscayne Bay
        st.write("Additionally, we captured photographs and videos during our research expeditions, documenting the \
           geographical features, marine life, and anthropogenic activities in Biscayne Bay and Haulover Beach. These visual \
           records not only complement our data analysis but also serve as valuable educational and outreach materials \
           for raising awareness about the importance of water quality conservation.")
    with col4:
        st.image(IMAGE_BBC_Research2, use_column_width=True)
    st.divider()
    col5, col6, col7 = st.columns([1, 1, 1])
    with col6:
        st.image(IMAGE_FIU_BANNER, width=200)


def render_sign_up():
    st.title('Sign Up to Learn More')
    st.write('Please enter your information below:')

    with st.form("Registration", clear_on_submit=True):
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        major = st.selectbox("Major:",
                             options= MAJORS)
        level = st.selectbox("Degree Level:", options=["", "UnderGrad", "Masters", "PhD", "Other"])
        subscribe = st.checkbox("Do you want to know about future events?")
        submit = st.form_submit_button("Submit")
        if (name and email and submit and subscribe and level) or (name and email and submit and level):
            st.success(f"{name}, {level} in {major}, is now registered")
        elif submit:
            st.warning(f"{name}, {level} in {major}, is NOT registered")
        else:
            st.info("Please Fill out the form")
    st.divider()
    col5, col6, col7 = st.columns([1, 1, 1])
    with col6:
        st.image(IMAGE_FIU_BANNER, width=200)

with st.sidebar:
    st.image(IMAGE_FIU,width=100)
    st.title("HCI FINAL PROJECT")
    page = st.sidebar.selectbox("Page", options=["Home", "Research", "Data", "Sign Up", "About"])


# Conditionally render pages based on selection
if page == "Home":
    render_home_page()
elif page == "About":
    render_About()
elif page == "Data":
    render_Data()
elif page == "Research":
    render_Research()
elif page == "Sign Up":
    render_sign_up()




