class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head=node
        else:
            node.next = self.head
            self.head = node

    def includes(self, key):
        temp = self.head
        while (temp):
            if temp.value == key:
                return True
            else:
                temp = temp.next
        return False
    
    def __repr__(self):

        output = ""

        if self.head is None:
            output = "Empty Linked List."
        else:
            current = self.head
            while (current):
                output += f'{current.value} ---> '
                current = current.next

            output += "Null"
        return output

# Code Challenge #6 starts from here, added append(), insert_before() & insert_after()

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def insert_before(self, t_value, n_value):
        node = Node(n_value)
        node.next = self.head
        if self.head is None:
            raise ValueError(
                'Error! The current list is empty, add some data first using insert()')
        elif self.head.value == t_value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next != None:
                if current.next.value == t_value:
                    node.next = current.next
                    current.next = node
                    return
                current = current.next
            raise ValueError(
                'Error! Make sure the T_value is present in the list, you can use include() to check if a value is available or not.')

    def insert_after(self, t_value, n_value):
        node = Node(n_value)
        if self.head is None:
            raise ValueError(
                'Error! The current list is empty, add some data first using insert()')
        else:
            current = self.head
            while current is not None:
                if current.value == t_value:
                    node.next = current.next
                    current.next = node
                    return
                current = current.next
            raise ValueError(
                'Error! Make sure the T_value is present in the list, you can use include() to check if a value is available or not.')

# Stretch Goal (delete());

    def delete(self, t_value):
        if self.head is None:
            raise ValueError("Error! Cannot delete from an empty list add some data first using isert()")
        elif self.head.value == t_value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next != None:
                if current.next.value == t_value:
                    current.next = current.next.next
                    return
                current = current.next
            raise ValueError('Error! Make sure the T_value is present in the list, you can use include() to check if a value is available or not.')
    
