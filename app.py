import streamlit as st
import os

url = st.text_input("youtube url", value="https://www.youtube.com/watch?v=IwOfCgkyEj0")
file_name = url.split("=")[-1]+".mp3"
command = "youtube-dl --extract-audio --audio-format mp3 " + url + " -o " + file_name 

os.system(command)
mp3 = open(file_name, "rb").read()
st.audio(mp3)
