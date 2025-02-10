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
movies = pd.read_csv("../data/movies_cleaned_v2.csv")

# print(movies.info())
# print(movies["tagged_overview"])

# Vector database has overview summaries of the movies. That is how it will query. It will be quicker

# Save the movie ID and movie summary dataframe to text file for Langchain
# def save_df_txtfile ():
#     movies["tagged_overview"].to_csv("tagged_overview.txt", sep="\n", index=False, header=False)

# save_df_txtfile()

raw_documents = TextLoader("tagged_overview.txt", encoding="utf-8").load()
text_splitter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator="\n")
documents = text_splitter.split_documents(raw_documents)

# print(documents[0])

db_movies = Chroma.from_documents(
    documents, 
    embedding=OpenAIEmbeddings()
)


query = "monster movies"

docs = db_movies.similarity_search(query, k=10)
print(docs)

movies[movies["uniqueID"] == int(docs[0].page_content.split()[0].strip())]

print(movies["uniqueID"])