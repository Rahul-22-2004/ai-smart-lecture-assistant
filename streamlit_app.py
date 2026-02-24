import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/upload"

st.set_page_config(page_title="AI Smart Lecture Assistant", layout="wide")

st.title("🎓 AI Smart Lecture Assistant")
st.caption("Upload lecture audio → Get notes, quiz, flashcards & PDF")

uploaded_file = st.file_uploader("Upload Lecture Audio", type=["mp3","wav","m4a"])

if uploaded_file:
    st.audio(uploaded_file)

    if st.button("🚀 Process Lecture"):

        with st.spinner("Processing lecture... AI is thinking 🧠"):

            files = {"file": uploaded_file.getvalue()}
            response = requests.post(API_URL, files={"file": (uploaded_file.name, uploaded_file.getvalue())})

            data = response.json()

        st.success("Processing complete ✅")

        # Metrics
        col1, col2 = st.columns(2)
        col1.metric("Transcript Length", len(data["transcript"]))
        col2.metric("Quiz Generated", "Yes")

        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs(["📜 Transcript","📝 Notes","❓ Quiz","🧠 Flashcards"])

        with tab1:
            st.text_area("", data["transcript"], height=300)

        with tab2:
            st.text_area("", data["notes"], height=300)

        with tab3:
            st.text_area("", data["quiz"], height=300)

        with tab4:
            st.text_area("", data["flashcards"], height=300)

        # PDF Download
        pdf_url = "http://127.0.0.1:8000" + data["pdf_path"]
        st.markdown(f"[📄 Download PDF]({pdf_url})")