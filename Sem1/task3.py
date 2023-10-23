def ratios_array(lst):
    pos = len(list(filter(lambda x: x > 0, lst)))
    neg = len(list(filter(lambda x: x < 0, lst)))
    zero = len(list(filter(lambda x: x == 0, lst)))

    lst_len = len(lst)
    pos_ratio = pos / lst_len
    neg_ratio = neg / lst_len
    zero_ratio = zero / lst_len

    return pos_ratio, neg_ratio, zero_ratio


init_list = [1, 2, -3, -4, 0]
print(ratios_array(init_list))
