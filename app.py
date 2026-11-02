import io
import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="TTS App", page_icon="🇰🇬", layout="centered")

st.title("🗣️ Онлайн Синтезатор Речи")

# Выбор языка, чтобы избежать ошибок
lang_choice = st.selectbox(
    "Типти тандаңыз / Выберите язык:", ("Кыргызча (kg)", "Русский (ru)")
)
lang_code = "ky" if "kg" in lang_choice else "ru"

user_text = st.text_area("Текстти жазыңыз:", height=150)

if st.button("Үнгө айлантуу (Озвучить)", type="primary"):
  if user_text.strip():
    with st.spinner("Генерация..."):
      try:
        tts = gTTS(text=user_text, lang=lang_code, slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)

        st.success("Дайын!")
        st.audio(audio_buffer, format="audio/mp3")
      except Exception as e:
        st.error(f"Ката кетти: {e}")
  else:
    st.warning("Сураныч, текст жазыңыз!")
