import pytest
from stack_queue_brackets import brackets_validater

def test_brackets_validater():
    
    assert brackets_validater("") == True
    assert brackets_validater("()") == True
    assert brackets_validater("[]") == True
    assert brackets_validater("{}") == True
    assert brackets_validater("()[]{}") == True
    assert brackets_validater("[{()}]") == True
    assert brackets_validater("(") == False
    assert brackets_validater(")") == False
    assert brackets_validater("(()") == False
    assert brackets_validater("([)]") == False
    assert brackets_validater("{{}") == False
    assert brackets_validater("[") == False
    assert brackets_validater("]") == False
    assert brackets_validater("[}") == False
    assert brackets_validater("(]") == False
