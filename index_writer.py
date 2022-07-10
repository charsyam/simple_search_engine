import os.path
from os import path
import json


class IndexWriter:
    def __init__(self, indexname, analyzer):
        self.indexname = indexname 
        self.analyzer = analyzer
        self.tokens = {}
        self.doc_count = 0

    def add_doc(self, filename, fp):
        raw = fp.read()
        self.tokens[filename] = self.analyzer.tokens(raw, filename) 
        self.doc_count += 1

    def union_tokens(self, tokens):
        ret = []
        for key in self.tokens.keys():
            ret.extend(self.tokens[key])

        ret.extend(tokens)
        return ret

    def sort_tokens(self, tokens): 
        return sorted(tokens, key=lambda x : x[0])

    def update_docs(self, doclist1, doclist2):
        ret = []
        ret.extend(doclist1)

        for d2 in doclist2:
            if d2 not in ret:
                ret.append(d2)

        return ret

                
    def combine_tokens(self, tokens):
        size = len(tokens)
        (pt, pdocs) = tokens[0]
        docs = pdocs
        ret = []
        for i in range(1, size):
            (t, idocs) = tokens[i]

            if pt == t:
                docs = self.update_docs(docs, idocs)
            else:
                ret.append((pt, docs))
                pt = t
                docs = idocs

        ret.append((pt, docs))
        return ret

    def load_index(self, indexname):
        existed = os.path.isfile(indexname)
        doc_count = 0
        tokens = []
        if existed:
            fp = open(self.indexname)
            data = fp.read()
            v = json.loads(data)
            doc_count = v["doc_count"]
            tokens = v["tokens"]
            fp.close() 

        return (doc_count, tokens)
        
    def commit(self):
        (old_doc_count, old_tokens) = self.load_index(self.indexname)
        tokens = self.union_tokens(old_tokens)
        sorted_tokens = self.sort_tokens(tokens)
        combined_tokens = self.combine_tokens(sorted_tokens)
        self.store(old_doc_count, combined_tokens)

        return combined_tokens

    def store(self, old_doc_count, tokens):
        existed = os.path.isfile(self.indexname)
        total_count = old_doc_count + self.doc_count

        v = {"doc_count": total_count, "tokens": tokens}
        fp = open(self.indexname, "w")
        fp.write(json.dumps(v))
        fp.close()
