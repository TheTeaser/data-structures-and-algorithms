from Stack import Stack

def brackets_validater(string):
    """
    A function that validates the brackets in a string.
    """

    stack = Stack()
    starting_brackets = ["(", "[", "{"]
    ending_brackets = [")", "]", "}"]

    for char in string:
        if char in starting_brackets:
            stack.push(char)
        elif char in ending_brackets:
            if stack.is_empty():
                return False
            opening_bracket = stack.pop()
            if starting_brackets.index(opening_bracket) != ending_brackets.index(char):
                return False

    return stack.is_empty()
