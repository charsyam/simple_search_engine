from index_writer import IndexWriter
from analyzer import EnglishAnalyzer


def get_fp(filename):
    return open(filename)
if __name__ == "__main__":
    indexWriter = IndexWriter("index", EnglishAnalyzer())

    fp1 = get_fp("doc1.txt")
    fp2 = get_fp("doc2.txt")
    fp3 = get_fp("doc3.txt")

    indexWriter.add_doc("doc1.txt", fp1)
    indexWriter.add_doc("doc2.txt", fp2)
    indexWriter.add_doc("doc3.txt", fp3)

    tokens = indexWriter.commit()
    for token in tokens:
        print(token)
