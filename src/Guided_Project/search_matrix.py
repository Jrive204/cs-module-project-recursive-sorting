matrix = [
    [1, 4, 7, 12, 15, 997, 999],
    [2, 5, 19, 32, 35, 1001, 1007],
    [4, 8, 24, 34, 36, 1008, 1015],
    [40, 41, 42, 44, 45, 1018, 1020],
    [98, 99, 101, 104, 190, 1021, 1025],
]


def search_matrix(arr, target):
    for index, element in enumerate(arr):
        # print(index, element)
        for i, e in enumerate(element):
            # print(i, e)
            if e == target:
                return [index, i]


print(search_matrix(matrix, 32))
