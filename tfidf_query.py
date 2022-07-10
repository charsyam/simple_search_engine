import math


class TFIDFQuery:
    def query(self, doc_count, tokens, terms):
        ret = []
        for t in terms:
            if t in tokens:
                ret.append((t, self._tfidf(doc_count, tokens[t])))

        return ret

    def _tfidf(self, doc_count, token):
        ret = []
        df = len(token)
        for t in token.keys():
            tf = token[t]
            idf = math.log(float(doc_count)/float(df))
            ret.append((tf*idf, t))

        return sorted(ret, key = lambda x: x[0], reverse=True)

