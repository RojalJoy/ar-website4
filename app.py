import streamlit as st

st.title("AR Experience with AI Integration")

# Button to redirect to AR page
if st.button('Launch AR Experience'):
    js = "window.location.href = 'https://rojaljoy.github.io/ar-website4/'"  # path to your AR page
    html = f"<script>{js}</script>"
    st.components.v1.html(html, height=0)
