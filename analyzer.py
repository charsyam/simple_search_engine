from filters import *
import itertools


class EnglishAnalyzer:
    filter_words = [
        ('s', 1),
        ('es', 2),
        ('ed', 2),
        ('ing', 3)
    ]

    unused_words = [
        "it'",
        "it",
        "and",
        "not",
        "but",
        "the",
        "a",
        "an",
        "around",
        "over",
        "in",
        "to",
        "on",
        "from"
    ]

    def __init__(self):
        self.filters = [remove_special_character, smaller]

    def remove_unused_words(self, words):
        ret = []
        for w in words:
            if w not in self.unused_words:
                ret.append(w)

        return ret 

    def do_filters(self, w):
        target = w
        for f in self.filters:
            target = f(target)

        return target

    def tokens(self, raw, filename):
        raw_tokens = raw.split()
        filtered_tokens = self.transfer(raw_tokens)
        stemmed_tokens = self.stemming(filtered_tokens)
        final_tokens = self.remove_unused_words(stemmed_tokens)

        return [(token, {filename: 1}) for token in final_tokens]

    def transfer(self, raws):
        raw_tokens = [self.do_filters(w) for w in raws] 
        return raw_tokens

    def _stemming(self, word):
        for f in self.filter_words:
            if word.endswith(f[0]):
                idx = -1 * f[1]
                return [word[:idx]]

        return [word]

    def stemming(self, filtered_tokens):
        ret = [self._stemming(w) for w in filtered_tokens]
        return list(itertools.chain(*ret))
