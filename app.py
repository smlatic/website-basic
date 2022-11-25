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
        