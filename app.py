import streamlit as st
import qrcode
from io import BytesIO
import base64

PDF_FILE = "voucher.pdf"

def generate_qr(url: str):
    qr = qrcode.make(url)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    return buf.getvalue()

st.set_page_config(page_title="Vánoční dárek ❤️", page_icon="🎁")

st.title("🎁 Vánoční dárek pro tebe ❤️")
st.write("Moje lásko, tady máš svůj speciální voucher.")

# URL svého projektu doplníš až PO deployi
target_url = "https://your-name-your-repo.streamlit.app"

qr_img = generate_qr(target_url)
st.image(qr_img, width=250, caption="Naskenuj mě ❤️")

st.write("---")

# Načtení PDF
with open(PDF_FILE, "rb") as f:
    pdf_bytes = f.read()

# Zobrazení PDF ve stránce
base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf">'
st.markdown(pdf_display, unsafe_allow_html=True)

st.download_button("📥 Stáhnout voucher", data=pdf_bytes, file_name="voucher.pdf")
