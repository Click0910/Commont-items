list_1 = ['a', 'b', 'c', 'x']
list_2 = ['z', 'y', 'c']

# Naive
def common_items(list_1, list_2):
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_2[j] == list_1[i]:
                return True
            else:
                return False


is_match = common_items(list_1, list_2)
print(is_match)


# Better
def common_items_3(items_1, items_2):
    for i in items_2:
        if i in items_1:
            return True
        else:
            return False


is_match = common_items_3(list_1, list_2)
print(is_match)

# Optimize just in python

list(set(list_1).intersection(list_2))



