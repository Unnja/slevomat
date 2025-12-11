import streamlit as st
from io import BytesIO
import base64

PDF_FILE = "voucher.pdf"

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Vánoční překvapení 🎄❤️",
                   page_icon="🎁", layout="centered")

# ---- CHRISTMAS BACKGROUND ----
page_bg = """
<style>
body {
    background-image: url('https://i.imgur.com/rU7bp6W.jpg');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---- RESPONSIVE STYLING ----
responsive_style = """
<style>
h1 {
    font-size: 8vw !important;  /* Nadpis se přizpůsobí šířce obrazovky */
}
h2 {
    font-size: 6vw !important;
}
p {
    font-size: 4vw !important;
}
.embed-container {
    position: relative;
    padding-bottom: 125%;
    height: 0;
    overflow: hidden;
    max-width: 100%;
}
.embed-container embed {
    position: absolute;
    top:0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>
"""
st.markdown(responsive_style, unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<h1 style='text-align:center; color:#fff; text-shadow: 0px 0px 15px black;'>
🎁 Vánoční dárek pro tebe, lásko ❤️
</h1>
<p style='text-align:center; color:white; text-shadow: 0px 0px 8px black;'>
Doufám, že ti udělá radost. Miluju tě. 🎄✨
</p>
""", unsafe_allow_html=True)

st.write("---")

# ---- LOAD PDF ----
with open(PDF_FILE, "rb") as f:
    pdf_bytes = f.read()

base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

# ---- CHRISTMAS CARD AROUND PDF ----
st.markdown("""
<div style="
    background: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
">
<h2 style='text-align:center; color:#b30000;'>🎄 Tvůj vánoční voucher 🎄</h2>
<div class='embed-container'>
""", unsafe_allow_html=True)

st.markdown(
    f'<embed src="data:application/pdf;base64,{base64_pdf}" type="application/pdf">',
    unsafe_allow_html=True
)

st.markdown("</div></div>", unsafe_allow_html=True)

# ---- DOWNLOAD ----
st.download_button("📥 Stáhnout voucher", data=pdf_bytes, file_name="voucher.pdf")

# ---- FOOTER ----
st.markdown("""
<p style='text-align:center; margin-top:30px; color:white; text-shadow: 0px 0px 6px black; font-size:4vw;'>
🎅 Veselé Vánoce, moje lásko ❤️
</p>
""", unsafe_allow_html=True)
