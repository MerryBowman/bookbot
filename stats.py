def get_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(path):
    text = get_text(path)
    words = text.split()
    return len(words)

def count_characters(path):
    chars = {}
    text = get_text(path)
    text_lower = text.lower()
    words = text_lower.split()
    for word in words:
        for letter in word:
            if letter.isalpha() == False:
                continue
            if letter in chars:
                chars[letter] += 1
            else:
                chars[letter] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(path):
    sorted_chars = []
    chars = count_characters(path)
    for char in chars:
        sorted_chars.append({"char": char, "num": chars[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars