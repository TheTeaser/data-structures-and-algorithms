from Challenge33.left_join import Hashtable, left_join
import pytest

def test_left_join():
    synonyms = Hashtable()
    synonyms.add("diligent", "employed")
    synonyms.add("fond", "enamored")
    synonyms.add("guide", "usher")
    synonyms.add("outfit", "garb")
    synonyms.add("wrath", "anger")

    antonyms = Hashtable()
    antonyms.add("diligent", "idle")
    antonyms.add("fond", "averse")
    antonyms.add("guide", "follow")
    antonyms.add("flow", "jam")
    antonyms.add("wrath", "delight")

    result = left_join(synonyms, antonyms)

    assert result == [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"]
    ]

    # Empty HashTables case:
    empty_synonyms = Hashtable()
    empty_antonyms = Hashtable()

    empty_result = left_join(empty_synonyms, empty_antonyms)
    assert empty_result == []
