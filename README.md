# Chat with Multiple PDFs

This Streamlit application allows users to interact with a conversational AI model that can reference and retrieve information from multiple uploaded PDF documents. It's an ideal tool for quickly querying content from a set of documents using natural language.

## Features

- **Multiple PDF Uploads**: Users can upload several PDF documents, which the app will process and use as a reference for answering queries.
- **Conversational AI**: Leveraging a conversational AI model, the app provides responses based on the content of the uploaded PDFs.
- **Streamlit Interface**: A user-friendly interface created with Streamlit, allowing for easy interaction and usage.

## How It Works

1. **Upload PDFs**: Users upload their PDF documents through the Streamlit sidebar.
2. **Process PDFs**: The application processes the uploaded PDFs to extract text and prepare it for the AI model.
3. **Ask Questions**: Users can ask questions in a text input field. The AI model references the processed PDF texts to answer these questions.
4. **View Conversation History**: The application displays the conversation history between the user and the AI.

## Installation

To run this app, you need Python and several dependencies installed.

1. Clone this repository: git clone https://github.com/yourusername/your-repo-name.git


2. Navigate to the cloned directory and install the required packages:

cd your-repo-name
pip install -r requirements.txt

3. Run the Streamlit application:

`streamlit run app.py`


## Dependencies

- Streamlit
- PyPDF2
- dotenv
- LangChain
- FAISS
- OpenAI

## Usage

After starting the app:

1. Upload PDF files by clicking on the 'Upload your PDFs here' button in the sidebar.
2. Click 'Process' to start processing the uploaded files.
3. Enter your query in the 'Ask a question about your documents' input field.
4. The AI response will be displayed on the main screen.

## Contributing

Contributions to improve this application are welcome. Please feel free to fork the repository and submit pull requests.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contact

For any queries or feedback, please reach out to dhavalsingh19@gmail.com.
