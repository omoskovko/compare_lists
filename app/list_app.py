def compare_lists(lst1, lst2):
    res_dict = {}

    res_dict["list1"] = {"len_diff": len(lst2) - len(lst1),
                         "dif_elems": [v for v in lst2 if not v in lst1]}
    res_dict["list2"] = {"len_diff": len(lst1) - len(lst2),
                         "dif_elems": [v for v in lst1 if not v in lst2]}

    return res_dict
