

# Query function
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
def retrieve_semantic_recommendations(query: str, k: int = 5) -> pd.DataFrame:
    load_dotenv()
    movies = pd.read_csv("../data/movies_cleaned_v2.csv")

    # Initialize or load the Chroma database
    persist_dir = "./chroma_db"
    if Path(persist_dir).exists():
        db_movies = Chroma(
            persist_directory=persist_dir,
            embedding_function=OpenAIEmbeddings()
        )
    else:
        raw_documents = TextLoader("tagged_overview.txt", encoding="utf-8").load()
        text_splitter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator="\n")  # Fixed chunk_size
        documents = text_splitter.split_documents(raw_documents)
        db_movies = Chroma.from_documents(
            documents,
            embedding=OpenAIEmbeddings(),
            persist_directory=persist_dir
        )
        db_movies.persist()
        
    recs = db_movies.similarity_search(query, k)
    movies_list = []

    for i in range(0, len(recs)):
        movies_list += [int(recs[i].page_content.strip('"').split()[0])]
    
    return movies[movies["id"].isin(movies_list)].head(k)

# Example usage
results = retrieve_semantic_recommendations("friendly delightful fun for children", k=10)
print(results)