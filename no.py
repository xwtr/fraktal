
[n,k] =list(map(int,input().split()))
arr= [['.' for i in range(n**k)] for j in range (n**k)]
temp_arr= [['.' for i in range(n)] for j in range (n)]


for i in range(n):
    temp_arr[i]=list(input())


def fartkal(rs,re,cs,ce,m):
    # # m=(re-rs)//n
    if((re-rs)==0) :
        return
    if ((re-rs)//n==1):
        for i in range(n):
            for j in range(n):
                if(arr[rs+i][cs+j]=='.'):
                    arr[rs+i][cs+j] = temp_arr[i][j]
        return
    # if((re-rs)//n==0 or (re-rs)//n==1):
    #     return
    for i in range(n):
        for j in range(n):
            if temp_arr[i][j]=='*':
                for w in range(rs+i*m,rs+(i+1)*m):
                    for e in range(cs+j*m,cs+(j+1)*m):
                        arr[w][e]='*'


    for i in range(n):
        for j in range(n):
            fartkal(rs+i*m,rs+m*(i+1),cs+j*m,cs+m*(j+1),m//n)
            fartkal(rs+i*m,rs+m*(i+1),cs+j*m,cs+m*(j+1),m//n)

        # print_fartkal(n,k)
        # print(" ")


def print_fartkal(n,k):
    str=''
    for j in range(n**k):
        for i in range(n**k):
            str+=arr[j][i]
        print(str)
        str=''

fartkal(0,n**k,0,n**k,n**(k-1))
print_fartkal(n,k)

