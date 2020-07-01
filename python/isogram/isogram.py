def is_isogram(string):
    encountered = set()
    for char in string.lower():
        if char in encountered:
            return False
        if char.isalpha():
            encountered.add(char)
    return True
