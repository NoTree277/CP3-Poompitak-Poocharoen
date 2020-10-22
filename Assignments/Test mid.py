def char_index_list(s, c):
    llist = s
    same_list = []
    final = []
    a = 0
    for i in range(len(llist)):
        if llist[a] == c:
            same_list.append(llist[a])
            final.append(a)
            a += 1
        else:
            a += 1
    return f"{final}"


print(char_index_list("aabaabaacca", 'a'))
print(char_index_list("aabaabaacca", 'b'))
print(char_index_list("aabaabaacca", 'c'))
print(char_index_list("aabaabaacca", 'e'))
