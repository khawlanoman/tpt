from typing import List
def list_intersection_finder(lists: List[List[int]]) -> List[int]:

    result = []
    for  i in lists[0]:
        if all(i in list for list in lists ) and i not in result:
            result.append(i)
    return result

print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
