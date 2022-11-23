import streamlit
import pandas
streamlit.set_page_config(layout="wide")

col1, col2 = streamlit.columns(2)

with col1:
    streamlit.image("images/photo.png")

with col2:
    streamlit.title("Anurag Yadav")
    content = """
    Hi, I am Anurag Yadav! I am a Student.
    """
    streamlit.info(content)

content2= """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
streamlit.write(content2)

col3,empty_col, col4 = streamlit.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index,row in df[:10].iterrows():
        streamlit.header(row["title"])
        streamlit.write(row["description"])
        streamlit.image("images/" + row["image"])
        streamlit.write(f"[Source Code]({row['url']})")
with col4:
    for index,row in df[10:].iterrows():
        streamlit.header(row["title"])
        streamlit.write(row["description"])
        streamlit.image("images/" + row["image"])
        streamlit.write(f"[Source Code]({row['url']})")
