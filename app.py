import streamlit as st
import random

# Set Page Configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟", layout="centered")

# Custom Styling
st.markdown("""
    <style>                   
        body { background: linear-gradient(to right, #ffecd2, #fcb69f); }
        .main-title { text-align: center; color: #FF5733; font-size: 42px; font-weight: bold; border-bottom: 5px solid #FFC300; padding-bottom: 10px; text-shadow: 3px 3px 6px rgba(0,0,0,0.3); }
        .sub-title { text-align: center; color: #FFC300; font-size: 28px; text-shadow: 2px 2px 5px rgba(0,0,0,0.3); }
        .quote-box { background: #2E86C1; color: white; font-size: 20px; text-align: center; font-style: italic; padding: 15px; border-radius: 10px; box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); }
        .section { background: linear-gradient(to right, #ffffff, #ffcccb); padding: 20px; border-radius: 15px; box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); margin-bottom: 20px; }
        .footer { text-align: center; font-size: 16px; color: white; background: #333; padding: 15px; border-radius: 10px; margin-top: 30px; box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""<h1 class='main-title'>🌱 Growth Mindset Challenge</h1>""", unsafe_allow_html=True)

# Header
st.markdown("""<h2 class='sub-title'>🎀 Welcome to Your Growth Journey!</h2>""", unsafe_allow_html=True)

# Introduction
st.markdown("""
    <div class='section'>
        This app is designed to help you develop a **growth mindset** by setting challenges, tracking progress, and learning new skills. 
        Embrace the journey of self-improvement! 🚀
    </div>
""", unsafe_allow_html=True)

# Random Motivational Quotes
quotes = [
    "“Believe you can and you're halfway there.” – Theodore Roosevelt",
    "“Do what you can, with what you have, where you are.” – Theodore Roosevelt",
    "“Your only limit is your mind.”",
    "“Growth and comfort do not coexist.” – Ginni Rometty",
    "“Doubt kills more dreams than failure ever will.”",
    "“The expert in anything was once a beginner.”",
]
st.markdown(f"""<div class='quote-box'>{random.choice(quotes)}</div>""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.header("📌 Navigation")
st.sidebar.write("Use the sidebar to explore different sections.")

# User Input - Daily Challenge
st.markdown("""<div class='section'>""", unsafe_allow_html=True)
st.subheader("📝 Set Your Daily Challenge")
challenge = st.text_input("What challenge will you take on today?", placeholder="E.g., Read 10 pages of a book")
if challenge:
    st.success(f"Great! Your challenge for today is: **{challenge}** 🎯")
st.markdown("</div>", unsafe_allow_html=True)

# User Reflection
st.markdown("""<div class='section'>""", unsafe_allow_html=True)
st.subheader("💭 Reflect on Your Learning")
reflection = st.text_area("Write about what you learned today")
if reflection:
    st.success("Great insight! Reflection helps you grow! 🌟")
st.markdown("</div>", unsafe_allow_html=True)

# Achievements
st.markdown("""<div class='section'>""", unsafe_allow_html=True)
st.subheader("🏆 Celebrate Your Wins")
achievement = st.text_input("Share an achievement from today", placeholder="E.g., Completed a coding problem")
if achievement:
    st.balloons()
    st.success(f"Amazing! You accomplished: **{achievement}** 🎉")
st.markdown("</div>", unsafe_allow_html=True)

# Progress Tracking with Dynamic Response
st.markdown("""<div class='section'>""", unsafe_allow_html=True)
st.subheader("📊 Track Your Progress")
progress = st.slider("How much progress have you made today?", 0, 100, 50)
if progress < 50:
    st.warning("You're getting there! Keep pushing forward! 💪")
elif progress < 100:
    st.info("Almost there! Stay consistent! 🚀")
else:
    st.balloons()
    st.success("🎉 Congratulations! You've completed today's challenge! Keep up the great work! 🎉")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer'>
        💖 Keep pushing forward and embrace the power of growth! 🚀
        <br>
        <b>Created by <span style='color: #FF5733;'>Nousheen Atif</span></b>
    </div>
""", unsafe_allow_html=True)
1