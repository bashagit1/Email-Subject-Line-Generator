import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Streamlit app title and description
st.title("Email Subject Line Generator")
st.write("""
    Generate catchy email subject lines for your marketing campaigns. 
    Enter a topic below, and let the AI do the rest!
""")

# Input for the email subject topic
topic = st.text_input("Enter your email subject topic:", placeholder="e.g., Digital Marketing Tips")

# Button to generate subject lines
if st.button("Generate Subject Lines"):
    if not topic.strip():
        st.warning("Please enter a topic to generate subject lines.")
    else:
        # Prepare the prompt
        subject_line_generator_prompt = f"""
        As an expert in email marketing, your task is to generate special email subject lines.

        Based on the following input: {topic}.

        Output: Return ONLY a list of 5 Subject Lines in a bulleted list.
        """

        with st.spinner("Generating subject lines..."):
            try:
                # Call the OpenAI API to generate subject lines
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": subject_line_generator_prompt,
                        }
                    ],
                    model="gpt-3.5-turbo",  # or "gpt-4" if available
                )

                # Extract the generated response
                generated_text = chat_completion.choices[0].message.content.strip()
                subject_lines = generated_text.split('\n')

                # Display the generated subject lines
                st.subheader("Generated Subject Lines")
                for line in subject_lines:
                    st.write(f"- {line.strip()}")

            except Exception as e:
                st.error(f"An error occurred: {e}")
