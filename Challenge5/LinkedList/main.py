from linked_list import LinkedList

my_list = LinkedList()

my_list.insert(1)
my_list.insert(2)
my_list.insert(3)

# New methods tests:
my_list.append(5)
my_list.insert_before(5,4)
my_list.insert_after(5,6)
my_list.delete(1)
#

print(my_list)
print(my_list.includes(2))
print(my_list.includes(1))
print(my_list.kthFromEnd(0))
print(my_list.middle_Value())
