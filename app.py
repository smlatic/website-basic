from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Emoji-list https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Edin Webtest", page_icon=":tada:", layout="wide")




# Function for lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- LOAD ASSETS ---
lottie_code = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_Lpuvp7YT5K.json")
image_ume = Image.open("images/köket.png")
image_kro = Image.open("images/kro.png")

 

# --- HEADER ---
with st.container():
    st.subheader("Hi, I am Edin :wave:")
    st.title("This is the st.Title yooo")
    st.write("This is st.write so lets see how this text turns out.")
    st.write("[Github >](https://github.com/smlatic/Portfolio-Edin-Smlatic)")



# --- What I doez
with st.container():
    st.write("---")

    # Left column
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i Doez")
        st.write("##")
        st.write("""
        
        SDJKAJDKSJKDJAKSDKAJD
         -asdasdasd
         - asdasdasd
         - asdasd
         -asdasda

        asdasdasd
        asdasdasd
        
        """)
        st.write("[Github >](https://github.com/smlatic/Portfolio-Edin-Smlatic)")
        

    with right_column:
        st_lottie(lottie_code, height=300, key="coding")


#----- PROJECTs-----

# --- Project1 ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
         st.image(image_kro)
    with text_column:
        st.subheader("Lottie Animation")
        st.write("""
        Some text here about something
        yada yada

        """)
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=X1gM3oIXKmE)")


# --- Project2 ---
with st.container():

    image_column, text_column = st.columns((1, 2))
    with image_column:
         st.image(image_ume)
    with text_column:
        st.subheader("Waz happennin")
        st.write("""
        Some text here about something
        yada yada

        """)
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=X1gM3oIXKmE)")
