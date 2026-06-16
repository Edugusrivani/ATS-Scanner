import streamlit as st
import PyPDF2
import re

st.title("📄 ATS Resume Scanner")
job = st.text_area("Job Description:", height=150)
pdf_file = st.file_uploader("Resume PDF:", type="pdf")

STOP_WORDS = {'with', 'for', 'and', 'the', 'a', 'an', 'in', 'on', 'at', 'to', 'of', 'is', 'are', 'use', 'using', 'you', 'your'}

def clean_words(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return set([w for w in words if w not in STOP_WORDS and len(w) > 2])

if st.button("Scan Now"):
    if not job.strip() or pdf_file is None:
        st.warning("Job Desc + Resume rendu petti bro")
    else:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        resume_text = "".join([p.extract_text() or "" for p in pdf_reader.pages])
        
        job_words = clean_words(job)
        resume_words = clean_words(resume_text)
        
        match_words = job_words & resume_words
        score = len(match_words) / len(job_words) * 100 if job_words else 0
        
        st.success(f"🔥 Match Score: {score:.1f}%")
        st.progress(score/100)
        st.write(f"**Matching keywords:** {', '.join(list(match_words)[:15])}")
        st.write(f"**Missing keywords:** {', '.join(list(job_words - resume_words)[:15])}")