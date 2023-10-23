def search(lst, targ):
    for i in lst:
        if i == targ:
            return True
    return False


init_list = [1, 2, 3, 4, 5]
target = 11
print(search(init_list, target))
