import streamlit as st
import os
from main import process_file

st.title("MCQ Processor")

# File uploader
uploaded_file = st.file_uploader("Upload a Word, PDF, or Text file", type=["docx", "pdf", "txt"])

# Output directory selector
output_dir = st.text_input("Output Directory", "../output_files")

if st.button("Process File"):
    if uploaded_file and output_dir:
        # Save the uploaded file temporarily
        input_dir = "../input_files"
        os.makedirs(input_dir, exist_ok=True)
        file_path = os.path.join(input_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Process the file
        try:
            process_file(uploaded_file.name, input_dir, output_dir)
            st.success(f"File processed successfully! Outputs saved in {output_dir}")
        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.error("Please upload a file and specify an output directory.")