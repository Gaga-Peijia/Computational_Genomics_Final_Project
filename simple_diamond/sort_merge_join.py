def sort_merge_join_dicts(dict1, dict2, shape):
    """
    Perform a sort-merge join between two dictionaries.
    The keys of the dictionaries are considered as the join keys.

    :param dict1: The first dictionary.
    :param dict2: The second dictionary.
    :return: A dictionary with joined keys and values as tuples.
    """

    # Convert the dictionaries to sorted lists of tuples
    sorted_list1 = sorted(dict1.items())
    sorted_list2 = sorted(dict2.items())

    # Initialize pointers for both lists
    i, j = 0, 0
    result = {}

    # Merge and join
    while i < len(sorted_list1) and j < len(sorted_list2):
        #mask
        match = True
        for l in range(len(shape)):
            if shape[l]=='1' and sorted_list1[i][0][l]!=sorted_list2[j][0][l]:
                match = False
                break
        if match==True:
            # Join matching elements
            result[sorted_list1[i][0]] = (sorted_list1[i][1], sorted_list2[j][1])
            i += 1
            j += 1
        elif sorted_list1[i][0] < sorted_list2[j][0]:
            i += 1
        else:
            j += 1

    return result