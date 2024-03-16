import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Wine Quality Prediction",
                   layout="wide",
                   page_icon="🍷")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

with open("wine_quality.sav", 'rb') as f:
   wine_pred_model = pickle.load(f)

# wine_pred_model = pickle.load(open('wine_quality.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Wine Quality Prediction System',
                           
                           ['Wine'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Wine':

    # page title
    st.title('Wine Quality Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        a = st.slider('Fixed Acidity', 4.6, 15.9, 4.6)

    with col2:
        b = st.slider('Volatile Acidity', 0.12, 1.58, 0.12)

    with col3:
        c = st.slider('Citric Acid', 0.00, 1.00, 0.00)

    with col1:
        d = st.slider('Residual Sugar', 0.9, 15.5, 0.9)

    with col2:
        e = st.slider('Chlorides', 0.01, 0.61, 0.01)

    with col3:
        f = st.slider('Free Sulphur Dioxide', 1, 68, 1)

    with col1:
        g = st.slider('Total Sulphur Disoxide', 6, 289, 6)

    with col2:
        h = st.slider('Density', 0.990, 1.000, 0.990)

    with col3:
        i = st.slider('pH', 2.74, 4.01, 2.74)

    with col1:
        j = st.slider('Sulphates', 0.33, 2.00, 0.33)

    with col2:
        k = st.slider('Alcohol', 8.4, 14.9, 8.4)
    

    # code for Prediction
    wine_prediction = ''

    # creating a button for Prediction

    if st.button('Wine Quality Test Result'):

        user_input = [a,b,c,d,e,f,g,h,i,j,k]

        # user_input = [float(x) for x in user_input]

        wine_prediction = wine_pred_model.predict([user_input])

    st.text("The rating of wine of out 10: ")
    st.success(wine_prediction)
