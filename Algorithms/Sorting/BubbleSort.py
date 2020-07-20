def bubble_sort(data):
    """
        sorts the data in order using bubble sort algorithm
        Author
        ------
        Anim Malvat
    """
    for i in range(len(data)):
        for j in range(i):
            if data[i] < data[j]:
                temp = data[j]
                data[j] = data[i]
                data[i] = temp
    return data

data = [1, 5, 2, 3, 4]
bubble_sort(data)
print(data)
