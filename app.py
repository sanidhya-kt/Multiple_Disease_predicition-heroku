"""
Spyder Editor

This is created by Sanidhya Kumar Tiwari

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# loading the saved model

diabetes_model = pickle.load(open('D:/major project/multiple disease prediction/saved model/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('D:/major project/multiple disease prediction/saved model/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('D:/major project/multiple disease prediction/saved model/parkinsons_model.sav' , 'rb'))


# slidebar for nevigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Predicition System', 
                           [
                               'Diabetic Predicition',
                               'Heart Disease Predicition',
                               'Parkinsons Predicition'
                               ],
                           
                           icons = ['activity' , 'heart' , 'person'],
                           
                           default_index = 0)
    
# Diabetic Prediction Page
if(selected == 'Diabetic Predicition'):

    #page Title
    st.title('Diabetes Predicition using ML')  
    
    #getting the input data from user
    #columns for the input fiels
    
    col1, col2 = st.columns(2)
    
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies') 
        
    with col2:
        Glucose = st.number_input('Glucose Level of Patient')
        
    with col1:
        BloodPressure = st.number_input('Blood pressure value of Patient') 
   
    with col2:
        SkinThickness = st.number_input('Skin Thickness Value of Patient') 
   
    with col1:
        Insulin = st.number_input('Insulin Level of Patient')   
   
    with col2:
        BMI = st.number_input('BMI value of Patient')   
    
    with col1:
        DiabetesPadigreeFunction = st.number_input('Diabetes Padigree Function value')  
    
    with col2:
        Age = st.number_input('Age of the Patient')
        
    
    # code for predicition
    
    diab_dignosis = ''
    
    #creating a button for predicition
    
    if st.button('Diabetic Test Result'):
        diab_predicition = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI , DiabetesPadigreeFunction, Age ]])
        
        if (diab_predicition[0] == 1):
            diab_dignosis = 'The patient is Diabetic'
            
        else:
            diab_dignosis = 'The patient is NON-Diabetic'
            
    st.success(diab_dignosis)
    
    
# Heart Disease Prediction Page
if(selected == 'Heart Disease Predicition'):

    #page Title
    st.title('Heart Disease Predicition using ML') 
    
    #getting the input data from user
    #columns for the input fiels
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input('Enter Patient age') 
        
    with col2:
        sex = st.number_input('Gender Of The Patient')
        
    with col1:
        cp = st.number_input('chest pain type (4 values)') 
   
    with col2:
        trestbps = st.number_input('resting blood pressure of Patient') 
   
    with col1:
        chol = st.number_input('serum cholestoral (mg/dl) of Patient')   
   
    with col2:
        fbs = st.number_input('fasting blood sugar of Patient')   
    
    with col1:
        restecg = st.number_input('resting electrocardiographic results (values 0,1,2)')  
    
    with col2:
        thalach = st.number_input('maximum heart rate of the Patient')
        
    with col1:
        exang = st.number_input('exercise induced angina')  
        
    with col2:
        oldpeak = st.number_input('ST depression induced by exercise relative to rest')
            
    with col1:
        slope = st.number_input('the slope of the peak exercise ST segment')  
            
    with col2:
        ca = st.number_input('number of major vessels (0-3) colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    # code for predicition
    
    heart_dignosis = ''
    
    #creating a button for predicition
    
    if st.button('Cardiac Test Result'):
        
        heart_predicition = heart_disease_model.predict([[ age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_predicition[0] == 1):
        
            heart_dignosis = 'The patient is having Heart Disease'
            
        else:
            
            heart_dignosis = 'The patient does not have any Heart Disease'
            
    st.success(heart_dignosis)
    
    
# Parkinsons Prediction Page
if(selected == 'Parkinsons Predicition'):

    #page Title
    st.title('Parkinsons Predicition using ML') 
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')
        
    with col1:
        Jitter_percent = st.number_input('MDVP:(%)')
        
    with col2:
        Jitter_Abs = st.number_input('MDVP:(Abs)')
        
    with col3:
        RAP = st.number_input('MDVP:RAP')
        
    with col1:
        PPQ = st.number_input('MDVP:PPQ')
        
    with col2:
        DDP = st.number_input('Jitter:DDP')
        
    with col3:
        Shimmer = st.number_input('MDVP:Shimmer')
        
    with col1:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
        
    with col2:
        APQ3 = st.number_input('Shimmer:APQ3')
        
    with col3:
        APQ5 = st.number_input('Shimmer:APQ5')
        
    with col1:
        APQ = st.number_input('MDVP:APQ')
        
    with col2:
        DDA = st.number_input('Shimmer:DDA')
        
    with col3:
        NHR = st.number_input('NHR')
        
    with col1:
        HNR = st.number_input('HNR')
        
    with col2:
        RPDE = st.number_input('RPDE')
        
    with col3:
        DFA = st.number_input('DFA')
        
    with col1:
        spread1 = st.number_input('spread1')
        
    with col2:
        spread2 = st.number_input('spread2')
        
    with col3:
        D2 = st.number_input('D2')
        
    with col1:
        PPE = st.number_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)






