n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]  # 첫 도시의 가격을 최소 가격으로 초기화
total_cost = 0

for i in range(n - 1):
    if prices[i] < min_price:  # 현재 도시의 가격이 최소 가격보다 작다면 업데이트
        min_price = prices[i]
    total_cost += min_price * distances[i]

print(total_cost)

