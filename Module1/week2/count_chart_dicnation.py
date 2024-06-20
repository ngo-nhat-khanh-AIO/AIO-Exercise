def count_chart_dicnation(text):
    count = {}
    strings = text.split()
    for char in strings:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
    count_chart_dicnation(num_list)
