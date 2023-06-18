def fun(a, b):
    res = 0
    for x, y in zip(a, b):
        if x != y:
            break
        res += 1
    return res
print(fun("два", "два")