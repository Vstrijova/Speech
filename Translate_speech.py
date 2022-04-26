import streamlit as st
from gtts import gTTS
from googletrans import Translator

your_text = st.input('Give me a text to translate ')
your_lang = st.input('Give me the 2-letter language code you want to translate into ')

translator = Translator()
your_text_transl = translator.translate(your_text, dest= your_lang)
your_text_tospeech = your_text_transl.text

tts1=gTTS(text = your_text_tospeech, lang = your_lang)
tts1.save('your_file.mp3')
audio_file = open('your_file.mp3', 'rb')
st.audio(data = audio_file, format = "audio/mp3", start_time = 0))
