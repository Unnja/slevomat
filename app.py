import streamlit as st

st.set_page_config(
    page_title="Vánoční překvapení 🎄❤️",
    page_icon="🎁",
    layout="centered"
)

# Tohle je bezpečné sněžení přímo od Streamlitu (nesere se do HTML)
st.snow()

# Čistý HTML kód pro kartu s dárkem
st.markdown("""
<style>
    .stApp {
        background-color: #0e0e0e;
    }
    .gift-container {
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://github.com/Unnja/slevomat/blob/main/IMG_7797.jpg?raw=true');
        background-size: cover;
        background-position: center;
        padding: 80px 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
        color: white;
        margin-top: 20px;
    }
    .gift-btn {
        background: linear-gradient(135deg, #ff4d4d, #ff9999);
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 20px;
        border-radius: 10px;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s;
    }
    .gift-btn:hover {
        transform: scale(1.05);
    }
</style>

<div class="gift-container">
    <h1 style='margin:0; font-size: 2.5rem; text-shadow:2px 2px 5px black;'>🎁 Tady máš svůj dárek! ❤️</h1>
    <p style='font-size: 1.2rem; text-shadow:1px 1px 3px black; margin: 20px 0;'>Klikni a rozbal si ho, beruško 🎄✨</p>
    
    <a href="https://drive.google.com/file/d/1Dxi3R6fMb0r8k4E2TIpyJ6Y786f0ntpJ/view?usp=drive_link" target="_blank" style="text-decoration:none;">
        <button class="gift-btn">🎁 Rozbalit dárek</button>
    </a>
</div>
""", unsafe_allow_html=True)
