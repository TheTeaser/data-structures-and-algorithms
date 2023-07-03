def repeated_word(string):
    '''
    This function finds the first repeated word in a given argument.
    '''
    words = string.lower().split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            return word
        else:
            word_count[word] = 1
    
    return None
