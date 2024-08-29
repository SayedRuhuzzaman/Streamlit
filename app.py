import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")
