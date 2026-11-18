import streamlit as st

st.set_page_config(page_title="Armenian Subtitle Editor", page_icon="🎬")

st.title("🎬 Armenian Subtitle Editor")
st.write("Upload your video to create English subtitles.")

video = st.file_uploader(
    "Upload your video",
    type=["mp4", "mov", "m4v"]
)

if video:
    st.video(video)
    st.success("Video uploaded successfully!")
