# def array_rotation_detector(arr1: list, arr2:list)-> bool:
#     count = 1
#     if not arr1 and  not arr2:
#         return True
#     arr2_D = arr2 + arr2
#     for i in arr1:
#         if i in arr2_D:
#             idx = arr2_D.index(i)
#             if ( (idx  < len(arr2_D))) and  (i+1 == arr2_D[idx + 1]):
#                 count +=1
            
#     if count == len(arr1):
#         return True
#     else:
#         return False
        
def array_rotation_detector(arr1: list, arr2:list)-> bool:
    if len(arr1) != len(arr2):
        return False
    arr2_d = arr2 + arr2

    for i in range(len(arr2_d)):
        if arr2_d[i:i+len(arr1)] ==arr1:
            return True
    return False


print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))