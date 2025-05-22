import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "apiKey": "AIzaSyDnEfO5U4LlCt83BCGfrqpRcDNjTY6ybpE",
    "authDomain": "studcredential.firebaseapp.com",
    "databaseURL": "https://studcredential-default-rtdb.firebaseio.com",
    "projectId": "studcredential",
    "storageBucket": "studcredential.firebasestorage.app",  # This is the correct Firebase storage domainpy
    "messagingSenderId": "344356259156",
    "appId": "1:344356259156:web:bb1a927e8442446a1434c1"
}




firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def register(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"

def login(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"
