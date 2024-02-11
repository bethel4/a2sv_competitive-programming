    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        num = set()
        for i in b:
            num.add(i)
        for i in a:
            num.add(i)
        #code here

        return len(num)
