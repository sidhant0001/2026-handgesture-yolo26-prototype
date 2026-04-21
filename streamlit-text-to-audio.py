
import io
from gtts import gTTS
import streamlit as st

#page setup
# This must be the FIRST Streamlit call. It sets the browser tab.
st.set_page_config(page_title="Speak!" )

# Title and subtitle
st.title("🗣️ Speak!")
st.write("Type anything and hear it aloud")

# text_area gives a multi-line text box
text = st.text_area(
    "Type something to say:",
    placeholder="e.g. Hello world!",
    height=100,
)
speak_clicked_function = st.button("Speak!", type="primary", use_container_width=True)

if speak_clicked_function:
    if not text.strip():
        st.warning("Type something first!")
    else:
        # gTTS = "Google Text-to-Speech". It sends our text to Google's free
        # online service, which converts the words into an MP3 audio clip
        # of a voice reading them out loud. lang="en" tells it to use English.
        google_text_to_speech = gTTS(text=text, lang="en")

        # An "audio buffer" is basically a pretend file that lives in memory
        # (RAM) instead of on the hard drive. io.BytesIO() creates an empty
        # one. We use it so we don't have to save an actual .mp3 file on disk.
        audio_buffer = io.BytesIO()

        # Ask gTTS to write the MP3 data into our in-memory buffer.
        google_text_to_speech.write_to_fp(audio_buffer)

        # After writing, the "cursor" inside the buffer is at the end.
        # seek(0) moves it back to the start so Streamlit can read from
        # the beginning when it plays the audio. (Like rewinding a tape.)
        audio_buffer.seek(0)

        # Show an audio player in the browser that plays our MP3 bytes.
        st.audio(audio_buffer, format="audio/mp3")
