def filter_list(l):
    result =[]
    for i in l:
        if type(i)== str:
            continue
        else:
            result.append(i)
    return result