#평균
n= int(input())
grades=list(map(int,input().split()))
mxg=max(grades) # 최대값
for i in range(len(grades)):
    grades[i] = grades[i]/mxg*100

new_mean=sum(grades)/len(grades)
print(new_mean)     
