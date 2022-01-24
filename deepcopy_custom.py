def deepcopy(to_convert: dict):
    copied_list = {}
    for key,value in to_convert.items():
        copied_list[key] = value
    return copied_list

lst = {
    1: 'one',
    2: "two",
    3: 'three'
}

print(id(lst), lst)
print(id(deepcopy(lst)), deepcopy(lst))

deep_copy = deepcopy(lst)
deep_copy[3] = 'four'
print(id(lst), lst)
print(id(deep_copy), deep_copy)
