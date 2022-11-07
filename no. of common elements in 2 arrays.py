       l = 0
       a = set(A)
       b = set(B)
       for i in a:
           if i in b:
               l+=1
       return l
