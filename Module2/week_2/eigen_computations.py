import numpy as np

def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def compute_cosine(v1,v2):
  result = np.dot(v1,v2)/np.linalg.norm(v1)*np.linalg.norm(v2)
  return result

if __name__ == "__main__":
    number_matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
    print(compute_eigenvalues_eigenvectors(number_matrix))
