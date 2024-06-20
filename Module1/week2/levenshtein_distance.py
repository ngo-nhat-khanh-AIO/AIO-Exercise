def levenshtein(token1, token2):
    # Initialize a 2D array to store distances
    distances = [[0]*(len(token2)+1) for i in range(len(token1)+1)]

    # Fill the first row and first column of the matrix
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    # Variables to store costs of different operations
    a = 0
    b = 0
    c = 0

    # Fill the rest of the matrix
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1-1] == token2[t2-1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                # Select the minimum cost and add one for the current operation
                if a <= b and a <= c:
                    distances[t1][t2] = a + 1
                elif b <= a and b <= c:
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    istances(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]


def istances(distances, token_1, token_2):

    for t1 in range(token_1 + 1):
        for t2 in range(token_2 + 1):
            print(int(distances[t1][t2]), end=" ")
        print()


if __name__ == "__main__":
    token1 = input("Enter the first token: ")
    token2 = input("Enter the second token: ")
    distance = levenshtein(token1, token2)
    print(
        f"The Levenshtein distance between '{token1}' and '{token2}' is {distance}")
