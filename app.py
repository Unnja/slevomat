import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Vánoční překvapení 🎄❤️",
    page_icon="🎁",
    layout="centered"
)

# ---- HLAVNÍ STRÁNKA ----
st.markdown("""
<style>
body {
    background-image: url('https://i.imgur.com/rU7bp6W.jpg');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}

/* Nadpis a text */
h1, p {
    text-align: center;
    text-shadow: 2px 2px 10px black;
    color: white;
}

/* Responzivní text */
h1 { font-size: 8vw; }
p  { font-size: 4vw; }

/* Styl tlačítka */
.button-container {
    display: flex;
    justify-content: center;
    margin-top: 30px;
}

.button-style {
    background: linear-gradient(135deg, #ff4d4d, #ff9999);
    color: white;
    border: none;
    padding: 18px 36px;
    font-size: 22px;
    border-radius: 12px;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    transition: transform 0.2s;
}
.button-style:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎁 Vánoční dárek pro tebe, lásko ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p>Klikni na tlačítko a rozbal svůj voucher 🎄✨</p>", unsafe_allow_html=True)

# ---- ODKAZ NA PDF ----
google_drive_link = "https://drive.google.com/file/d/1Dxi3R6fMb0r8k4E2TIpyJ6Y786f0ntpJ/view?usp=drive_link"

st.markdown(f"""
<div class="button-container">
    <a href="{google_drive_link}" target="_blank">
        <button class="button-style">🎁 Rozbalit dárek</button>
    </a>
</div>
""", unsafe_allow_html=True)
