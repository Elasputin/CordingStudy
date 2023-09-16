n = int(input())
doro = list(map(int, input().split()))
price = list(map(int, input().split()))
min_price = price[0] #첫번째 값을 설정
cost = 0
for i in range(n-1):
    if price[i] < min_price: #price[i] 가 min_price보다 작다면
        min_price = price[i]
    cost += doro[i] * min_price
print(cost)
        
        
