def num_list_v(number, kerner):
    n = len(number)
    result = []
    for i in range(n - kerner + 1):
        max_value = 0
        for j in range(i + kerner):
            if number[j] > max_value:
                max_value = number[j]
        result.append(max_value)
    return result


if __name__ == "__main__":
    file_path = "/content/P1_data.txt"
    
