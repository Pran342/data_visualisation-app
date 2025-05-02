import streamlit as st
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpaperaccess.com/full/2881108.jpg");
    background-size: cover;
    background-position: center;
    opacity: 100%;
}

[data-testid="stSidebar"] {
    background-image: url("https://24.media.tumblr.com/e6747bd33481310223189274ee767345/tumblr_mkfaw4AyVV1s97ldco1_500.jpg");
    background-size: inherit;
}
</style>
"""

st.sidebar.title("RoboFlow Analyzer")

st.title("🤖 About the Robot Path Planner")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("### Empowering Data-Driven Navigation and Decision-Making")

st.markdown("""
The **Robot Path Planner** is an interactive Streamlit-based application designed to simplify and enhance the way 
we interact with structured data and pathfinding algorithms. This tool is especially crafted for students, researchers, and developers 
who are working with graph-based systems, robotics, logistics, and AI decision-making pipelines.

---

### 🛠️ What We Do

- 📂 Upload & Edit JSON Data  
- 📊 Analyze Optimized Paths  
- 🔄 Live Visualization & Feedback  
- 🧠 Retain App State  

---

### 🔍 Why We Built It

We wanted a tool that’s simple, powerful, and intuitive for graph-based routing tasks — without the overhead of a bulky framework.  

---

### 🚧 What’s Under the Hood?

- Built with **Streamlit**
- Uses **NetworkX** for pathfinding
- Real-time editing via custom JSON editor
- Python-powered performance and visuals

---


### 💬 Feedback & Contributions

We’re open to ideas, bugs, and feature requests.  
Let’s make path planning smarter — together.

---

_Made with ❤️ and Python._
""")
