
import os
import streamlit as st

DEFAULT_MODEL = "HuggingFaceTB/SmolLM2-360M-Instruct"

st.set_page_config(
    page_title="International Marketing AI",
    page_icon="🌍",
    layout="centered"
)

# -----------------------------
# Load Hugging Face Model
# -----------------------------
@st.cache_resource(show_spinner="Loading AI Model...")
def get_llm(model_id):
    from transformers import AutoTokenizer, pipeline

    tokenizer = AutoTokenizer.from_pretrained(model_id)

    text_generator = pipeline(
        "text-generation",
        model=model_id,
        tokenizer=tokenizer,
    )

    return text_generator


# -----------------------------
# Generate Marketing Content
# -----------------------------
def generate_marketing_content(product_name, model_id):

    llm = get_llm(model_id)

    prompt = f"""
You are an International Business Marketing Expert.

Generate professional global marketing content for the product: {product_name}

Generate the following:

1. Global Product Title
2. Powerful Marketing Slogan
3. Emotional Marketing Advertisement
4. Luxury Brand Advertisement
5. Digital Marketing Advertisement

Use professional and attractive international marketing language.
"""

    output = llm(
        prompt,
        max_new_tokens=250,
        temperature=0.7,
        do_sample=True,
    )

    return output[0]["generated_text"]


# -----------------------------
# UI Design
# -----------------------------
st.title("🌍 International Business Marketing AI App")

st.markdown("Generate Global Marketing Content using Generative AI")

# Sidebar
with st.sidebar:
    st.header("⚙ Settings")

    model_id = st.text_input(
        "Hugging Face Model",
        value=os.getenv("HF_MODEL_ID", DEFAULT_MODEL)
    )

    st.markdown("---")
    st.markdown("### Example Products")
    st.write("• Smart Watch")
    st.write("• Herbal Tea")
    st.write("• Electric Bike")
    st.write("• Gaming Laptop")


# -----------------------------
# User Input
# -----------------------------
product_name = st.text_input(
    "Enter Product Name",
    placeholder="Example: Smart Watch"
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("Generate Marketing Content"):

    if product_name == "":
        st.warning("Please enter a product name.")
    else:

        with st.spinner("Generating International Marketing Content..."):

            try:
                result = generate_marketing_content(
                    product_name,
                    model_id
                )

                st.success("Content Generated Successfully!")

                st.markdown("## ✨ AI Generated Marketing Content")

                st.write(result)

            except Exception as e:
                st.error(f"Error: {e}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Developed using Streamlit + Hugging Face + Prompt Engineering")
