def repeated_word(string):
    words = string.lower().split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            return word
        else:
            word_count[word] = 1
    
    return None
