def sum1(list1):
    if len(list1) != 0:
        return list1[0] + sum1(list1[1:])
    return 0


print(sum1([1, 2, 3]))


def sum2(list1):
    if len(list1) != 0:
        if type(list1[0]) != list:
            return list1[0] + sum2(list1[1:])
        else:
            return sum2(list1[0]) + sum2(list1[1:])
    return 0


print(sum2([1, 2, 3, [1, 2, 3, [1, 2, 3]]]))
