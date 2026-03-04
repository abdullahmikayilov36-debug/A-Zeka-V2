import streamlit as st
import google.generativeai as genai

# Google-da tapılmaq üçün başlıq
st.set_page_config(page_title="A-Zəka - Mikayılov Abdullah", page_icon="🤖")

# API
API_KEY = "AIzaSyBprup0Op0xws6tbcoKwokDRKzez_OHVjI"
genai.configure(api_key=API_KEY)

# ... kodun qalan hissəsi ...
