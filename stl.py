import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image



pickle_in = open("diabetes_model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):

   
   
    prediction=classifier.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    print(prediction)
    return prediction



def main():
    st.title("Diabetes Pridiction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Diabetes Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Pregnancies = st.number_input("Preganancies", step = 0.1)
    Glucose = st.number_input("Glucose",step = 0.1)
    BloodPressure = st.number_input("Blood Pressure",step = 0.1)
    SkinThickness = st.number_input("Skin Thickness",step = 0.1)
    Insulin = st.number_input("Insulin",step = 0.1)
    BMI = st.number_input("BMI",step = 0.1)
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function",step = 0.1)
    Age = st.number_input("Age",step = 0.1)

    result=""
    if st.button("Predict"):
        result=predict_diabetes(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()
    