# Streamlit is a Python library used for creating web applications with simple Python scripts.
# Imports streamlit python library
import streamlit as st

# Sets the title to "Bio data"
# st.title() function sets the title of the app
st.title("Title: Bio data")
# st.write() function displays text in the app
st.write("This is a sample web app.")

# Stores the user's first name in the variable first_name
first_name = st.text_input("First Name")

# Stores the user's last name in the variable last_name
last_name = st.text_input("Last Name")

# selectbox creates a drop down menu with two options(male and female)
# the 2 options are stores in the variable gender
gender = st.selectbox("Gender",["Male","Female"])

# Allows user to input their age between 0 and 100
# 30  is the default age and 1 allows the user to increase or decrease their age by 1
age = st.number_input("Your age", 0, 100, 30, 1)

# The variable dob stores the user's date of birth
# dateinput() function allows the user to select the date from a calendar widget
dob = st.date_input("Your Birthday")

# st.radio() creates radio buttons for selecting marital status
# marital_status variable stores the marital status of a user
marital_status = st.radio("Marital Status", ["Single", "Married"])

# creates a slider for selecting years of experience, ranging from 0 to 40
# years_of_experience variable stores the years of experience that a user has
years_of_experience = st.slider("Years of experience", 0, 40)
