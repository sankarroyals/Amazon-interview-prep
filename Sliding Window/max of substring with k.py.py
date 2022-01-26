import collections
k=3
a=[1,2,3,4,5]
ouput=[]
# for i in range(len(a)-(k-1)):
#     maxi=a[0]                                                  // WORST CASE          O(k*(n-m))
#     for j in range(1,k):
#         if(a[i+j]>maxi):
#             maxi=a[i+j]
#     ouput.append(maxi)


q=collections.deque()
l=r=0
while r<len(a):
    while q and a[r]>a[q[-1]]:
        q.pop()
    q.append(r)
    if(l>q[0]):                                              # BEST CASE               O(n)
        q.popleft()
    
    if(r+1)>=k:
        ouput.append(a[q[0]])
        l+=1
    r+=1
print(ouput)   


        
