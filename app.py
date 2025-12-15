import streamlit as st
import random

st.set_page_config(
    page_title="Vánoční překvapení 🎄❤️",
    page_icon="🎁",
    layout="centered"
)

# 1. GENERUJEME SNÍH (Python vyrobí HTML pro 50 vloček)
snow_html = ""
for _ in range(50):
    left = random.randint(0, 100)      # Pozice zleva 0-100%
    duration = random.uniform(3, 8)    # Rychlost padání
    delay = random.uniform(0, 5)       # Zpoždění startu
    size = random.uniform(8, 20)       # Velikost vločky
    alpha = random.uniform(0.3, 0.8)   # Průhlednost
    
    # Přidáme HTML pro jednu vločku
    snow_html += f"""
    <div class="snowflake" style="
        left: {left}vw; 
        animation-duration: {duration}s; 
        animation-delay: -{delay}s;
        font-size: {size}px;
        opacity: {alpha};
    ">❄</div>
    """

# 2. VYKRESLENÍ VŠEHO NAJEDNOU
# Pozor: V CSS jsou zdvojené závorky {{ }}, aby to fungovalo s f-stringem!
st.markdown(f"""
<style>
    /* Tmavé pozadí celé appky */
    .stApp {{
        background-color: #0e0e0e;
    }}
    
    /* Styl pro vločky */
    .snowflake {{
        position: fixed;
        top: -10vh;
        color: white;
        z-index: 9999;
        pointer-events: none; /* DŮLEŽITÉ: Aby šlo klikat skrz sníh */
        animation: fall linear infinite;
        text-shadow: 0 0 5px white;
    }}

    /* Animace padání */
    @keyframes fall {{
        0% {{ transform: translateY(-10vh) rotate(0deg); }}
        100% {{ transform: translateY(110vh) rotate(360deg); }}
    }}

    /* Kontejner s dárkem */
    .gift-container {{
        position: relative;
        z-index: 1;
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://github.com/Unnja/slevomat/blob/main/IMG_7797.jpg?raw=true');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.6);
        color: white;
        margin-top: 20px;
    }}

    /* Tlačítko */
    .gift-btn {{
        background: linear-gradient(135deg, #ff4d4d, #ff9999);
        color: white;
        border: none;
        padding: 18px 36px;
        font-size: 22px;
        border-radius: 12px;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s;
        text-decoration: none;
        display: inline-block;
        margin-top: 20px;
    }}
    .gift-btn:hover {{
        transform: scale(1.05);
    }}
</style>

{snow_html}

<div class="gift-container">
    <h1 style='color:white; font-size: 3rem; text-shadow:2px 2px 10px black; margin-bottom: 20px; line-height: 1.2;'>
        🎁 Tady máš svůj vánoční dárek, beruško ❤️
    </h1>
    <p style='color:white; font-size: 1.5rem; text-shadow:1px 1px 6px black; margin-bottom: 30px;'>
        Klikni a rozbal si ho! 🎄✨
    </p>
    <a href="https://drive.google.com/file/d/1Dxi3R6fMb0r8k4E2TIpyJ6Y786f0ntpJ/view?usp=drive_link" target="_blank" style="text-decoration:none;">
        <button class="gift-btn">
            🎁 Rozbalit dárek
        </button>
    </a>
</div>
""", unsafe_allow_html=True)
