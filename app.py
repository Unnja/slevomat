import streamlit as st

# 1. Konfigurace stránky
st.set_page_config(
    page_title="Vánoční překvapení 🎄❤️",
    page_icon="🎁",
    layout="centered"
)

# 2. Efekt sněžení
st.snow()

# 3. HTML/CSS styl a obsah
st.markdown("""
<div style="
    position: relative;
    /* Odkaz na tvůj obrázek z GitHubu s efektem ztmavení, aby šel přečíst text */
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://github.com/Unnja/slevomat/blob/main/IMG_7797.jpg?raw=true');
    background-size: cover;
    background-position: center;
    padding: 100px 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    color: white;
">
    <h1 style='color:white; font-size: 3rem; text-shadow:2px 2px 10px black; margin-bottom: 20px; line-height: 1.2;'>
        🎁 Tady máš svůj vánoční dárek, beruško ❤️
    </h1>
    
    <p style='color:white; font-size: 1.5rem; text-shadow:1px 1px 6px black; margin-bottom: 40px;'>
        Klikni a rozbal si ho! 🎄✨
    </p>
    
    <a href="https://drive.google.com/file/d/1Dxi3R6fMb0r8k4E2TIpyJ6Y786f0ntpJ/view?usp=drive_link" target="_blank" style="text-decoration:none;">
        <button style="
            background: linear-gradient(135deg, #ff4d4d, #ff9999);
            color: white;
            border: none;
            padding: 18px 36px;
            font-size: 22px;
            border-radius: 12px;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: transform 0.2s;
        " onmouseover="this.style.transform='scale(1.05)';" onmouseout="this.style.transform='scale(1)';">
            🎁 Rozbalit dárek
        </button>
    </a>
</div>
""", unsafe_allow_html=True)
