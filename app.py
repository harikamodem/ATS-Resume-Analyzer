import streamlit as st
from utils.text_cleaner import clean_text

st.title("AI Resume Analyzer & ATS Scoring System")

sample = "Python, SQL & Machine Learning!"

st.write("Original Text:")
st.write(sample)

st.write("Cleaned Text:")
st.write(clean_text(sample))