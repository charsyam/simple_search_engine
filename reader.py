from index_reader import IndexReader
from simple_query import SimpleQuery


if __name__ == "__main__":
    reader = IndexReader("index", SimpleQuery())
    results = reader.query(["blue", "sky"])
    for ret in results:
        print(ret)
