import streamlit as st
import torch
from transformers import VitsModel, AutoTokenizer
import soundfile as sf
import io

# Минималистичный дизайн страницы
st.set_page_config(page_title="Kyrgyz TTS", page_icon="🇰🇬", layout="centered")

# Кэшируем стандартную модель от Meta, чтобы сайт работал мгновенно
@st.cache_resource
def load_model():
    model_name = "facebook/mms-tts-kir"
    model = VitsModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

try:
    model, tokenizer = load_model()
    
    st.title("🇰🇬 Кыргыз Тили Сүйлөйт")
    st.caption("Акысыз онлайн синтезатор речи (Официальная модель Meta MMS)")

    # Удобное поле для ввода текста, как ты хотел
    user_text = st.text_area("Текстти бул жерге жазыңыз (Введите текст):", placeholder="Мисалы: Салам, кандайсың?", height=150)

    # Главная кнопка запуска
    if st.button("Үнгө айлантуу (Озвучить)", type="primary"):
        if user_text.strip():
            with st.spinner("Генерация улантылууда..."):
                # Токенизация стандартного текста
                inputs = tokenizer(user_text.lower(), return_tensors="pt")
                
                with torch.no_grad():
                    output = model(**inputs).waveform
                
                audio_data = output.numpy().squeeze()
                sampling_rate = model.config.sampling_rate
                
                # Запись аудио в поток памяти
                buffer = io.BytesIO()
                sf.write(buffer, audio_data, sampling_rate, format='WAV', subtype='PCM_16')
                buffer.seek(0)
                
                # Вывод готового плеера
                st.success("Ийгиликтүү түзүлдү!")
                st.audio(buffer, format="audio/wav")
        else:
            st.warning("Сураныч, текстти жазыңыз (Пожалуйста, введите текст)")

except Exception as e:
    st.error(f"Ката кетти (Произошла ошибка): {e}")
