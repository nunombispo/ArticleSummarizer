import streamlit as st
from summarizer import summarize_article


# Set page title
st.set_page_config(page_title="Article Summarizer", page_icon="📜", layout="wide")


# Set title
st.title("Article Summarizer", anchor=False)
st.header("Summarize Articles with AI", anchor=False)

# Input URL
st.divider()
url = st.text_input("Enter Article URL", value="")

# Download audio
st.divider()
if url:
    with st.status("Processing...", state="running", expanded=True) as status:
        st.write("Summarizing Article...")
        summary, time_taken = summarize_article(url)
        status.update(label=f"Finished - Time Taken: {time_taken} seconds", state="complete")

    # Show Summary
    st.subheader("Summary:", anchor=False)
    st.write(summary)
