import streamlit as st 
import pyrebase 
from datetime import datetime
import requests

#configuration key 
firebaseConfig = {
  'apiKey': "AIzaSyCzBkDE1stJoxH6X6ZSKZQmeMcqsc30J7w",
  'authDomain': "universityscholarships-7eab8.firebaseapp.com",
  'projectId': "universityscholarships-7eab8",
  'databaseURL':'https://universityscholarships-7eab8-default-rtdb.europe-west1.firebasedatabase.app/',
  'storageBucket': "universityscholarships-7eab8.appspot.com",
  'messagingSenderId': "847734098769",
  'appId': "1:847734098769:web:b173f21fdff3e331e7a170",
  'measurementId': "G-DLJP2GMLVL"
}

#firebase Authentication 

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()

st.write("Universities Scholarships Solutions")

# Authentication 

choice = st.sidebar.selectbox('Login/Signup',["Login","Sign up"])

email= st.sidebar.text_input("Please enter your email address")
password = st.sidebar.text_input("Please enter your password",type="password")

if choice == "Sign up":
    Username = st.sidebar.text_input("Please input your app User name",value="Default")
    submit=st.sidebar.button("Create my account")
    if submit:
        user=auth.create_user_with_email_and_password(email,password)
        st.success("Your account is created successfully")
        st.balloons()
        # Sign In
        user=auth.sign_in_with_email_and_password(email,password)
        db.child(user["localId"]).child("Username").set(Username)
        db.child(user["localId"]).child("ID").set("localId")
        st.title("welcome  "+f"{Username}")
        st.info("Login via login drop down select")

if choice == "Login":
    login = st.sidebar.button("Login")

    if login:
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Login successful!")
            # Add code to navigate to the desired section of your app (e.g., scholarships or finance).
            bio = st.radio("Jump to", ["Scholarships", "Finance"])
        except requests.exceptions.HTTPError as e:
            # Handle the authentication error and display an error message.
            st.error("Login failed. Please check your credentials.")



hide_streamlit_style="""
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
footer

</style>
"""
st.markdown(hide_streamlit_style,unsafe_allow_html=True)
        