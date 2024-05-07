import streamlit as st
from transformers import pipeline

# Load the Hugging Face model from the Hub
@st.cache_resource
def load_model(model_name):
    model = pipeline("text-generation", model=model_name)
    return model

# Streamlit app
def app():
    st.title("Text Generation with Custom Hugging Face Model")

    # Load the model
    model_name = "MorTal007/Mimicker"
    model = load_model(model_name)

    # Get user input for the prompt
    prompt = st.text_area("Enter your prompt:", height=200)

    if st.button("Generate"):
        if prompt:
            # Generate text with the model
            response = model(prompt, max_length=200, num_return_sequences=1)[0]["generated_text"]

            # Display the response
            st.success(f"Response: {response}")
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    app()