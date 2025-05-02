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

st.title("Home")

# Inject into Streamlit
st.markdown(page_bg_img, unsafe_allow_html=True)


# Title and subtitle
st.markdown("<h1 style='text-align: center;'>👋 Welcome to RoboFlow Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Your all-in-one assistant for smart productivity</h3>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Action buttons in columns
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='home-button'><span></span><br></div>", unsafe_allow_html=True)

#main
st.markdown("""
<div class='landing'>
    <h4>Welcome to the **RoboFlow Analyzer** <br>
        An Interactive tool for analyzing robot movement paths <br> 
        Editing structured JSON data, <br>
        And visualizing graph-based decisions in real-time. </h4>

<ul>Whether you're testing routing algorithms, debugging pathfinding logic, or just exploring data structures, 
this app provides a seamless, intuitive experience.</ul>                
    """, unsafe_allow_html=True)



            

# Feature highlights
st.markdown("""
<div class='feature-box'>
    <h4>🚀 Features</h4>
    <ul>
        <li>Chat with an intelligent assistant</li>
        <li>Analyze text, documents, or data</li>
        <li>Customize and extend your tools</li>
    </ul>
</div>
""", unsafe_allow_html=True)




