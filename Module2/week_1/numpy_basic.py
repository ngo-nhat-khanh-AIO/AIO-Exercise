import numpy as np

arr = np.arange(0, 10, 1)

arr_1 = np.full((3, 3), fill_value=True, dtype=bool)

arr_2 = np.arange(0, 10)

arr_3 = np . arange(0, 10)
arr_3[arr_3 % 2 == 1] = -1

arr_4 = np . arange(0, 10)
arr_4[arr_4 % 2 == 1] = -1

arr_5 = np.arange(10)
arr_2d = arr_5.reshape(2, -1)

arr1 = np.arange(10) . reshape(2, -1)
arr2 = np.repeat(1, 10) . reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=0)

arr = np.array([1, 2, 3])

a = np . array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5) & (a <= 10))

def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


num_1 = np.array([5, 7, 9, 8, 6, 4, 5])
num_2 = np.array([6, 3, 4, 8, 9, 7, 1])

if __name__ == "__main__":
    print(arr)
    print(type(arr_1))
    print(arr_3[arr_3 % 2 == 1])
    print(arr_4)
    print(arr_2d)
    print(" Result : \n", c)
    print(np.repeat(arr, 3))
    print(np.tile(arr, 3))
    print(" result ", a[index])

    pair_max = np.vectorize(maxx, otypes=[float])
    print(pair_max(num_1, num_2))
    print(" Result ", np . where(a < b, b, a))
