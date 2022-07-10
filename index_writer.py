class IndexWriter:
    def __init__(self, filename, analyzer):
        self.filename = filename
        self.analyzer = analyzer
        self.tokens = {}

    def add_doc(self, filename, fp):
        raw = fp.read()
        self.tokens[filename] = self.analyzer.tokens(raw, filename) 

    def union_tokens(self):
        ret = []
        for key in self.tokens.keys():
            ret.extend(self.tokens[key])

        return ret

    def sort_tokens(self, tokens): 
        return sorted(tokens, key=lambda x : x[0])

    def combine_tokens(self, tokens):
        size = len(tokens)
        (pt, pdoc) = tokens[0]
        docs = [pdoc]
        ret = []
        for i in range(1, size):
            (t, doc) = tokens[i]

            if pt == t:
                if doc not in docs:
                    docs.append(doc)
            else:
                ret.append((pt, docs))
                pt = t
                docs = [doc]

        ret.append((pt, docs))
        return ret

    def commit(self):
        tokens = self.union_tokens()
        sorted_tokens = self.sort_tokens(tokens)
        return self.combine_tokens(sorted_tokens)

