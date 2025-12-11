import streamlit as st

PDF_FILE = "voucher.pdf"

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Vánoční překvapení 🎄❤️",
                   page_icon="🎁",
                   layout="centered")

# ---- HLAVNÍ STRÁNKA ----
st.markdown("""
<h1 style='text-align:center; color:white; text-shadow: 2px 2px 8px black; font-size:8vw;'>
🎁 Vánoční dárek pro tebe, lásko ❤️
</h1>
<p style='text-align:center; color:white; text-shadow: 1px 1px 6px black; font-size:4vw;'>
Klikni na tlačítko a rozbal svůj voucher 🎄✨
</p>
""", unsafe_allow_html=True)

# ---- ODKAZ NA PDF ----
st.markdown(f"""
<div style="text-align:center; margin-top:20px;">
    <a href="{PDF_FILE}" target="_blank">
        <button style="
            background-color:#b30000;
            color:white;
            border:none;
            padding:15px 30px;
            font-size:20px;
            border-radius:10px;
            cursor:pointer;
        ">🎁 Rozbalit dárek</button>
    </a>
</div>
""", unsafe_allow_html=True)

# ---- VOLITELNÉ STAHOVÁNÍ ----
with open(PDF_FILE, "rb") as f:
    pdf_bytes = f.read()
st.download_button("📥 Stáhnout voucher", data=pdf_bytes, file_name="voucher.pdf")
