import streamlit as st
import requests

# Page settings
st.set_page_config(
    page_title="AI Prompt Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Prompt Assistant")
st.write("Enter any prompt and get the AI response.")

# Prompt input
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Example: Explain C programming language in simple terms",
    height=150
)

# Generate button
if st.button("Generate Response", type="primary"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        url = "http://localhost:11434/api/generate"

        data = {
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }

        try:
            with st.spinner("Generating response..."):

                response = requests.post(
                    url,
                    json=data,
                    timeout=120
                )

                response.raise_for_status()

                result = response.json()

                # Display AI response
                st.subheader("🤖 AI Response")
                st.write(result.get("response", "No response received."))

        except requests.exceptions.ConnectionError:
            st.error(
                "❌ Ollama is not running. "
                "Please start Ollama and try again."
            )

        except requests.exceptions.Timeout:
            st.error("⏳ Request timed out. Please try again.")

        except Exception as e:
            st.error(f"❌ Error: {e}")