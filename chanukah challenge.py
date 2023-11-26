n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    _sum=0
    for j in range(b+1):
        _sum+=j
        
   
    print(a,_sum+b)
 