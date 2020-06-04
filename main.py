def alphabetically_ordered_list(some_list):
    new_list = some_list.split(",")
    new_list.sort()
    return new_list

print(alphabetically_ordered_list("b, w, r, bt, g"))