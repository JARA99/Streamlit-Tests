import streamlit as st

st.title('Try to add text')

def write(text):
    f = open('edit_file.txt','a')
    f.write('New input: {}\n'.format(text))
    f.close()

text = st.text_input('Text')
st.button('Add text to file',on_click = write,args = [text])
