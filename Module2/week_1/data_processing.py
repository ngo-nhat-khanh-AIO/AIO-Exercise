import pandas as pd
import numpy as np
df = pd.read_csv("/content/advertising.csv")

data = df.to_numpy()

data_1 = data[::, 3]
data_2 = np.average(data[::, 0])

# Tạo một DataFrame ví dụ
df = pd.DataFrame({'Sales': [100, 200, 300, 150, 250]})

# Tìm chỉ mục của giá trị lớn nhất trong cột 'Sales'
max_index = df['Sales'].idxmax()

# Lấy giá trị lớn nhất trong cột 'Sales'
max_value = df['Sales'][max_index]

if __name__ == "__main__":
    print(data_2)
    print("Chỉ mục của giá trị lớn nhất:", max_index)
    print("Giá trị lớn nhất:", max_value)
   
