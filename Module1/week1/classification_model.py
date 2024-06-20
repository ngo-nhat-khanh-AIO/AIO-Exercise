def classification_model(num_1, num_2, num_3):
    precision = num_1/(num_1+num_2)
    recall = num_1/(num_1+num_3)
    f1_score = 2*(precision*recall)/(precision+recall)
    return precision, recall, f1_score

def test_value(num_1, num_2, num_3):
    if (isinstance(num_1,int)) and (isinstance(num_2,int)) and (isinstance(num_3,int)):
       return True
    else:
       print("fn must be int")
       return False

def test_number(num_1, num_2, num_3):
    if num_1 > 0 and num_2 > 0 and num_3 > 0:
       return True 
    else:
       print("p and fp and fn must be greater than zero")
       return False
       
def test_total_value(num_1, num_2, num_3):
   if (isinstance(num_1,int)) and (isinstance(num_2,int)) and (isinstance(num_3,int)):
      if (num_1 > 0) and (num_2 > 0) and (num_3 > 0):
         return True
      else:
         return "p and fp and fn must be greater than zero"
   else:
      return "fn must be int"

def classification_model_v1(num_1, num_2, num_3):
   if test_value(num_1,num_2,num_3) and test_number(num_1,num_2,num_3):
        precision = num_1/(num_1+num_2)
        recall = num_1/(num_1+num_3)
        f1_score = 2*(precision*recall)/(precision+recall)
        return print(f'vậy kết quả precision: {precision}, kết quả recall: {recall}, vậy kết quả f1_score: {f1_score}')
   
if __name__== "__main__":
   print(f"kết quả là: {classification_model_v1(2,4,5)}")