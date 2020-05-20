from collections import defaultdict


def filter_list(l):
    d = defaultdict(list)
    for i in l:
        d[type(i)].append(i)
    return d[int]

    #return [x for x in l if type(x) is not str]

    #return [i for i in l if not isinstance(i, str)]


print(filter_list([1,2,'a','b', 3, 4, 5, 's']))