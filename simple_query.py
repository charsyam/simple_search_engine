class SimpleQuery:
    def query(self, doc_count, tokens, terms):
        ret = []
        for t in terms:
            if t in tokens:
                ret.append((t, tokens[t]))

        return ret
