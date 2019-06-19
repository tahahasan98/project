#Working with 2-dimensional arrays


def arr1():
    # Define array values as A
    a = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
    for row in a:
        # add for loop to stop at the end of each array
        for col in range(len(row)):
            # locate if their is a 12 in each array
            if (row[col]) == 12:
                # change each 12 to 77
                (row[col]) = 77
    print(a)
# call the function
arr1()


def arr2():
    v = 0
    a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    for row in a:
        v = a[0] + a[1] + a[2]
        v1 = sum(v)
    print(v1)
    print(v)

arr2()


def arr3():
    a = [[1, 0 , 0 , 0], [2, 1, 0, 0], [2, 2, 1, 0], [2, 2, 2, 1]]
    n = {}

    for row in a:
        for col in range(len(row)):
            index = row[col]
            if index not in n:
                n.update({index: 1})
            else:
                count = n[index] + 1
                n.update({index: count})

    for i in n:
        print(i, "occurs", n[i], "times")

arr3()