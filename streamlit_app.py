import streamlit as st

from langchain.llms import openai
#from langchain.text_splitter import CharacterTextSplitter
#from langchain.embeddings import OpenAIEmbeddings
#from langchain.vectorstores import Chroma
#from langchain.chains import RetrievalQA


#st.set_page_config(page_title='🦜 Pearson Career Coach App')
st.title('🦜 Welcome to Pearsonify, your personal career coach')


## a good place to start is with a CV
#uploaded_file = st.file_uploader('Upload an your resume, it can be in any format such as a downloaded linkedin pdf', type='txt')

## query
#query_text = st.text_input('Enter your question:', placeholder = 'Please provide a short summary.', disabled=not uploaded_file)

st.write('Hello world!')
