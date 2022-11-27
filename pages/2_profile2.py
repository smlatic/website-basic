from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# -- THEME
# create .streamlit folder, and a config.toml file
# paste from 
# https://blog.streamlit.io/introducing-theming/


# -- HIDE MENU AND FOOTER --
hide_menu =  """
<style>
#MainMenu {
visibility:hidden;
}
footer {
visibility:hidden;    
}
</style>

"""


# Emoji-list https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Edin Webtest", page_icon=":tada:", layout="wide")

# Hide menu after set page config
st.markdown(hide_menu, unsafe_allow_html=True)
st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        .css-eczf16 {display: none}
        .css-jn99sy {display: none}
        </style>
        """, unsafe_allow_html=True)
        #TODO Find Theme and put it in



# Function for lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- LOAD ASSETS ---
lottie_profile = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_bfgchzaf.json")
lottie_code = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_Lpuvp7YT5K.json")
image_ume = Image.open("images/picardwot.png")
image_kro = Image.open("images/facepalm.png")

 

# --- Sidebar ---
with st.sidebar:
    st.header("Header title")
    st.subheader("This is the sub-header")
    st.write("asdklasdasdlas ")




# --- HEADER ---
with st.container():
    st.subheader("Hi, I am Edin :wave:")

    left1_column, right1_column = st.columns(2)
    with left1_column:
        st.title("PrO WeBDevelOper")
        st.write("cringy quote, never stop dreamin!")
        st.write("[Github >](https://github.com/smlatic/Portfolio-Edin-Smlatic)")
    with right1_column:
        st_lottie(lottie_profile, height=200)


# --- What I doez
with st.container():
    st.write("---")

    # Left column
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i Doez")
        st.write("##")
        st.write(
            """
            I doez this stuff:
            -  lestiae quas vel sint commodi repudiandae consequuntur vol
            -  Quo neque error repudiandae fuga? Ipsa laudantium molestias eos sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
            -  Quo neque error repudiandae fuga? Ipsa laudantium molestias eos sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
            -  Quo neque error repudiandae fuga? Ipsa laudantium molestias eos sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
            """
        )
        st.write("[Github >](https://github.com/smlatic/Portfolio-Edin-Smlatic)")
        

    with right_column:
        st_lottie(lottie_code, height=400, key="coding")



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
        st.subheader("Got nuthin")
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
        st.subheader("Got nuthin part 2")
        st.write("""
        Some text here about something
        yada yada

        """)
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=X1gM3oIXKmE)")
