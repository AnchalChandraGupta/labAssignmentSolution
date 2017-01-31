
a = [1, 2, 5, 5, 2, 4, 5, 4, 2, 2, 2, 5, 2, 2, 3, 3, 4, 5]

def mode(a):
    """put each element as key and its number of occurrences as
             value in a dictionary fqDict and return
             key vaalue pair which has max value"""

    fqDict = {}
    for v in a:
        if fqDict.get(v):
            fqDict[v] = fqDict.get(v)+1
        else:
            fqDict[v] = 1

    maxFq = 0
    elem = -1
    for v in fqDict.keys():
        if fqDict.get(v) > maxFq:
            maxFq = fqDict.get(v)
            elem = v
    return (elem, maxFq)

t = mode(a)
print("Mode: ", t[0])
print("Frequency: ", t[1])
