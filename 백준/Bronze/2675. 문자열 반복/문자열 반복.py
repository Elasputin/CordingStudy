N=int(input())
for i in range(N):
    answer=''
    ipruk= list(input().split()) 
    cnt=int(ipruk[0])
    words=ipruk[1]
    for c in words:
        answer+= c * cnt
    print(answer)
        