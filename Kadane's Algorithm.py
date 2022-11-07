def maxSubArraySum(self,arr,N):
        ##Your code here
        a=arr[0]
        b=arr[0]
        for i in range(1,N):
            if a>0:
                a+=arr[i]
            else:
                a=arr[i]
            if a>b:
                b=a
        return b
