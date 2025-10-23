import streamlit as st

st.title("📂 Download File Organizer Desktop App")
st.write("Click the button below to download the desktop app and organize your folders locally.")

# URL to your .exe on GitHub Releases
exe_url = "https://github.com/Shameerburney/FileOrganizer/releases/download/v1/file_organizer.exe"

st.markdown(f"[⬇️ Download File Organizer]({exe_url})")

