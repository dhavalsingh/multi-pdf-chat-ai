import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def get_pdf_text(docs):
    text = ""
    for doc in docs:
        pdf_reader = PdfReader(doc)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def build_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator= "\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl"
    vectorstroe = FAISS.from_texts(texts=text_chunks, embedding=embeddings)

    return vectorstroe

def get_convo_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    convo_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return convo_chain

def handle_user_input(user_q):
    response = st.session_state.convo({'question': user_q})
    #st.write(response)
    st.session_state.history = response['chat_history']

    for i, msg in enumerate(st.session_state.history):
        if i % 2 == 0:
            st.write(f'<p>User: {msg.content}</p>', unsafe_allow_html=True)
        else:
            st.write(f'<p>AI: {msg.content}</p>', unsafe_allow_html=True)

def main():
    load_dotenv()
    if "convo" not in st.session_state:
        st.session_state.convo = None
    if "history" not in st.session_state:
        st.session_state.history = None
    
    st.set_page_config(page_title= "Chat with multiple PDFs", page_icon=":books:")
    st.header("Chat with mulitple PDFs :books:")
    user_q = st.text_input("Ask a question about your documents:")
    if user_q:
        handle_user_input(user_q)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                # Get raw pdf text
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text)

                # Get text chunks
                text_chunks = build_text_chunks(raw_text)
                # st.write(text_chunks)

                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # Create convo chain
                st.session_state.convo = get_convo_chain(vectorstore)

if __name__ == '__main__':
    main()