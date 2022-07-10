from index_reader import IndexReader
from tfidf_query import TFIDFQuery


if __name__ == "__main__":
    reader = IndexReader("index", TFIDFQuery())
    results = reader.query(["blue", "sky"])
    for ret in results:
        print(ret)
