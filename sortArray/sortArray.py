# Массив для примера ->

arr = [143, 4832, 11, 31, 9932]

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(f'Sort array {arr}')


