import streamlit as st
from io import BytesIO
import base64

PDF_FILE = "voucher.pdf"

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Vánoční překvapení 🎄❤️",
                   page_icon="🎁",
                   layout="centered")

# ---- LOAD PDF ----
with open(PDF_FILE, "rb") as f:
    pdf_bytes = f.read()
base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

# ---- SESSION STATE pro "rozbalený dárek" ----
if "opened" not in st.session_state:
    st.session_state.opened = False

# ---- FUNKCE PRO OTEVŘENÍ DÁRKU ----
def open_gift():
    st.session_state.opened = True
    st.experimental_rerun()

# ---- HLAVNÍ STRÁNKA ----
if not st.session_state.opened:
    st.markdown("""
    <style>
    body {
        background-image: url('https://i.imgur.com/rU7bp6W.jpg');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    h1, p {
        text-align: center;
        text-shadow: 2px 2px 8px black;
        color: white;
    }
    h1 { font-size: 8vw; }
    p  { font-size: 4vw; }
    .center-btn {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>🎁 Vánoční dárek pro tebe, lásko ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p>Klikni na tlačítko a rozbal svůj voucher 🎄✨</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
    st.button("🎁 Rozbalit dárek", on_click=open_gift)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- STRÁNKA S PDF ----
else:
    st.markdown("<h2 style='text-align:center; color:#b30000;'>🎄 Tvůj vánoční voucher 🎄</h2>", unsafe_allow_html=True)
    st.markdown(
        f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf">',
        unsafe_allow_html=True
    )
    st.download_button("📥 Stáhnout voucher", data=pdf_bytes, file_name="voucher.pdf")
