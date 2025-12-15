import streamlit as st
import random

st.set_page_config(
    page_title="Vánoční překvapení 🎄❤️",
    page_icon="🎁",
    layout="centered"
)

# 1. CSS STYLY (Zde definujeme vzhled - bez f-stringu, aby se nehádaly závorky)
css_styles = """
<style>
    .stApp {
        background-color: #0e0e0e;
    }
    .snowflake {
        position: fixed;
        top: -10vh;
        z-index: 9999;
        pointer-events: none;
        color: white;
        animation: fall linear infinite;
    }
    @keyframes fall {
        0% { transform: translateY(-10vh); }
        100% { transform: translateY(110vh); }
    }
    .gift-container {
        position: relative;
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://github.com/Unnja/slevomat/blob/main/IMG_7797.jpg?raw=true');
        background-size: cover;
        background-position: center;
        padding: 80px 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
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
        transition: transform 0.2s;
    }
    .gift-btn:hover {
        transform: scale(1.05);
    }
</style>
"""

# 2. GENERÁTOR SNĚHU (Vytvoříme HTML pro 50 vloček)
snow_html = ""
for _ in range(50):
    left = random.randint(0, 100)
    duration = random.uniform(3, 8)
    delay = random.uniform(0, 5)
    size = random.uniform(10, 25)
    alpha = random.uniform(0.3, 0.8)
    
    # Zde používáme f-string, ale protože jsme oddělili CSS, je to bezpečné
    snow_html += f"""
    <div class="snowflake" style="
        left: {left}vw;
        animation-duration: {duration}s;
        animation-delay: -{delay}s;
        font-size: {size}px;
        opacity: {alpha};
    ">❄</div>
    """

# 3. OBSAH KARTY (HTML bez odsazení na začátku řádků)
content_html = """
<div class="gift-container">
<h1 style='margin:0; font-size: 2.5rem; text-shadow:2px 2px 5px black;'>🎁 Tady máš svůj dárek! ❤️</h1>
<p style='font-size: 1.2rem; text-shadow:1px 1px 3px black; margin: 20px 0;'>Klikni a rozbal si ho, beruško 🎄✨</p>
<a href="https://drive.google.com/file/d/1Dxi3R6fMb0r8k4E2TIpyJ6Y786f0ntpJ/view?usp=drive_link" target="_blank" style="text-decoration:none;">
<button class="gift-btn">🎁 Rozbalit dárek</button>
</a>
</div>
"""

# 4. SPOJENÍ A VYKRESLENÍ (Tohle je ten klíčový moment)
st.markdown(css_styles + snow_html + content_html, unsafe_allow_html=True)
