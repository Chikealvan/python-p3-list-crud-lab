def create_an_empty_list():
    return []

def create_a_list():
    return [1, "apple", True, 3.14]

def add_element_to_end_of_list(l, element):
    return l.append(element)
my_list = ["apple", "banana", "cherry"]
add_element_to_end_of_list(my_list, "orange")
print(my_list)

def add_element_to_start_of_list(l, element):
    return l.insert(0, element)
my_list = ["apple", "banana", "cherry"]
add_element_to_start_of_list([0], "orange")
print(my_list)

def remove_element_from_end_of_list(l):
    return 
    if len(l) > 0:
        l.pop()
my_list = [1, 2, 3, 4]
remove_element_from_end_of_list(my_list)
print(my_list)

def remove_element_from_start_of_list(l):
    return
    if len(l) > 0:
        del l[0]
my_list = ["apple", "banana", "cherry", "orange"]
remove_element_from_start_of_list(my_list)
print(my_list)

def retrieve_first_element_from_list(l):
    if len(l) > 0:
        return l[0]
    my_list = ["apple", "banana", "cherry", "orange"]
first_element = retrieve_first_element_from_list(my_list)
print(first_element)

def retrieve_element_from_index(l, index):
    return
    if 0 <= index < len(l):
        return l[index]
    else:
        return None  # Return None if the index is out of range
my_list = ["apple", "banana", "cherry", "orange"]
element_at_index = retrieve_element_from_index(my_list, 2)
print(element_at_index)

def retrieve_last_element_from_list(l):
    return
    if len(l) > 0:
        return l[-1]
my_list = ["apple", "banana", "cherry", "orange"]
last_element = retrieve_last_element_from_list(my_list)
print(last_element) 