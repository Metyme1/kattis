n = int(input())
m = int(input())
i =0

for i in range(m):
    st=""
    s,k = list(map(str,input().split()))
    k = int(k)
    if k < n:
        st= s+" lokud"
        print(st)
    else:
        st =s+" opin"
        print(st)
    