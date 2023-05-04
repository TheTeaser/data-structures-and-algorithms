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
            self.head = node
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
            raise ValueError(
                "Error! Cannot delete from an empty list add some data first using insert()")
        elif self.head.value == t_value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next != None:
                if current.next.value == t_value:
                    current.next = current.next.next
                    return
                current = current.next
            raise ValueError(
                'Error! Make sure the T_value is present in the list, you can use include() to check if a value is available or not.')

 # Challanege 7 (kth):

    def kthFromEnd(self, k):
        if self.head is None:
            raise ValueError(
                "Error! Current list is empty, add some data first using insert(). ")

        # Count the length of the list first to run the cAses of k's values:
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next

        if k >= length:
            raise ValueError(
                "Error! You have inserted an index bigger than or equal to the list's whole length, please try again.")
        elif k < 0:
            raise ValueError("Error! You can't insert a negative index.")

        # Iterate the list to the kth node from the end:
        current = self.head
        for i in range(length - k ):
            current = current.next

        return current.value
    
    #Challenge 7 stretch goal (Middle_Value()):

    def middle_Value(self):
        if self.head is None:
            raise ValueError(
                "Error! Current list is empty, add some data first using insert(). ")

        # Count the length of the list first to run the cAses of k's values:
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        middle_index = (length - 1) // 2
        # Iterate the list to the middle element and return its value:
        current = self.head
        for i in range(middle_index):
            current = current.next

        return current.value

    #Challenge 8 LinkedList Zip:

    def zipLists(list1, list2):

        current1 = list1.head
        current2 = list2.head
        nList=LinkedList()
        while True:
            if current1 :
                nList.append(current1.value)
                current1=current1.next
            if current2:
                nList.append(current2.value)
                current2=current2.next

            if not current1 and not current2:
                break

        return nList
    
    #Challenge 9 Reverse a LinkedList:

    def reverse_LinkedList(self):
        
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev= current
            current = next
        self.head = prev
        return self.head
