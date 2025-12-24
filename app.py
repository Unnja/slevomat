st.markdown(f"""
<style>
.stApp {{
    background-color: #0e0e0e;
}}
.gift-container {{
    background-image:
        linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
        url("data:image/jpeg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    padding: 100px 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.6);
    color: white;
}}
.gift-btn {{
    background: linear-gradient(135deg, #ff4d4d, #ff9999);
    color: white;
    border: none;
    padding: 18px 36px;
    font-size: 22px;
    border-radius: 12px;
    cursor: pointer;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    transition: transform 0.2s;
    text-decoration: none;
    display: inline-block;
    margin-top: 20px;
}}
.gift-btn:hover {{
    transform: scale(1.05);
}}
</style>

<div class="gift-container">
<h1 style='margin:0; font-size: 3rem; text-shadow:2px 2px 10px black; line-height: 1.2;'>
🎁 Tady máš svůj vánoční dárek, bobku. ❤️
</h1>
<p style='font-size: 1.5rem; text-shadow:1px 1px 6px black; margin: 30px 0;'>
Klikni a rozbal si ho! 🎄✨
</p>
<a href="https://drive.google.com/file/d/1Dxi3R6fMb0r8k4E2TIpyJ6Y786f0ntpJ/view" target="_blank">
<button class="gift-btn">🎁 Rozbalit dárek</button>
</a>
</div>
""", unsafe_allow_html=True)
