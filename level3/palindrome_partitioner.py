def palindrome_partitioner(s: str) -> int:
    flag = 0
    new_list = s[::-1]

    if new_list == s or  not s:
        flag = 1
    else:
        flag = 0
    
    count_par = 0
    list_par = []
    if flag == 1 :
        return  0 
    else:
        sub = ""
        count_par = 0
        for i in s:
            sub += i
            if sub == sub[::-1]:
                count_par += 1
                list_par.append(count_par)
        print(sub, sub[::-1])
        min_lt  = min(list_par)
        return min_lt

print(palindrome_partitioner("abc"))