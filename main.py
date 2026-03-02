import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Səhifə Ayarları
st.set_page_config(page_title="A-Zəka v2.0", page_icon="🤖", layout="wide")

st.title("🤖 A-Zəka v2.0: Ultra Universal Sistem")
st.write("### Yaradıcı və Müəllif: Abdullah Mikayılov")
st.markdown("---")

# 2. API Təhlükəsizlik Ayarları
API_KEY = "AIzaSyBprup0Op0xws6tbcoKwokDRKzez_OHVjI"
genai.configure(api_key=API_KEY)

# 3. Beyin Təlimatı
instructions = """
Sən Abdullah Mikayılov tərəfindən yaradılmış A-Zəka v2.0-san.
1. KİMLİK: "Səni kim yaradıb?" soruşulsa, "Mən Abdullah Mikayılov tərəfindən yaradılmışam" de.
2. BİLİK: 2026-cı ilin bütün məlumatlarına professor səviyyəsində sahibsən.
3. QAYDA: Cavablarda LaTeX ($...$) işlətmə, hər şeyi sadə mətnlə yaz.
"""

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash', 
    system_instruction=instructions
)

# 4. Şəkil Analizi
with st.sidebar:
    st.header("🖼️ Şəkil Analizi")
    uploaded_file = st.file_uploader("Analiz üçün şəkil seçin:", type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption='Yüklənən şəkil', use_container_width=True)

# 5. Sual-Cavab
user_input = st.chat_input("A-Zəka-ya sualınızı yazın...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    with st.spinner("A-Zəka cavab hazırlayır..."):
        try:
            if uploaded_file:
                response = model.generate_content([user_input, img])
            else:
                response = model.generate_content(user_input)
            with st.chat_message("assistant"):
                st.write(response.text)
        except Exception as e:
            st.error(f"Xəta: {e}")
