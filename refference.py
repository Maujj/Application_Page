import streamlit as st
from PIL import Image

videoclip = open("vd.mp4",'rb')
videobytes = videoclip.read()

Audioclip = open("myAudio.mp3", 'rb')
Audiobytes = Audioclip.read()
#------------------------------------------------

st.title("Wedding Invite")

st.image(image=Image.open("pic2.jpg"))

st.video(videobytes,autoplay = True,muted =True,loop = True)

st.audio(Audiobytes,autoplay = True,loop = True)


#--------------------------------------------------

if st.button('Wedding_Card'):
    st.video(videobytes,autoplay = True,muted =True,loop = True)

if st.checkbox('pics'):
    st.image(image=Image.open("pic2.jpg"))

quarter = st.radio('which option?',('wedding_card','pics'))
if (quarter == 'wedding_card'):
    st.video(videobytes,autoplay = True,muted =True,loop = True)
elif (quarter == 'pics'):
    st.image(image=Image.open("pic2.jpg"))

quarter = st.selectbox('which option?',('wedding_card','pics'))
if (quarter == 'wedding_card'):
    st.video(videobytes,autoplay = True,muted =True,loop = True)
elif (quarter == 'pics'):
    st.image(image=Image.open("pic2.jpg"))
