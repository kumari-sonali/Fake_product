import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Load Lottie animation
def load_lottie_url(url):
    return requests.get(url).json()

lottie_animation = load_lottie_url("https://lottie.host/5a7a80b2-24bf-471e-b523-e6b363ae05b60/k3XcsaucJG.json")

# Streamlit UI Setup
st.set_page_config(page_title="Fake Review Detector", layout="wide")

# Sidebar
with st.sidebar:
    st.title("Fake Review Detector")
    st.write("A tool to detect if a product review is fake or genuine using AI.")
    st_lottie(lottie_animation, height=200, key="lottie")

# Main Page Layout
st.markdown("<h1 style='text-align: center; color: blue;'>Fake Review Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Enter a product review to check its authenticity.</p>", unsafe_allow_html=True)

# User Input
user_input = st.text_area("Paste the review to be checked:", height=150, placeholder="Enter your review here...")

# Button to Check Review
if st.button("Check Review", help="Click to analyze the review"):
    if user_input:
        with st.spinner("Analyzing review..."):
            try:
                response = requests.post("http://127.0.0.1:8000/predict/", json={"text": user_input})
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"Prediction: {result['label']} (Confidence: {result['confidence']:.2f})")
                else:
                    st.error("❌ Error: Unable to get a response from the server.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a review before checking.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
