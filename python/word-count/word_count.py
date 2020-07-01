import re
from collections import Counter

def count_words(sentence):
    words = re.findall(r"(?!\')[a-z\d\']+(?<!\')", sentence.lower())
    return dict(Counter(words))
