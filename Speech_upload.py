import streamlit as st
from gtts import gTTS
from googletrans import Translator

st.header("Welcome to my translation_app")

your_uploaded_file =  st.file_uploader("Choose a file")
if your_uploaded_file is not None:
     bytes_data = your_uploaded_file.getvalue()
     st.write(bytes_data)
     stringio = StringIO(your_uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     if your_uploaded_file != ' ':
          translator = Translator()
          your_text_transl = translator.translate(your_uploaded_file, dest= your_lang)
          your_text_tospeech = your_text_transl.text
          st.write('Your translated text is: ', your_text_tospeech)
          
          tts1=gTTS(text = your_text_tospeech, lang = your_lang)
          tts1.save('your_file.mp3')
          audio_file = open('your_file.mp3', 'rb')
          st.audio(data=audio_file, format="audio/mp3", start_time = 0)
          st.download_button(label="Download audio file", data=audio_file, file_name='yourfile.mp3',mime='audio/mp3')
else:
  pass
