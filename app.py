import streamlit as st

st.set_page_config(
    page_title="Vánoční překvapení 🎄❤️",
    page_icon="🎁",
    layout="centered"
)

# ---- CSS PRO NEKONEČNÝ SNÍH A DÁREK ----
st.markdown("""
<style>
    /* 1. Pozadí celé stránky na černo/šedo, aby sníh vynikl */
    .stApp {
        background-color: #0e0e0e;
    }

    /* 2. Definice animace padání */
    @keyframes snowfall {
        0% { transform: translateY(-100vh); }
        100% { transform: translateY(100vh); }
    }

    /* 3. Vytvoření vloček (teček) pomocí CSS */
    .snowflake {
        position: fixed;
        top: -10vh;
        color: #FFF;
        font-size: 1em;
        font-family: Arial;
        text-shadow: 0 0 1px #000;
        animation: snowfall linear infinite;
        z-index: 9999; /* Aby byly nad vším */
        pointer-events: none; /* DŮLEŽITÉ: Aby šlo klikat skrz sníh na tlačítko! */
    }
</style>

<script>
    // Vytvoříme 50 vloček s náhodnou pozicí a rychlostí
    for(let i=0; i<50; i++) {
        let flake = document.createElement('div');
        flake.className = 'snowflake';
        flake.innerHTML = '•'; // Znak tečky (můžeš změnit na ❄ pro vločku)
        flake.style.left = Math.random() * 100 + 'vw';
        flake.style.animationDuration = (Math.random() * 3 + 2) + 's'; // Rychlost 2-5s
        flake.style.opacity = Math.random();
        flake.style.fontSize = (Math.random() * 20 + 10) + 'px'; // Velikost
        document.body.appendChild(flake);
    }
</script>

<div style="position: relative; z-index: 1; background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://github.com/Unnja/slevomat/blob/main/IMG_7797.jpg?raw=true'); background-size: cover; background-position: center; padding: 100px 20px; border-radius: 20px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.5); color: white;">
<h1 style='color:white; font-size: 3rem; text-shadow:2px 2px 10px black; margin-bottom: 20px; line-height: 1.2;'>🎁 Tady máš svůj vánoční dárek, beruško ❤️</h1>
<p style='color:white; font-size: 1.5rem; text-shadow:1px 1px 6px black; margin-bottom: 40px;'>Klikni a rozbal si ho! 🎄✨</p>
<a href="https://drive.google.com/file/d/1Dxi3R6fMb0r8k4E2TIpyJ6Y786f0ntpJ/view?usp=drive_link" target="_blank" style="text-decoration:none;">
<button style="background: linear-gradient(135deg, #ff4d4d, #ff9999); color: white; border: none; padding: 18px 36px; font-size: 22px; border-radius: 12px; cursor: pointer; box-shadow: 0 5px 15px rgba(0,0,0,0.3); transition: transform 0.2s;" onmouseover="this.style.transform='scale(1.05)';" onmouseout="this.style.transform='scale(1)';">🎁 Rozbalit dárek</button>
</a>
</div>
""", unsafe_allow_html=True)
