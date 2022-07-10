import os.path
from os import path
import json


class IndexReader:
    def __init__(self, indexname, query_handler):
        self.indexname = indexname
        self.doc_count = 0
        self.tokens = None
        self.query_handler = query_handler
        self.load()

    def load(self):
        existed = os.path.isfile(self.indexname)
        if existed == False:
            raise Exception("No Index File: ", self.indexname) 

        fp = open(self.indexname)
        data = fp.read()
        v = json.loads(data) 
        self.doc_count = v["doc_count"]
        tokens = v["tokens"]
        self.tokens = {}
        for token in tokens:
            self.tokens[token[0]] = token[1]

    def query(self, terms):
        return self.query_handler.query(self.doc_count, self.tokens, terms)
