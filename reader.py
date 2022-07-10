from index_reader import IndexReader


if __name__ == "__main__":
    reader = IndexReader("index")
    results = reader.query(["blue", "sky"])
    for ret in results:
        print(ret)
