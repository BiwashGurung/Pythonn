def even_position():
    arr = [43, 23, 21, 44, 56, 75]

    arr1 = []

    for i in range(1, len(arr), 2):
        arr1.append(arr[i])

    print(arr1)

if __name__ == "__main__":
    even_position()
