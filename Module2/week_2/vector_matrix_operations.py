import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(vector**2))
    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = vector1@vector2
    return result


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    len_of_vector = matrix1@matrix2
    return len_of_vector

def inverse_matrix ( matrix):
  result = np.linalg.inv(matrix)
  return result

if __name__ == "__main__":
    number_matrix_1 = np.array([[3, 4], [2, 5]])
    print(compute_vector_length(number_matrix_1))
