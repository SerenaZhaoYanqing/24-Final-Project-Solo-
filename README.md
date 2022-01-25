# Project Goal
Aiming to use the 2021 stackflow developer survey to run machine learning model for predicting the developer's salary and deploy it to web_app.

* As heroku is not compatiable with apple M1. Please follow below steps to try out the web app.
 1. clone current repository
 2. run salary_prediction jupyter notebook ( which will generate a saved.pkl file). as the file is too big to be pushed to github.
 3. once the notebook has been run, use command streamlit run app.py 
 4. you might have to install streamlit if you dont have it  pip install streamlit 

# About the Data
In  2021 over 80,000 developers has completed the 2021 Developer Survey by StackFlow, providing information on  how they learn and level up, which tools they’re using, and what they want.I have utilised the survey data to develop machine learning model, using different parameters to run estimator for  developer's salary.
Date source available at: https://insights.stackoverflow.com/survey 



# WorkFlow 

## Data Cleaning
The data set was complete with small amount of missing values. However there were quite a bit cleaning need to done due to string input.For instance, with where developers learn coding from, the input might be "Other online resources ,Online Forum" which can all be categorised as "Online Resources" during cleaning process. And also,  using  Interquartile Range (IQR) for identifying outliers. 


## Data Visualizations
Once obtaining the cleaned data set, I have used different visualizations to  determine the parameters for machine learning. For example, using histogram for undersatnding the distribution of the salary range. I have also split the data into numerical and non-numerical before analysing. By doing this, we can easily removed the parameter that doesnt have a significant impact on "Salary" and remove it from our training data. 

## Modelling 
Choosing the right model is definitely the key here in order to achieve better forecasting result. Find out more about how to choose the right estimator
https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html
In this case, we have used get dummies for all categorical data then fit into different models with 20% test data, 80% train data.  Including linear Regression, Ridge Regression, Grid Search, and random forest.Random forest has the highest score of 58% on the training dataset, however the test data set is only 28% but still higher than the rest models. 

## Launching the APP
Streamlit is a easy to use tool for converting Python Script into a Web Version App. I have also included the explore option for users to have a understanding of the survey results, where multiple visualizations have been included. 


# Final project links
https://serenazhaoyanqing.github.io/24-Final-Project-Solo-/

