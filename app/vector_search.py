from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma

loader = DirectoryLoader('./wiki/', glob="**/*.txt")
docs = loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
emb = GPT4AllEmbeddings()

documents = text_splitter.split_documents(documents=docs)
db = Chroma.from_documents(documents, emb)

# does not work with docker
# query = input("Enter your query (default: What is the purpose of reinforcement learning?): ") or "What is the purpose of reinforcement learning?"
query = "What is the purpose of reinforcement learning?"
print("Query:", query)
k = 2
docs = db.similarity_search_with_score(query, 5)
for doc, score in docs:
	print("Page Content:", doc.page_content)
	print("Source:", doc.metadata['source'])
	print("Score:", score)
	print("=====================================")