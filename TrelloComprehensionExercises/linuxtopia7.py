

def median(data):
    data.sort()
    print(repr(data))
    if len(data) % 2 == 1:
        return data[int(len(data)+1)/2]
    else:
        return (data[int(len(data)/2)] + data[int(len(data)/2-1)])/2

data = [1, 2, 5, 2, 2, 5, 2, 4, 5, 4, 2, 2, 2, 5, 2, 2, 3, 3, 4, 5]
print("Median: ", median(data))
