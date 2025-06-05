import streamlit as st
import pandas as pd
from datetime import datetime

# Data Structures
timelines_data = {
    "Timeline 1 Name": {
        "priority": 1, # Lower number means higher priority
        "tasks": [
            {"id": "t1_task1", "description": "Design database schema", "due_date": "2025-06-10", "completed": False, "notes": ""},
            {"id": "t1_task2", "description": "Develop API endpoints", "due_date": "2025-06-15", "completed": False, "notes": ""},
        ]
    },
    "Timeline 2 Name": {
        "priority": 2,
        "tasks": [
            {"id": "t2_task1", "description": "Morning Jog", "due_date": "daily", "completed": False, "notes": ""},
            {"id": "t2_task2", "description": "Read a chapter", "due_date": "daily", "completed": False, "notes": ""},
        ]
    }
}

# Configure and Initialize
st.set_page_config(layout="wide", page_title="Timeline Vis")

# --- Main App ---
st.title("⏳ Timeline Task Prioritizer")
st.caption("Organize your tasks across different timelines and prioritize the timelines themselves.")
