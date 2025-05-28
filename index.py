import streamlit as st
import random
import time

# Set up Streamlit page
st.set_page_config(page_title="🎯 Growth Mindset Challenge Spinner", layout="wide")

# Custom styles
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .main-title {
            text-align: center;
            color: #2E8B57;
            font-size: 2.5rem;
            font-weight: bold;
        }
        .dashboard-title {
            font-size: 1.5rem;
            font-weight: bold;
            color: #333;
        }
        .challenge-box {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-top: 20px;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 0.9rem;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown("<h2 class='dashboard-title'>📌 Menu</h2>", unsafe_allow_html=True)
    page = st.radio("Choose a section:", ["Home", "My Progress", "Contact"], index=0, key="sidebar_radio")
    st.session_state.sidebar_open = False

# Growth challenges
challenges = [
    "Try something new today",
    "Turn a failure into a lesson",
    "Give yourself positive feedback",
    "Step out of your comfort zone",
    "Teach someone what you just learned",
    "Reframe a negative thought into a positive one",
    "Ask for feedback and apply it",
    "Celebrate a small win today",
    "Write down three things you are grateful for",
    "Keep going even when it gets tough"
]

# Initialize session state
if "completed_challenges" not in st.session_state:
    st.session_state["completed_challenges"] = []

if "spin_result" not in st.session_state:
    st.session_state["spin_result"] = "Press the button to spin the wheel!"

# Spinner logic
def spin_wheel():
    with st.spinner("Spinning the wheel..."):
        time.sleep(2)
    st.session_state["spin_result"] = random.choice(challenges)

# Mark challenge as done
def complete_challenge():
    challenge = st.session_state["spin_result"]
    if challenge not in st.session_state["completed_challenges"]:
        st.session_state["completed_challenges"].append(challenge)

# Home page
if page == "Home":
    st.markdown("<h1 class='main-title'>🎯 Growth Mindset Challenge Spinner</h1>", unsafe_allow_html=True)
    st.write("Click the button below to spin the wheel and take on a new mindset-building challenge!")

    st.markdown("<div class='challenge-box'>", unsafe_allow_html=True)
    st.subheader("Your Challenge:")
    st.write(f"**{st.session_state['spin_result']}**")
    st.markdown("</div>", unsafe_allow_html=True)

    st.button("🎰 Spin the Wheel", on_click=spin_wheel)
    st.button("✅ Mark as Completed", on_click=complete_challenge)

# Progress page
elif page == "My Progress":
    st.subheader("📊 Progress Tracker")
    st.write(f"You've completed {len(st.session_state['completed_challenges'])} out of {len(challenges)} challenges.")

    if st.session_state["completed_challenges"]:
        st.write("### Completed Challenges:")
        for challenge in st.session_state["completed_challenges"]:
            st.write(f"- ✅ {challenge}")
    else:
        st.info("You haven't completed any challenges yet. Try spinning the wheel on the Home page!")

# Contact page
elif page == "Contact":
    st.subheader("📬 Get in Touch")
    st.write("If you'd like to connect or collaborate, feel free to reach out!")
    st.write("📌 **GitHub:** [FaybieBakshi](https://github.com/FaybieBakshi)")

# Footer
st.markdown("<div class='footer'>Made with 💻 by Urooj</div>", unsafe_allow_html=True)