from Challenge30.hash_table import HashTable
import pytest

@pytest.fixture
def hash_table():
    return HashTable()

def test_set_and_get(hash_table):
    hash_table.add("key1", "value1")
    assert hash_table.get("key1") == "value1"

def test_replace_value(hash_table):
    hash_table.add("key1", "value1")
    hash_table.add("key1", "new_value")
    assert hash_table.get("key1") == "new_value"

def test_get_non_existing_key(hash_table):
    assert hash_table.get("key2") is None

def test_contains(hash_table):
    hash_table.add("key1", "value1")
    assert hash_table.contains("key1") is True
    assert hash_table.contains("key2") is False

def test_delete(hash_table):
    hash_table.add("key1", "value1")
    hash_table.delete("key1")
    assert hash_table.get("key1") is None

def test_collision_handling(hash_table):
    hash_table.add("key1", "value1")
    hash_table.add("key11", "value11")
    assert hash_table.get("key1") == "value1"
    assert hash_table.get("key11") == "value11"

def test_hash():
    hash_table = HashTable()
    assert hash_table.get_hash("key1") == hash_table.get_hash("key1")

