

def uniue_in_sequence(a):
    """put each element as key and its number of occurrences as
            value in a dictionary fqDict and return all the keys which has value 1"""
    fqDict = {}
    for v in a:
        if fqDict.get(v):
            fqDict[v] = fqDict.get(v)+1
        else:
            fqDict[v] = 1

    result = []
    for v in fqDict.keys():
        if fqDict.get(v) ==1:
            result.append(v)
    return result

a = [1, 2, 5, 5, 2, 5, 2, 2, 2, 5, 2, 2, 3, 3, 4, 5]

print("Unique in sequence: ", uniue_in_sequence(a))
