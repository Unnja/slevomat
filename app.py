import streamlit as st
import random

st.set_page_config(
    page_title="Vánoční překvapení 🎄❤️",
    page_icon="🎁",
    layout="centered"
)

# 1. Vygenerujeme HTML pro sníh pomocí Pythonu (obcházíme tím zákaz JavaScriptu)
snow_html = ""
for _ in range(50):
    left = random.randint(0, 100)      # Náhodná pozice zleva (0-100%)
    duration = random.uniform(2, 5)    # Náhodná rychlost padání (2-5 sekund)
    delay = random.uniform(0, 5)       # Náhodné zpoždění startu
    size = random.uniform(10, 20)      # Náhodná velikost
    alpha = random.uniform(0.4, 0.8)   # Náhodná průhlednost
    
    # Přidáme jednu vločku do HTML řetězce
    snow_html += f"""
    <div class="snowflake" style="
        left: {left}vw; 
        animation-duration: {duration}s; 
        animation-delay: -{delay}s;
        font-size: {size}px;
        opacity: {alpha};
    ">•</div>
    """

# 2. Vložíme CSS a HTML do stránky
st.markdown(f"""
<style>
    /* Tmavé pozadí stránky */
    .stApp {{
        background-color: #0e0e0e;
    }}

    /* Styl vločky */
    .snowflake {{
        position: fixed;
        top: -10vh;
        color: white;
        z-index: 9999;
        pointer-events: none; /* DŮLEŽITÉ: Sníh neblokuje klikání */
        animation: fall linear infinite;
    }}

    /* Animace padání */
    @keyframes fall {{
        0% {{ transform: translateY(-10vh); }}
        100% {{ transform: translateY(110vh); }}
    }}
</style>

{snow_html}

<div style="position: relative; z-index: 1; background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://github.com/Unnja/slevomat/blob/main/IMG_7797.jpg?raw=true'); background-size: cover; background-position: center; padding: 100px 20px; border-radius: 20px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.5); color: white;">
<h1 style='color:white; font-size: 3rem; text-shadow:2px 2px 10px black; margin-bottom: 20px; line-height: 1.2;'>🎁 Tady máš svůj vánoční dárek, beruško ❤️</h1>
<p style='color:white; font-size: 1.5rem; text-shadow:1px 1px 6px black; margin-bottom: 40px;'>Klikni a rozbal si ho! 🎄✨</p>
<a href="https://drive.google.com/file/d/1Dxi3R6fMb0r8k4E2TIpyJ6Y786f0ntpJ/view?usp=drive_link" target="_blank" style="text-decoration:none;">
<button style="background: linear-gradient(135deg, #ff4d4d, #ff9999); color: white; border: none; padding: 18px 36px; font-size: 22px; border-radius: 12px; cursor: pointer; box-shadow: 0 5px 15px rgba(0,0,0,0.3); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)';" onmouseout="this.style.transform='scale(1)';">🎁 Rozbalit dárek</button>
</a>
</div>
""", unsafe_allow_html=True)
