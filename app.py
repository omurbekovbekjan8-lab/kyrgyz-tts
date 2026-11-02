import io
import requests
import streamlit as st

st.set_page_config(page_title="Kyrgyz TTS", page_icon="🇰🇬", layout="centered")

# Берём токен из секретов Streamlit (а не пишем текстом)
HF_TOKEN = st.secrets["HF_TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-kir"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}


def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.content


st.title("🇰🇬 Кыргыз Тили Сүйлөйт")
st.caption("Акысыз онлайн синтезатор речи (Облачный режим Hugging Face)")

user_text = st.text_area(
    "Текстти бул жерге жазыңыз:",
    placeholder="Мисалы: Салам, кандайсың?",
    height=150,
)

if st.button("Үнгө айлантуу (Озвучить)", type="primary"):
  if user_text.strip():
    with st.spinner("Облако генерирует голос..."):
      audio_bytes = query({"inputs": user_text.lower()})

      if b"error" in audio_bytes and len(audio_bytes) < 500:
        st.error(
            "Ката кетти: Токен туура эмес же сервер жүктөлүүдө. Кайра"
            " аракет кылыңыз."
        )
      else:
        st.success("Ийгиликтүү түзүлдү!")
        st.audio(audio_bytes, format="audio/wav")
  else:
    st.warning("Сураныч, текстти жазыңыз")
