import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Unknow Person")
    content = """
    I'm a freelancer with a passion for travel. I enjoy hiking, reading, cooking, playing board games and love to spend time with friends and family. I'm always seeking new adventures and learning opportunities. I believe in the power of kindness, creativity, and making a positive impact on the world. I'm excited to connect with others who share similar interests.
    """
    st.info(content)

content2 = "Below you can find some apps written in Python."
st.write(content2)

col3, colempty, col4 = st.columns([3,1,3])

df = pandas.read_csv("data.csv",sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:20].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        st.write(f"[Source Code]({row['url']})")