# PDF reader using Langchain, OpneAI and Chromadb

You can upload a pdf document and ask questions. 

# Startup 🚀
1. Create a virtual environment `python -m venv langchain`
2. Activate it: 
   - Windows:`.\langchain\Scripts\activate`
   - Mac: `source langchain/bin/activate`
3. Clone this repo `git clone https://github.com/nicknochnack/LangchainDocuments`
4. Go into the directory `cd LangchainDocuments`
5. Install the required dependencies `pip install -r requirements.txt` . Note: For macos, currently python3.11 (from homebrew) is the only one that worked for me to install chromadb and hnswlib. 
6. Add your OpenAI APIKey in `.env` file and execute the command `source .env`
7. Start the app `streamlit run app.py`  

# References 🔗
<p>The main LG Agent used:<a href="https://python.langchain.com/en/latest/modules/agents/toolkits/examples/vectorstore.html">Langchain VectorStore Agents
</a></p>
<p>
OpenAI https://chat.openai.com/
</p>

# AuthorShip
👨🏾‍💻 Author: Abdullah Khan Zehady <br />
📜 License: This project is licensed under the MIT License </br>

## Original Idea derived from this tutorial 📺
   https://youtu.be/u8vQyTzNGVY
   Thanks Nicholas Renotte


