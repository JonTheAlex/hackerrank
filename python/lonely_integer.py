def lonelyinteger(a):
    dict = {}
    for num in a:
        dict[num] = 0

    for num in a:
        dict[num] += 1

    for key, value in dict.items():
        if value == 1:
            return key

print(lonelyinteger([1,2,3,4,3,2,1]))
