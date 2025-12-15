import streamlit as st

st.set_page_config(
    page_title="Vánoční překvapení 🎄❤️",
    page_icon="🎁",
    layout="centered"
)

# ---- HLAVNÍ CONTAINER S POZADÍM ----
st.markdown("""
<div style="
    background-image: url('https://github.com/Unnja/slevomat/blob/main/IMG_7797.jpg?raw=true');
    background-size: cover;
    background-position: center;
    padding: 100px 20px;
    border-radius: 20px;
    text-align: center;
">
    <h1 style='color:white; font-size:8vw; text-shadow:2px 2px 10px black;'>🎁 Tady máš svůj vánoční dárek, beruško ❤️</h1>
    <p style='color:white; font-size:4vw; text-shadow:1px 1px 6px black;'>Klikni a rozbal si ho! 🎄✨</p>
    <a href="https://drive.google.com/file/d/1Dxi3R6fMb0r8k4E2TIpyJ6Y786f0ntpJ/view?usp=drive_link" target="_blank">
        <button style="
            background: linear-gradient(135deg, #ff4d4d, #ff9999);
            color:white;
            border:none;
            padding:18px 36px;
            font-size:22px;
            border-radius:12px;
            cursor:pointer;
            box-shadow:0 5px 15px rgba(0,0,0,0.3);
            transition: transform 0.2s;
        " onmouseover="this.style.transform='scale(1.05)';" onmouseout="this.style.transform='scale(1)';">🎁 Rozbalit dárek</button>
    </a>
</div>
""", unsafe_allow_html=True)
