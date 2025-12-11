import streamlit as st
from io import BytesIO
import base64

PDF_FILE = "voucher.pdf"

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Vánoční překvapení 🎄❤️",
    page_icon="🎁",
    layout="centered"
)

# ---- CHRISTMAS BACKGROUND, SNOW, LIGHTS ----
christmas_style = """
<style>
body {
    background-image: url('https://i.imgur.com/rU7bp6W.jpg');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}

h1, h2, p {
    text-align: center;
    text-shadow: 2px 2px 6px black;
    color: white;
}

h1 { font-size: 8vw; }
h2 { font-size: 6vw; }
p  { font-size: 4vw; }

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
    left:0;
    width:100%;
    height:100%;
}

@keyframes snow {
    0% {transform: translateY(-10px);}
    100% {transform: translateY(100vh);}
}

.snowflake {
    position: fixed;
    top: -10px;
    color: white;
    font-size: 1.5em;
    z-index: 9999;
    user-select: none;
    pointer-events: none;
    animation: snow linear infinite;
}

.light {
    position: fixed;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: yellow;
    top: 0;
    animation: blink 1.5s infinite alternate;
}

@keyframes blink {
    0% {opacity:0;}
    50% {opacity:1;}
    100% {opacity:0;}
}
</style>

<!-- Snowflakes -->
<script>
for(let i=0;i<30;i++){
    let span=document.createElement('span');
    span.innerHTML='❄';
    span.className='snowflake';
    span.style.left=Math.random()*100+'vw';
    span.style.animationDuration=(3+Math.random()*5)+'s';
    span.style.fontSize=(12+Math.random()*20)+'px';
    document.body.appendChild(span);
}
</script>
"""
st.markdown(christmas_style, unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<h1>🎁 Vánoční dárek pro tebe, lásko ❤️</h1>
<p>Doufám, že ti udělá radost. Miluju tě. 🎄✨</p>
""", unsafe_allow_html=True)

st.write("---")

# ---- LOAD PDF ----
with open(PDF_FILE, "rb") as f:
    pdf_bytes = f.read()

base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

# ---- CHRISTMAS CARD AROUND PDF ----
st.markdown("""
<div style="
    background: rgba(255, 0, 0, 0.85);
    padding: 20px;
    border-radius: 25px;
    box-shadow: 0 0 25px rgba(0,0,0,0.5);
    border: 5px solid gold;
">
<h2 style='color: gold;'>🎄 Tvůj vánoční voucher 🎄</h2>
<div class='embed-container'>
""", unsafe_allow_html=True)

st.markdown(
    f'<embed src="data:application/pdf;base64,{base64_pdf}" type="application/pdf">',
    unsafe_allow_html=True
)
st.markdown("</div></div>", unsafe_allow_html=True)

# ---- DOWNLOAD BUTTON ----
st.download_button("📥 Stáhnout voucher", data=pdf_bytes, file_name="voucher.pdf")

# ---- FOOTER ----
st.markdown("""
<p style='margin-top:30px; font-size:4vw; color:white; text-shadow:2px 2px 6px black;'>
🎅 Veselé Vánoce, moje lásko ❤️
</p>
""", unsafe_allow_html=True)
