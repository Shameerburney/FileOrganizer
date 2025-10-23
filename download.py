import streamlit as st
import os

st.title("📂 Download File Organizer Desktop App")
st.write("Click the button below to download the desktop app and organize your folders locally.")

# Full path to your .exe
exe_path = r"C:\Ipynb\dist\file_organizer.exe"

# Check if file exists
if os.path.exists(exe_path):
    with open(exe_path, "rb") as f:
        st.download_button(
            label="Download File Organizer",
            data=f,
            file_name="Shameer_File_Organizer.exe",
            mime="application/octet-stream"
        )
    st.success("✅ Click the button to download the app!")
else:
    st.error("❌ file_organizer.exe not found at C:\\Ipynb\\dist")
