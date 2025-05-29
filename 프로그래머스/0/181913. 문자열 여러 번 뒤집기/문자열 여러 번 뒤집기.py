def solution(my_string, queries):
    my_list = list(my_string)
    for s, e in queries:
        while s < e:
            my_list[s], my_list[e] = my_list[e], my_list[s]
            s += 1
            e -= 1
    return ''.join(my_list)