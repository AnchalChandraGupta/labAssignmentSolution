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

def add(x,y):
    return x + y

def square(x):
    return x ** 2

l = [1, 2, 3, 4, 5]

print("standard deviation: ", reduce(add, map(square,l)) / reduce(add, l))


mean = reduce(add, l)/len(l)

def variance(x, m):
    return (x - m) ** 2

def reduce_variance(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    mean = reduce(add, l) / len(l)
    for x in it:
        accum_value = function(x, mean)
    return accum_value

print("Total Variance: ", reduce_variance(variance, l))
print("Average Variance: ", reduce_variance(variance, l)/ (len(l)-1))
