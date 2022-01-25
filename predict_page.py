from pyexpat import features
import streamlit as st
import pickle
import numpy as np
import pandas as pd

#load model
load_model=pickle.load(open('saved.pkl','rb'))

def show_predict_page():
    st.title(" Developer Salary Prediction")

    st.write("""### Please enter below details""")

    Country = (
    'Australia',
    'Austria',
    'Belgium',
    'Brazil',
    'Canada',
    'Czech Republic',
    'France',
    'Germany',
    'India',
    'Iran, Islamic Republic of...',
    'Israel',
    'Italy',
    'Mexico',
    'Netherlands',
    'Norway',
    'Poland',
    'Russian Federation',
    'Spain',
    'Sweden',
    'Switzerland',
    'Turkey',
    'United Kingdom of Great Britain and Northern Ireland',
    'Ukraine',
    'United States of America', 
    )

    EdLevel = (
    'Master’s degree',
    'Bachelor’s degree',
    'Professional degree',
    'Less than a Bachelors',
    )

    LearnCode=(
    'School', 
    'Online Resources', 
    'Bootcamp', 
    'Others', 
    )

    Age=(
    'Under 18 years old',
    '18-24 years old',
    '25-34 years old',
    '35-44 years old',
    '45-54 years old',
    '55-64 years old',
    '65 years or older',
    'Prefer not to say',
    )
    

    Country = st.selectbox("Country", Country)
    EdLevel = st.selectbox("Education Level", EdLevel)
    LearnCode = st.selectbox("Where to learn Coding from", LearnCode)
    Age = st.selectbox("Age", Age)
    YearsCodePro = st.slider("Years of Professional Coding Experience", 0, 50, 3)
    #df=pd.from_dict({'Country':[Country],'EdLevel':[EdLevel],'LearnCode':[LearnCode],'Age':[Age]})
    
    data = {'Country': Country,
            'EdLevel':EdLevel,
            'LearnCode':LearnCode,
            'Age': Age,
            'YearsCodePro': YearsCodePro
                }

    input_df=pd.DataFrame(data,index=[0])
    #reading already cleaned data
    df=pd.read_csv('data_eda.csv')
#columns listed as: Country	 EdLevel	LearnCode	Age	YearsCodePro	Salary
    #drop target variable 
    target_df=df.drop(['Salary'], axis = 1)
    #add user input to the df 
    df=pd.concat([input_df,target_df],axis=0)

    #get a list of categorical data
    encode=['Country', 'EdLevel','LearnCode','Age']
    for col in encode:
        dummy=pd.get_dummies(df[col],prefix=0)
        df=pd.concat([df,dummy],axis=1)
        del df[col]
    df=df[:1]
                  
    ok = st.button("Predict Salary")
    if ok:
        salary = load_model.predict(df)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

