import math
def sigmoid(number):
   return 1 / (1 + math.exp(-number))

def relu(number):
   if number < 0:
      return 0
   return number

def elu(number):
   alpha = 0.01
   if number <= 0:
      return alpha*(math.exp(number)-1)
   return number

def is_number(number):
   try:
      float(number)
      return True
   except ValueError:
      print("cái này không phải là số")
      return False
   return True

def activation_function_name(name_1):
   if (name_1 == "sigmoid") or (name_1 == "relu") or (name_1 == "elu"):
      print("hàm của bạn đã nhập đã đúng")
      return True
   else:
      print(f"{name_1} hàm của bạn đã nhập sai")
      return False

def user_activation_function(number,name_1):
   if is_number(number) and activation_function_name(name_1):
      if name_1 == "sigmoid":
         return sigmoid(number)
      elif name_1 == "relu":
         return relu(number)
      elif name_1 == "elu":
         return elu(number)
      
if __name__ == "__main__":
    print(f"vậy kết quả là: {user_activation_function(-1, 'elu')}")

