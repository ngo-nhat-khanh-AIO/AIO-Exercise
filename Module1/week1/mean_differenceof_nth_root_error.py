def mean_differenceof_nth_root_error(y, y_hat, n, p):
   tast = y ** (1/n)
   predict = y_hat **(1/n)
   signal = tast - predict
   error = (signal)**p
   return error

if __name__ =="__main__":
   task_mess = mean_differenceof_nth_root_error( y =100 , y_hat =99.5 , n =2 , p =1)
   print(task_mess)