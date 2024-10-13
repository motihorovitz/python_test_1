def list_o(s):
    if len(s) % 3 != 0:
        return False
    part_size = len(s) // 3
    first = s[0:part_size]
    middle = s[part_size: part_size * 2]
    last = s[part_size * 2 :]
    if first != middle !=last:
        return False
    return True

s = [1,2,3,1,2,4,1,2,3]
print(list_o(s))