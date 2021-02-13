def recursion(num):
    if num>0:
      result = num + recursion(num-1)
      print(result)
    else:
       result = 0
    return result

(recursion(6))
