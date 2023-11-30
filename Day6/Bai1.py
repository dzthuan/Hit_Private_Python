def indexOfMultiply(*idx):
    """ truyen tuple unpacking  
    """
    result = 1.0
    for i in idx:
        result *= i
    return result

result1 = indexOfMultiply(1, 2, 3, 4)
print(result1)

result2 = indexOfMultiply(1.2, 5, 5)
print(result2)