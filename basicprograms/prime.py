def prime(n: int)->bool:
    '''This is the function to check wheather 
    given number is prime of not'''
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count == 2


  # main code
  num = int(input())
  out = prime(num)
  print(out)
