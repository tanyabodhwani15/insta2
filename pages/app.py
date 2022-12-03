import streamlit as st
import pickle
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
      menu_title="Main Menu",  # required
      options=["Home", "Main"],  # required
                
               
      default_index=0,  # optional
    )
return selected
    
    if selected == "Home":
      import streamlit as st
      import base64
      import webbrowser
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
   st.subheader("INSTAGRAM REACH ANALYSIS")
   st.markup("giphy.gif")
   st_lottie(lottie123, key='hello')


   url = 'https://tanyabodhwani15-insta3-pagesapp-skazw5.streamlit.app/'

   if st.button('Click Here For Prediction'):
     webbrowser.open_new_tab(url)
   if selected == "Projects":
     st.title(f"You have selected {selected}")


model = pickle.load(open('Model.pkl', 'rb'))
col1, col2, = st.columns((2, 2,))

with col1:
    st.title("Instagram Impression Analysis")

with col2:
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_animation1 = "https://assets10.lottiefiles.com/packages/lf20_toqwmdjr.json"
    lottie_animi = load_lottieurl(lottie_animation1)

    st_lottie(lottie_animi, key='hello')

st.subheader('This model will have you to find out the reach or impression of your post or story.')


def run():
    name = st.text_input("Write your name of your instagram account.  ")
    Likes = st.number_input("How many likes do you have on your post or reel ? 👍", value=0)
    Saves = st.number_input("How many people saved your post or reel ?", value=0)
    Comments = st.number_input("How many comments you got on your post or reel ? ", value=0)
    Shares = st.number_input("How many people shared your post or reel ? ", value=0)
    Profile_Visits = st.number_input("How many people visited your profile ?", value=0)
    follows = st.number_input("How many people follows you on instagram ?", value=0)
    acc = st.checkbox('Your account should be public account')

    if st.button("submit") and acc:

        features = [[Likes, Saves, Comments, Shares, Profile_Visits, follows]]
        Impressions = model.predict(features)
        st.write('HELLO ', name, " ! from the above given details , your impressions are ", Impressions)

        if not acc:
            st.error('error')


run()
