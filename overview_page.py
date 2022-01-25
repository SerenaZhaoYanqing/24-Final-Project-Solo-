import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

def load_model():
    with open('saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

def professional_experience(x):
    if x ==  'More than 50 years':
        return 51
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def educational_level(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x:
        return 'Professional degree'
    if 'Other doctoral degree' in x:
        return 'PHD' 
    return 'Less than a Bachelors'

def learn_code(x):
    if 'online' in x:
        return 'Online Resources'
    if 'Bootcamp' in x:
        return 'Bootcamp'
    if 'School' in x:
        return 'School'

def employment_status(x):
    if 'full-time' in x:
        return 'Full Time'
    if 'part-time' in x:
        return 'Part Time'
    if 'self-employed' in x:
        return 'Self-Employed'
    return 'Others'

def gender_stardarlised(x):
    if 'Woman' in x:
        return 'Female'
    if 'Man' in x:
        return 'Male'
    return 'Others'

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel","LearnCode", "YearsCodePro", "Employment", "ConvertedCompYearly","Age","Gender"]]
    df=df.dropna()
    df = df.rename({"ConvertedCompYearly": "Salary"},axis=1)
    

    counts=df['Country'].value_counts()
    to_remove =counts[counts <= 413].index
    df = df[~df.Country.isin(to_remove)]

    df = df[df["Salary"] <= 109672]
    df = df[df["Salary"] >= 41520]

    df = df[df['Gender']!='Others']

    df['Employment'] = df['Employment'].apply(employment_status)
    df = df[df['Employment']!='Others']

    df['EdLevel'] = df['EdLevel'].apply(educational_level)
    df['LearnCode'] = df['LearnCode'].apply(learn_code)
    df['YearsCodePro'] = df['YearsCodePro'].apply(professional_experience)
    return df
    
df = load_data()

def show_overview_page():
    st.title("Explore Software Developer Salaries")

    st.write(
        """
    ### Stack Overflow Developer Survey 2021
    """
    )

      
    data = df["LearnCode"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax2.axis("equal")  

    st.write("""#### Where do developers learn coding from""")

    st.pyplot(fig2)

    st.write(
        """
    #### Mean Salary Based On Years of Professional Coding Experience 
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)


    st.write(
        """
    #### Mean Salary Based On Degree
    """
    )

    data = df.groupby(["EdLevel"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)


    st.write(
        """
    #### Mean Salary based on Age Group
    """
    )

    data = df.groupby(["Age"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)


  
    

