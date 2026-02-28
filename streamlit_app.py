import streamlit as st
import requests

API_URL = "/upload"

st.set_page_config(page_title="AI Smart Lecture Assistant", layout="wide")

st.title("🎓 AI Smart Lecture Assistant")
st.caption("Upload lecture audio → Get structured notes, quiz, flashcards & PDF")

uploaded_file = st.file_uploader("Upload Lecture Audio", type=["mp3","wav","m4a"])

# Session storage
if "data" not in st.session_state:
    st.session_state.data = None

if uploaded_file:
    st.audio(uploaded_file)

    if st.button("🚀 Process Lecture"):

        with st.spinner("Processing lecture... AI is thinking 🧠"):
            try:
                response = requests.post(
                    API_URL,
                    files={"file": (uploaded_file.name, uploaded_file.getvalue())}
                )
                st.session_state.data = response.json()
            except Exception as e:
                st.error(f"Backend error: {e}")

        st.success("Processing complete ✅")

# ---------------- DISPLAY RESULTS ----------------
if st.session_state.data:

    data = st.session_state.data

    if "error" in data:
        st.error(data["error"])
        st.stop()

    required = ["transcript","notes","quiz","flashcards","pdf_path"]
    if not all(k in data for k in required):
        st.warning("Incomplete response from backend")
        st.json(data)
        st.stop()

    # Metrics
    col1, col2 = st.columns(2)
    col1.metric("Transcript Length", len(data["transcript"]))
    col2.metric("Quiz Generated", "Yes")

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📜 Transcript","📝 Notes","❓ Quiz","🧠 Flashcards"])

    # -------- Transcript --------
    with tab1:
        st.markdown("### Transcript")
        st.write(data["transcript"])

    # -------- Notes (Markdown Rendering) --------
    with tab2:
        st.markdown("### Structured Notes")
        st.markdown(data["notes"])

    # -------- Quiz (ONLY inside tab3) --------
    with tab3:
        st.subheader("Interactive Quiz")

        if isinstance(data["quiz"], list) and len(data["quiz"]) > 0:

            if "quiz_answers" not in st.session_state:
                st.session_state.quiz_answers = {}

            for i, q in enumerate(data["quiz"]):

                st.markdown(f"### Question {i+1}")
                st.write(q["question"])

                selected = st.radio(
                    "Select an option:",
                    q["options"],
                    key=f"quiz_{i}"
                )

                st.session_state.quiz_answers[i] = selected

            if st.button("Submit Quiz"):

                score = 0

                for i, q in enumerate(data["quiz"]):
                    if st.session_state.quiz_answers.get(i) == q["answer"]:
                        score += 1

                st.success(f"Your Score: {score} / {len(data['quiz'])}")

                for i, q in enumerate(data["quiz"]):
                    st.markdown(f"**Q{i+1}:** {q['question']}")
                    st.write(f"Correct Answer: {q['answer']}")
                    st.info(q["explanation"])

        else:
            st.warning("Quiz parsing failed.")

    # -------- Flashcards --------
    with tab4:
        st.markdown("### Flashcards")
        st.markdown(data["flashcards"])

    # -------- PDF Download --------
    pdf_url = "http://127.0.0.1:8000" + data["pdf_path"]
    st.markdown(f"[📄 Download PDF]({pdf_url})")