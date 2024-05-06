import os
import requests
import streamlit as st
import time
from task import email_task
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
api_key = os.getenv('SUNO_API_KEY')
st.set_page_config(
    page_title="Lyzr Music Generator🎶🎸",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Lyzr Music Generator")
st.markdown("## Welcome to the Lyzr Music Generator!")
st.markdown("You Have to Enter Your Email,Music Title,Tags and Music Prompt.This app Will Generates Music for you.")

def get_song_id(title, tags, prompt):
    song_id_list = []
    url = "https://api.sunoaiapi.com/api/v1/gateway/generate/music"

    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "title": title,
        "tags": tags,  # Music style
        "prompt": prompt
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()['data']

        for i in range(len(data)):
            song_id_list.append(response.json()['data'][i]['song_id'])

        return song_id_list


def generate_song(song_id):
    url_song = f"https://api.sunoaiapi.com/api/v1/gateway/feed/{song_id}"

    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }

    song_response = requests.get(url_song, headers=headers)

    if song_response.status_code == 200:
        data1 = song_response.json()['data']
        return data1


email = st.text_input("Email")
title = st.text_input("Title")
tag_list = ["Jazz", "Rock", "Pop", "Classical", "Hip-hop", "Electronic", "Country", "Blues", "Reggae", "Folk"]
tags = st.selectbox("Tags", options=tag_list)
prompt = st.text_area("Enter Prompt")



if st.button("Generate"):

    songs_url = []
    n = 0
    while n < 4:
        song_ids = get_song_id(title, tags, prompt)

        for song_id in song_ids:
            while True:
                songs = generate_song(song_id)
                if songs['status'] in ['streaming', 'complete']:
                    songs_url.append(songs)
                    n += 1
                    break
                else:
                    time.sleep(10)

    for s in songs_url:
        st.audio(s['audio_url'])

    email_task(email)



