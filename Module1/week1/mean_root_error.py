import random

def mean_abs_error(num_1, num_2, num_3):
    return (1/num_1) * abs(num_2 - num_3)

def mean_root_error(num_1, num_2, num_3):
    return (1/num_1) * (num_2 - num_3)**2

def activation_function_name_v1(names):
    if (names == "MAE") or (names == "MSE"):
        # print("hàm của bạn đã nhập đã đúng")
        return True
    else:
        print(f"hàm tính {names}, bạn nhập bị sai hãy thử lại")
        return False

def tests_isnumeric(number):
    if (isinstance(number, int)):
        print("thành công")
        return True
    else:
        print("số nhập vào phải là một số nguyên")
        return False

def use_name_root_error(number, names):
    total = 0
    if activation_function_name_v1(names) and tests_isnumeric(number):
        for _ in range(number - 1):
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)
            if names == "MAE":
                loss = mean_abs_error(number, target, predict)
                total += loss
                print(
                    f"loss name: {names}, vậy giá trị predict: {predict}, vậy giá trị target: {target}, vậy kết quả loss: {loss}")
            elif names == "MSE":
                loss = mean_root_error(number, target, predict)
                total = total + loss
                print(
                    f"loss name: {names}, vậy giá trị predict: {predict}, vậy giá trị target: {target}, vậy kết quả loss: {loss}")
            print(f"vậy tổng total: {total}")

if __name__ == "__main__":
    print(f"vậy kết quả là: {use_name_root_error(7, 'MSE')}")
