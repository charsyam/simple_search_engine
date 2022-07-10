import re


def remove_special_character(word):
    return re.sub(r'[?|$|.|,|`|!]',r'',word)

def smaller(word):
    return word.lower()
