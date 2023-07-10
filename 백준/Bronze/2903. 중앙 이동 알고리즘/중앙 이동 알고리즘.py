# 초기상태 4개 , 사각형 1개
# 늘어나는양 :기존 사각형 개수(늘어날 점) *4 + 기존 사각형 갯수(가운데점) - 겹치는 점(기존 4각형의 개수)
N=int(input())
before= 2
for i in range(1,N+1):
    before += before-1
print((before)**2)