'''li=list(map(int,input().split()))
d={}
for i in li:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)'''

#Find distinct ele in array without set 
'''nums=list(map(int,input().split()))
l=[]
for i in nums:
    if i not in l:
        l.append(i)
    l.sort()
print(l)
'''

#find element with max freq if 2 elements have same freq then print both
'''from collections import Counter
nums=list(map(int,input().split()))
freq=Counter(nums)
max_freq = max(freq,key=freq.get)
for ele, f in freq.items():
    if f == max_freq:
        print(ele, end=" ")
'''

