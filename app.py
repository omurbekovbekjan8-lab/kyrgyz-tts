import io
import streamlit as st
from gtts import gTTS

# Настройка страницы
st.set_page_config(page_title="Kyrgyz TTS", page_icon="🇰🇬", layout="centered")

st.title("🇰🇬 Кыргыз Тили Сүйлөйт")
st.caption("Акысыз онлайн синтезатор речи (Google TTS)")

# Поле для ввода текста
user_text = st.text_area(
    "Текстти бул жерге жазыңыз (Введите текст):",
    placeholder="Мисалы: Салам, кандайсың?",
    height=150,
)

if st.button("Үнгө айлантуу (Озвучить)", type="primary"):
  if user_text.strip():
    with st.spinner("Генерация улантылууда..."):
      try:
        # Создаем озвучку на кыргызском языке ('ky')
        tts = gTTS(text=user_text, lang="ky", slow=False)

        # Сохраняем аудио в оперативную память
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)

        st.success("Ийгиликтүү түзүлдү!")
        st.audio(audio_buffer, format="audio/mp3")

      except Exception as e:
        st.error(f"Ката кетти: {e}")
  else:
    st.warning("Сураныч, текстти жазыңыз (Пожалуйста, введите текст)")
