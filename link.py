import streamlit as st
from urllib.parse import urlparse, urlunparse

# Page setup
st.set_page_config(page_title="Professional Link Maker")

st.title("🔗 Professional Link Maker")
st.write("Make long professional links look clean and presentable.")

# Input field
long_url = st.text_input("Paste your professional link")

# Function to clean URL
def clean_url(url):
    parsed = urlparse(url)
    return urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        '', '', ''
    ))

# Button logic
if st.button("Clean Link"):
    if long_url.strip() == "":
        st.error("Please enter a URL.")
    elif not (long_url.startswith("http://") or long_url.startswith("https://")):
        st.error("URL must start with http:// or https://")
    else:
        cleaned_link = clean_url(long_url)

        st.success("Your clean link is ready")
        st.write("**Clean Link:**")
        st.code(cleaned_link)
        
