def count_chart_s(text):
    count = {}
    strings = list(text)
    for char in strings:
        if char in count:
            count[char] = count[char] + 1
        else:
            count[char] = 1
    return count


if __name__ == "__main__":
    string = "Happiness"
    print(count_chart_s(string))