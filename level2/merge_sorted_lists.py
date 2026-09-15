
def merge_sorted_lists(lists: list[list[int]]) -> list[int]:

    if not lists[0]:
        return []


    all_elem = []

    for i in lists:
        for k in i:
            all_elem.append(k)

    min_e = all_elem[0]

    for l in range(len(all_elem)):
        min_e = l
        for k in range( l +1,len(all_elem)):
            if all_elem[k] <= all_elem[min_e]:
                min_e = k
        all_elem[l], all_elem[min_e] = all_elem[min_e], all_elem[l]

    return all_elem

print(merge_sorted_lists([[10], [10], [10]]))

