import requests
from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image

# Find more emojis here https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open('file_name','r') as f:
        st.markdown(f"<style>{f.read()}<\style>", unsafe_allow_html=True)

local_css(r"https://raw.githubusercontent.com/Ikenna-The-Data-Guy/website/main/style.css")

# LOAD ASSETS
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")
img_covid19 = Image.open(r"https://github.com/Ikenna-The-Data-Guy/website/blob/main/Covid.png")
img_housing = Image.open(r"https://github.com/Ikenna-The-Data-Guy/website/blob/main/housing.jpg")
img_cyclistic = Image.open(r"https://github.com/Ikenna-The-Data-Guy/website/blob/main/Cyclistic.png")
img_developer = Image.open(r"https://github.com/Ikenna-The-Data-Guy/website/blob/main/developer.jpg")

## HEADER SECTION
with st.container():
    st.subheader("Hi, I am Ikenna :wave:")
    st.title("A Data Scientist/ML Engineer from Nigeria")
    st.write("""I am very passionate about using Python, SQL,
    and other Data Science and Analytics tools to make positive contributions in business settings.
    I'm also handy with visualization tools like MS Excel, Tableau, and Power BI.""")
    st.write("[Learn More>](https://github.com/Ikenna-The-Data-Guy)")


#  WHAT I DO
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I collect, transform and organize data in order to draw conclusions, make predictions, and help in 
            driving informed decision-making. I also help individuals and organisations that:
            -   are looking for ways to leverage the power of Python in their day-to-day work.
            -   are struggling with repetitive tasks in Excel and are looking for a way to use Python and R.
            -   want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            -   are working with Excel and find themselves thinking - "there has to be a better way."
            If this sounds interesting to you, head on to the next section.
            """
            )

    
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#    PROJECTS
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_covid19)
    with text_column:
        st.subheader("Exploratory Data Analysis on Covid 19 Dataset Using SQL")
        st.write(
            """
            Learn how to pull insights from a large dataset using SQL!
            In this exploratory data analysis project, you will learn how to write SQL codes as well as the logic
            behind each query. You will also see JOINs, CTE, and Temp Tables in use in the course of the project.
            """
        )
        st.markdown("[Go to project>](https://github.com/Ikenna-The-Data-Guy/Data-Exploration-in-SQL---Covid)")
        st.markdown("[Click here to view dashboard>](https://public.tableau.com/app/profile/ikenna.nwankpa/viz/Covid-19DashboardProjectDataAnalyzedinSQL/Dashboard1)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_housing)
    with text_column:
        st.subheader("Cleaning and Transformation of Housing Dataset Using SQL")
        st.write(
            """
            Learn data cleaning and transformation with SQL!
            This project focuses on data cleaning and transformation using SQL.
            """
        )
        st.markdown("[Go to project>](https://github.com/Ikenna-The-Data-Guy/Data-Cleaning-in-SQL---NashvilleHousing)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_cyclistic)
    with text_column:
        st.subheader("My Google Data Analytics Course Capstone Project.")
        st.write(
            """
            This project is all about handling business tasks/challenges using data analytics.
            The R programming language is used to manipulate the dataset. A great opportunity for anyone 
            looking to learn how to use R for data analysis! 
            """
        )
        st.markdown("[Go to project>](https://github.com/Ikenna-The-Data-Guy/Analysis-in-R-The-Cyclistic-Project)")
        st.markdown("[Click here to read up on the project>](https://medium.com/@leeec.ik/my-google-data-analytics-course-capstone-project-79146624100b)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_developer)
    with text_column:
        st.subheader("Software Developer Salary Prediction App Project.")
        st.write(
            """
            Ever wondered how machine learning models are built? This project is all about building a machine
            learning model and developing an app based on the model using the streamlit framework.
            """
        )
        st.markdown("[Go to project>](https://github.com/Ikenna-The-Data-Guy/streamlit-app-1)")
        st.markdown("[Salary Prediction App>](https://ikenna-the-data-guy-streamlit-app-1-app-8kj44k.streamlit.app/)")


#     CONTACT
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

# Documentation: https://formsubmit.co/

    contact_form = """
    <form action="https://formsubmit.co/inwankpa@yahoo.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """ 

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)   
    with right_column:
        st.empty()

        





