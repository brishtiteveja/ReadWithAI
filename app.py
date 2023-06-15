# Import os to set API key
import os, sys
# Import OpenAI as main LLM service
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
# Bring in streamlit for UI/app interface
import streamlit as st
from io import StringIO
import time
import shutil

# Import PDF document loaders...there's other ones as well!
from langchain.document_loaders import PyPDFLoader
# Import chroma as the vector store 
from langchain.vectorstores import Chroma

# Import vector store stuff
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

# remove temp files and directory
doc_dir = "./docs/"
tmp_dir = os.path.abspath(doc_dir) + '/tmp/'  
if os.path.exists(tmp_dir):
    shutil.rmtree(tmp_dir)

st.title('🦜🔗 GPT PDF reader')

# Set APIkey for OpenAI Service
# Can sub this out for other LLM providers
if os.environ['OPENAI_API_KEY'] ==  "":
    st.info("Please specify OPENAI_API_KEY in the environment file .env")

# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.1, verbose=True)
embeddings = OpenAIEmbeddings()

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.info('File uploaded successfully')

    bytes_data = uploaded_file.getvalue()

    # create temp dir for pdf loader
    
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
 
    pdf_file_name = uploaded_file.name
    pdf_file_path = tmp_dir + pdf_file_name
    # create temp file
    f = open( pdf_file_path, 'wb')
    f.write(bytes_data)

    # Create and load PDF Loader
    loader = PyPDFLoader(pdf_file_path)

    

    # Split pages from pdf 
    pages = loader.load_and_split()
    # Load documents into vector database aka ChromaDB
    store = Chroma.from_documents(pages, embeddings, collection_name='annualreport')

    # Create vectorstore info object - metadata repo?
    vectorstore_info = VectorStoreInfo(
        name="false_promise_llm",
        description="Understanding an LLM paper",
        vectorstore=store
    )
    # Convert the document store into a langchain toolkit
    toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

    # Add the toolkit to an end-to-end LC
    agent_executor = create_vectorstore_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )

    # Create a text input box for the user
    prompt = st.text_input('Input your prompt here')

    # If the user hits enter
    if prompt:
        # Then pass the prompt to the LLM
        response = agent_executor.run(prompt)
        # ...and write it out to the screen
        st.write(response)

        # With a streamlit expander  
        with st.expander('Document Similarity Search'):
            # Find the relevant pages
            search = store.similarity_search_with_score(prompt) 
            # Write out the first 
            st.write(search[0][0].page_content) 