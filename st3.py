import streamlit as st
import pandas as pd
st.image("code.jpg")
st.header("Task 3 grades")
Names = ["omar_ahmed",'Ahmed Eslam',
         'Ahmed Fawzy',
         'Shimmaa hamdy', 
         'mariam mostafa',
         'Abdelrhman Ahmed',
         'bassant', 
         'khaled Ahmed',
         'Esraa salah', 
         'Ahmed Essam',
         'manar mohammed',
         'Jana', 
         'Eslam']
IDs = ['omar','5751', '6620', '3#51', '2533', '1109', '5642', '#52*', '3619', '1771', '3700', '2209', '6747']
IDs_Series = pd.Series(IDs)
grades = pd.read_excel("grades.xlsx",sheet_name="Task 3 More about Poiners and S", engine="openpyxl")
grades = grades[['task 0', 'task1 ', 'task 2 ', 'task 3 ', 'Task 4 ', 'Task 5 ', 'Task 6 ', 'Task 7', 'task 8','Task 9', 'Task 10','Task 11', 
                'Task 12 ', 'Task 13', 'Task 14']]
grades = pd.concat((IDs_Series,grades),axis=1)

password = st.text_input("enter password",max_chars=4)
button = st.button("get result")
if button :
    if password not in IDs :
        st.subheader("wrong password or you didn't submmit this task , if there is problem tell us and we will work to fix it")
    else :
        name = "Name is " + Names[IDs.index(password)]
        st.subheader(name)
        grade_row = IDs.index(password)
        st.write(grades.iloc[grade_row,1:])
        
