import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Load Lottie animations
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Custom CSS for enhanced UI
st.markdown(
    """
    <style>
        body {
            background-color: #f0f0f6;
            font-family: 'Inter', sans-serif;
        }
        .main-container {
            background: linear-gradient(145deg, #ffffff, #f9fafb);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 8px 8px 18px #d1d5db, -8px -8px 20px #ffffff;
            max-width: 750px;
            margin: auto;
            text-align: center;
            animation: fadeIn 1s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .title {
            font-size: 40px;
            font-weight: 800;
            color: #1f2937;
            margin-bottom: 10px;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            animation: slideIn 1s ease-in-out;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        .subtext {
            font-size: 20px;
            color: #6b7280;
            text-align:center;
            margin-bottom: 30px;
            animation: slideIn 1.2s ease-in-out;
        }
        .input-box {
            width: 100%;
            border-radius: 15px;
            padding: 15px;
            font-size: 16px;
            border: none;
            box-shadow: inset 4px 4px 8px #d1d5db, inset -4px -4px 8px #ffffff;
            outline: none;
            transition: box-shadow 0.3s ease;
        }
        .input-box:focus {
            box-shadow: inset 6px 6px 12px #d1d5db, inset -6px -6px 12px #ffffff;
        }
        .btn {
            background: linear-gradient(145deg, #3b82f6, #2563eb);
            color: white;
            font-size: 18px;
            font-weight: 600;
            padding: 15px;
            border-radius: 15px;
            width: 100%;
            text-align: center;
            cursor: pointer;
            box-shadow: 4px 4px 10px #d1d5db, -4px -4px 10px #ffffff;
            transition: all 0.3s ease;
            border: none;
            margin-top: 20px;
        }
        .btn:hover {
            background: linear-gradient(145deg, #2563eb, #1d4ed8);
            box-shadow: 2px 2px 5px #d1d5db, -2px -2px 5px #ffffff;
            transform: translateY(-2px);
        }
        .result-container {
            margin-top: 30px;
            padding: 20px;
            border-radius: 15px;
            font-size: 20px;
            font-weight: 600;
            box-shadow: 4px 4px 8px #d1d5db, -4px -4px 8px #ffffff;
            animation: fadeIn 0.5s ease-in-out;
        }
        .success {
            background: linear-gradient(145deg, #d1fae5, #a7f3d0);
            color: #065f46;
        }
        .error {
            background: linear-gradient(145deg, #fee2e2, #fecaca);
            color: #991b1b;
        }
        .lottie-animation {
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load Lottie animation
lottie_animation = load_lottie_url("https://lottie.host/5a7a802b-24bf-471e-b523-e6b363a05b60/k3XcsauCJG.json")

# UI Components
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<div class='title'>🔍 Fake Product Review Detector</div>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Detect if a product review is genuine or fake using AI.</p>", unsafe_allow_html=True)

# Lottie Animation
if lottie_animation:
    st_lottie(lottie_animation, height=200, key="lottie", speed=1, loop=True, quality="high")

# User input
user_input = st.text_area("Paste the review to be checked:", height=150, placeholder="Enter your review here...")

# Centered Button
if st.button("Check Review", help="Click to analyze the review", key="check_button"):
    if user_input:
        with st.spinner("Analyzing review..."):
            # Simulate API call (replace with your actual API endpoint)
            try:
                response = requests.post("http://127.0.0.1:8000/predict/", json={"text": user_input})
                if response.status_code == 200:
                    result = response.json()
                    st.markdown(
                        f"<div class='result-container success'>✅ Prediction: {result['label']} (Confidence: {result['confidence']:.2f})</div>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        "<div class='result-container error'>❌ Error: Unable to get a response from the server.</div>",
                        unsafe_allow_html=True,
                    )
            except Exception as e:
                st.markdown(
                    f"<div class='result-container error'>❌ Error: {str(e)}</div>",
                    unsafe_allow_html=True,
                )
    else:
        st.warning("⚠️ Please enter a review before checking.")

st.markdown("</div>", unsafe_allow_html=True)