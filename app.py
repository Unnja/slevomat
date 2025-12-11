import streamlit as st
from io import BytesIO
import base64

PDF_FILE = "voucher.pdf"

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Vánoční překvapení 🎄❤️", page_icon="🎁", layout="wide")

# ---- CHRISTMAS BACKGROUND ----
page_bg = """
<style>
body {
    background-image: url('https://i.imgur.com/rU7bp6W.jpg');
    background-size: cover;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<h1 style='text-align:center; color:#fff; text-shadow: 0px 0px 15px black; font-size:60px;'>
🎁 Vánoční dárek pro tebe, lásko ❤️
</h1>
<p style='text-align:center; color:white; font-size:22px; text-shadow: 0px 0px 8px black;'>
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
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(0,0,0,0.4);
">
<h2 style='text-align:center; color:#b30000;'>
🎄 Tvůj vánoční voucher 🎄
</h2>
""", unsafe_allow_html=True)

st.markdown(
    f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf">',
    unsafe_allow_html=True
)

st.markdown("""
</div>
""", unsafe_allow_html=True)

# ---- DOWNLOAD ----
st.download_button("📥 Stáhnout voucher", data=pdf_bytes, file_name="voucher.pdf")

# ---- FOOTER ----
st.markdown("""
<p style='text-align:center; margin-top:40px; color:white; text-shadow: 0px 0px 8px black; font-size:18px;'>
🎅 Veselé Vánoce, moje lásko ❤️
</p>
""", unsafe_allow_html=True)
