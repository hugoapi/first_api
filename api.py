import streamlit as st
import pandas as pd
from PIL import Image
import joblib



# Inject custom CSS into the app using st.markdown
st.markdown(custom_css, unsafe_allow_html=True)




# Selectbox
Season = "Season"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Season}</span>", unsafe_allow_html=True)
selectboxexample = st.selectbox(label="Season", label_visibility='collapsed', options=("Spring", "Summer", "Winter"))

# Input bar 1
Classroom_volunme = "Classroom volunme"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Classroom_volunme}</span>", unsafe_allow_html=True)
volume = st.number_input(label="Classroom volunme", label_visibility='collapsed', min_value=0.00, format='%.2f')

# Input bar 2
N_students = "Number of students"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{N_students}</span>", unsafe_allow_html=True)
students = st.number_input(label="Number of students",label_visibility='collapsed', min_value=0, max_value=100, format='%g')

# Input bar 3
Occupancy_duration = "Occupancy duration"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Occupancy_duration}</span>", unsafe_allow_html=True)
occtime = st.number_input(label="Occupancy duration",label_visibility='collapsed', min_value=0, format='%g')

# Input bar 4
Area_window = "Opening area of windows"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Area_window}</span>", unsafe_allow_html=True)
openwindow = st.number_input(label="Opening area of windows",label_visibility='collapsed', min_value=0.00, format='%.2f')

# Input bar 5
Duration_window = "Window opening duration"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Duration_window}</span>", unsafe_allow_html=True)
windowtime = st.number_input(label="Window opening duration",label_visibility='collapsed', min_value=0, format='%g')

# Input bar 6
Area_door = "Opening area of door"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Area_door}</span>", unsafe_allow_html=True)
opendoor = st.number_input(label="Opening area of door",label_visibility='collapsed', min_value=0.00, format='%.2f')

# Input bar 7
Duration_door = "Door opening duration"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Duration_door}</span>", unsafe_allow_html=True)
doortime = st.number_input("Door opening duration", label_visibility='collapsed', min_value=0, format='%g')

# Text area
Comments = "Do you have any comments?"
st.markdown(f"<span style='font-size: 18px; font-weight: bold;'>{Comments}</span>", unsafe_allow_html=True)
st.text_area("Do you have any comments?", label_visibility='collapsed')

# If button is pressed
if st.button("Know your IAQ"):
    
    # Unpickle classifier
    clf = joblib.load("model.pkl")
    
    # Store inputs into dataframe
    X = pd.DataFrame([[volume, students, occtime, openwindow, windowtime, opendoor, doortime]], 
                     columns = ["VOLUME", "TOTAL_STUDENTS", "OCCUPIED_TIME", "OPENING_SIZE_WINDOW",
                                "OPENINNG_WINDOW_TIME", "OPENING_SIZE_DOOR", 
                                "OPENING_DOOR_TIME"])
    
    # Get prediction
    prediction = clf.predict(X)[0]
    
    # Output prediction
    if prediction == 1:
        st.text(f"Your IAQ level is：Good")
    if prediction == 2:
        st.text(f"Your IAQ level is：Acceptable")
    if prediction == 3:
        st.text(f"Your IAQ level is：Bad")
