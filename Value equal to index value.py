def valueEqualToIndex(self,arr, n):
	     a = []
         for i in range (n):
             if arr[i] == i+1:
                 a.append(arr[i])
         return a
