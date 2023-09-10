# 최대힙 문제 파이썬에는 그런데 최대힙이라는게 존재하지 않는다. 그러므로 다른 접근이 필요하다.
# 가장 높은 수를 (-1)로 곱하면 최소힙이 완성되고 거기에 (-1)을 곱하면 유사 최대힙이 될 수 있다.
import heapq
import sys
N = int(sys.stdin.readline().rstrip()) 
my_heap = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip()) *(-1)
    if num != 0:
        heapq.heappush(my_heap, num)
    else:
        if my_heap:
            print(heapq.heappop(my_heap)*(-1))
        else:
            print(0)
# 2차 시기 sys로 바꾸고 0이 아닌것을 먼저 처리