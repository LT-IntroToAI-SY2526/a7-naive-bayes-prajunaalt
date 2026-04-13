import wikipedia
import re, time
from typing import List

def tokenize(text: str) -> List[str]:
    """Splits given text into a list of the individual tokens in order

    Args:
        text - text to tokenize

    Returns:
        tokens of given text in order
    """
    tokens = []
    token = ""
    for c in text:
        if (
            re.match("[a-zA-Z0-9]", str(c)) != None
            or c == "'"
            or c == "_"
            or c == "-"
        ):
            token += c
        else:
            if token != "":
                tokens.append(token.lower())
                token = ""

    if token != "":
        tokens.append(token.lower())
    return tokens

article = wikipedia.page("Artemis II", auto_suggest=False).content
# print(article)
words = tokenize(article)

with open("sorted_stoplist.txt", "r", encoding="utf8") as f:
    stoplist=f.read()
    

freqs = {}

for word in words:
    if word in freqs:
        freqs[word] += 1
    else:
        freqs[word] = 1

print(freqs)

total_unique_words = len(freqs)
print(f'unique words:' + total_unique_words)
total_words = sum(freqs)
print(f'total words' + total_words)

top_words = sorted(freqs.items, key = lambda x:x[1] reverse=True)
print(top_words[0:20])