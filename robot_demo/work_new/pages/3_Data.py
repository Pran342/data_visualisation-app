import streamlit as st
import json
import networkx as nx
import matplotlib.pyplot as plt
import random
import os
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter
from streamlit.components.v1 import html
from collections import defaultdict
from matplotlib.patches import FancyArrowPatch

# Initialize page configuration
st.set_page_config(layout="wide", page_title="Robot Capability Event Analysis System")

st.sidebar.title("RoboFlow Analyzer")

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

st.title("Data Input")

# Inject into Streamlit
st.markdown(page_bg_img, unsafe_allow_html=True)

def json_editor_component():
    formatter = HtmlFormatter(style="colorful", full=True, cssclass="highlight")

    col1, col2 = st.columns([1, 1])
    with col1:
        new_json = st.text_area(
            "📝 Edit JSON Content",
            value=st.session_state.raw_json,
            height=600,
            key=f"editor_{st.session_state.editor_key}",
            help="Click save button after modification to update charts"
        )

        if st.button("💾 Save Changes", type="primary"):
            try:
                if "uploaded_file" in st.session_state:
                    del st.session_state.uploaded_file
                    st.session_state.file_processed = False

                parsed = json.loads(new_json)
                processed = process_capability_data(parsed)
                st.session_state.json_data = processed
                st.session_state.raw_json = json.dumps(
                    parsed,
                    indent=2,
                    ensure_ascii=False
                )
                st.session_state.max_time = processed["max_time"]
                st.session_state.editor_key += 1
                st.rerun()
            except Exception as e:
                st.error(f"Save failed: {str(e)}")

    with col2:
        st.markdown("Live Preview")
        if st.session_state.raw_json:
            html_code = highlight(
                st.session_state.raw_json,
                JsonLexer(),
                formatter
            )
            html(f'<div class="highlight">{html_code}</div>', height=600, scrolling=True)

    
if st.session_state:
        st.header("📂 Data Input")
        if st.session_state.raw_json:
            json_editor_component()
        else:
            st.info("Please upload a JSON file in the App to start editing and live preview.")
