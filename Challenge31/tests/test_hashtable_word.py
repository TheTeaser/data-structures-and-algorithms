from Challenge31.hashtable_word import repeated_word
import pytest

def test_repeated_word():
    assert repeated_word("Once upon a time, there was a brave princess who...") == "a"
    assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom") == "it"
    
