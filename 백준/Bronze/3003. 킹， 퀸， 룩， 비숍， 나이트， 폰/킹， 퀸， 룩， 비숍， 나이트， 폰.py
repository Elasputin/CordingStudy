lst=list(map(int, input().split()))
chess=[1,1,2,2,2,8]
answer=[]
for i in range(len(lst)):
    cnt = chess[i] - lst[i]
    answer.append(cnt)
print(*answer)    
    
    
    
