
def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)

def searchMatrix(matrix, target):
    for i in matrix:
        if binary_search(i, target):
            return True
        else:
            return False
    # print()

matrix = [
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3

print(searchMatrix(matrix, target))

