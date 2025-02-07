# Convert raw text so that langchain can interpret it
from langchain_community.document_loaders import TextLoader
# Split movie dataset into movie overviews
from langchain_text_splitters import CharacterTextSplitter
# Convert chunks into embeddings to use with OpenAI API calls
from langchain_openai import OpenAIEmbeddings
# Chroma is vector database to store AI results
from langchain_chroma import Chroma

from dotenv import load_dotenv

import pandas as pd


load_dotenv()
# movies = pd.read_csv("../data/movies_cleaned_v2.csv")

# print(movies.info())
# print(movies["tagged_overview"])

# Vector database has overview summaries of the movies. That is how it will query. It will be quicker

# Save the movie ID and movie summary dataframe to text file for Langchain
# def save_df_txtfile ():
#     movies["tagged_overview"].to_csv("tagged_overview.txt", sep="\n", index=False, header=False)

# save_df_txtfile()

dataset = "../id_name.csv"
df = pd.read_csv(dataset)

raw_documents = TextLoader("tagged_overview.txt", encoding="utf-8").load()
text_splitter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator="\n")
documents = text_splitter.split_documents(raw_documents)

print(documents[0])

db_movies = Chroma.from_documents(
    documents, 
    embedding=OpenAIEmbeddings()
)


query = "movies like the stormlight archive book series"

docs = db_movies.similarity_search(query, k=10)

# Display the results
for doc in docs:
    print(f"Document: {doc.page_content}")

def process_document(doc):
    doc_string = str(doc.page_content)
    content = doc_string.replace("Document: ", "")
    movie_id, description = content.split(" ", 1)
    return int(movie_id), description

for doc in docs:
    id, desc = process_document(doc)
    name = df[df['id'] == id]['title'].values[0]
    print(f"Movie ID: {id}, Name: {name}, Description: {desc}")