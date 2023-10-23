def ratios_array(lst):
    pos, neg, zero = 0, 0, 0
    for i in lst:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    lst_len = len(lst)
    pos_ratio = pos / lst_len
    neg_ratio = neg / lst_len
    zero_ratio = 1 - (pos_ratio + neg_ratio)

    return pos_ratio, neg_ratio, zero_ratio


init_list = [1, 2, -3, -4, 0]
print(ratios_array(init_list))
