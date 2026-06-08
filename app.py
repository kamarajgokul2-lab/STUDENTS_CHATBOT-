import streamlit as st
import google.generativeai as genai

# Configure page
st.set_page_config(
    page_title="Student Project Chatbot",
    page_icon="🎓"
)

st.title("🎓 Student Project Chatbot")
st.write("Ask project ideas, coding doubts, technology suggestions, and more.")

# Gemini API Key from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-3.5-flash")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input
prompt = st.chat_input("Ask anything about projects...")

if prompt:

    # Display user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # System Prompt
    system_prompt = """
    You are a Student Project Assistant.

    Help students with:
    - Final year projects
    - Mini projects
    - AI/ML projects
    - Web Development
    - Mobile App Development
    - Python Programming
    - Project Documentation
    - Technology Selection

    Give beginner-friendly explanations.
    """

    try:
        response = model.generate_content(
            system_prompt + "\n\nUser: " + prompt
        )

        answer = response.text

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

    except Exception as e:
        st.error(f"Error: {e}")
