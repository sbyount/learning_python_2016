def list2_dict(a_list):
    my_dict = {}
    for i, k in enumerate(a_list):
        my_dict[i] = k
    return my_dict

keys = ['key1', 'key2', 'key3']

print list2_dict(keys)
