import streamlit as st
import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_animation1 = 'https://assets8.lottiefiles.com/private_files/lf30_5jrklsmp.json'
lottie123 = load_lottieurl(lottie_animation1)
st.title("WELCOME TO MY WEB APP")
st.tabs("INSTAGRAM REACH ANALYSIS")
st_lottie(lottie123, key='hello')
