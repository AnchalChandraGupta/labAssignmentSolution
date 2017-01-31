def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

def max(x,y):
    if x>=y:
        return x
    return y

def min(x,y):
    if x<=y:
        return x
    return y

l = [1, 2, 3, 4, 5]

print("max: ", reduce(max, l))
print("min: ", reduce(min, l))